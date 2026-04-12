# Comprehensive Broken Image Checker for all demo sites
# Checks both local files AND external URLs (Unsplash etc.)
# Outputs results as CSV-like format for easy analysis

$baseDir = "d:\sharkstars\demos"
$results = @()
$totalBroken = 0
$totalChecked = 0

$demoFolders = Get-ChildItem -Path $baseDir -Directory | Sort-Object Name

foreach ($folder in $demoFolders) {
    $indexPath = Join-Path $folder.FullName "index.html"
    if (-not (Test-Path $indexPath)) {
        continue
    }

    $content = Get-Content -Path $indexPath -Raw -Encoding UTF8

    # Extract img src attributes
    $imgMatches = [regex]::Matches($content, '<img[^>]+src=[''"]([^''"]+)[''"]')
    foreach ($match in $imgMatches) {
        $src = $match.Groups[1].Value
        if ($src -match "^data:") { continue }

        $totalChecked++
        $isBroken = $false

        if ($src -match "^https?://") {
            # External URL - do a HEAD request
            try {
                $response = Invoke-WebRequest -Uri $src -Method Head -TimeoutSec 10 -UseBasicParsing -ErrorAction Stop
                if ($response.StatusCode -ne 200) {
                    $isBroken = $true
                }
            } catch {
                $isBroken = $true
            }
        } else {
            # Local file
            $fullPath = Join-Path $folder.FullName $src
            $fullPath = [System.IO.Path]::GetFullPath($fullPath)
            if (-not (Test-Path $fullPath)) {
                $isBroken = $true
            }
        }

        if ($isBroken) {
            $totalBroken++
            $results += [PSCustomObject]@{
                Site = $folder.Name
                Type = "img"
                Source = $src
                Status = "BROKEN"
            }
        }
    }

    # Extract background-image: url(...) from inline styles
    $bgMatches = [regex]::Matches($content, "url\(['""]?([^'"")\s]+)['""]?\)")
    foreach ($match in $bgMatches) {
        $src = $match.Groups[1].Value
        if ($src -match "^data:") { continue }
        if ($src -match "^#") { continue }

        $totalChecked++
        $isBroken = $false

        if ($src -match "^https?://") {
            try {
                $response = Invoke-WebRequest -Uri $src -Method Head -TimeoutSec 10 -UseBasicParsing -ErrorAction Stop
                if ($response.StatusCode -ne 200) {
                    $isBroken = $true
                }
            } catch {
                $isBroken = $true
            }
        } else {
            $fullPath = Join-Path $folder.FullName $src
            $fullPath = [System.IO.Path]::GetFullPath($fullPath)
            if (-not (Test-Path $fullPath)) {
                $isBroken = $true
            }
        }

        if ($isBroken) {
            $totalBroken++
            $results += [PSCustomObject]@{
                Site = $folder.Name
                Type = "bg-image"
                Source = $src
                Status = "BROKEN"
            }
        }
    }

    # Also check CSS files
    $cssDir = Join-Path $folder.FullName "assist\css"
    if (Test-Path $cssDir) {
        $cssFiles = Get-ChildItem -Path $cssDir -Filter "*.css" -ErrorAction SilentlyContinue
        foreach ($cssFile in $cssFiles) {
            $cssContent = Get-Content -Path $cssFile.FullName -Raw -Encoding UTF8
            $cssBgMatches = [regex]::Matches($cssContent, "url\(['""]?([^'"")\s]+)['""]?\)")
            foreach ($match in $cssBgMatches) {
                $src = $match.Groups[1].Value
                if ($src -match "^https?://") {
                    $totalChecked++
                    try {
                        $response = Invoke-WebRequest -Uri $src -Method Head -TimeoutSec 10 -UseBasicParsing -ErrorAction Stop
                        if ($response.StatusCode -ne 200) {
                            $totalBroken++
                            $results += [PSCustomObject]@{
                                Site = $folder.Name
                                Type = "css-url"
                                Source = $src
                                Status = "BROKEN"
                            }
                        }
                    } catch {
                        $totalBroken++
                        $results += [PSCustomObject]@{
                            Site = $folder.Name
                            Type = "css-url"
                            Source = $src
                            Status = "BROKEN"
                        }
                    }
                    continue
                }
                if ($src -match "^data:") { continue }
                if ($src -match "^#") { continue }

                $totalChecked++
                $fullPath = Join-Path $cssFile.DirectoryName $src
                $fullPath = [System.IO.Path]::GetFullPath($fullPath)
                if (-not (Test-Path $fullPath)) {
                    $totalBroken++
                    $results += [PSCustomObject]@{
                        Site = $folder.Name
                        Type = "css-url"
                        Source = $src
                        Status = "BROKEN"
                    }
                }
            }
        }
    }

    $siteCount = ($results | Where-Object { $_.Site -eq $folder.Name }).Count
    if ($siteCount -gt 0) {
        Write-Host "BROKEN ($siteCount): $($folder.Name)" -ForegroundColor Red
    } else {
        Write-Host "OK: $($folder.Name)" -ForegroundColor Green
    }
}

Write-Host ""
Write-Host "============================================"
Write-Host "SUMMARY"
Write-Host "============================================"
Write-Host "Total images checked: $totalChecked"
Write-Host "Total broken: $totalBroken"
Write-Host ""

if ($results.Count -gt 0) {
    Write-Host "--- BROKEN IMAGE DETAILS ---"
    $results | Group-Object Site | ForEach-Object {
        Write-Host ""
        Write-Host "[$($_.Name)] ($($_.Count) broken)" -ForegroundColor Red
        $_.Group | ForEach-Object {
            $shortSrc = if ($_.Source.Length -gt 80) { $_.Source.Substring(0, 80) + "..." } else { $_.Source }
            Write-Host "  [$($_.Type)] $shortSrc" -ForegroundColor Yellow
        }
    }
}

# Save results to CSV
$csvPath = "d:\sharkstars\broken_images_report.csv"
$results | Export-Csv -Path $csvPath -NoTypeInformation -Encoding UTF8
Write-Host ""
Write-Host "Report saved to: $csvPath"
