# Extract full broken URLs with their alt text context
$baseDir = "d:\sharkstars\demos"
$demoFolders = Get-ChildItem -Path $baseDir -Directory | Sort-Object Name

foreach ($folder in $demoFolders) {
    $indexPath = Join-Path $folder.FullName "index.html"
    if (-not (Test-Path $indexPath)) { continue }
    $content = Get-Content -Path $indexPath -Raw -Encoding UTF8

    $brokenFound = $false

    # Check img tags
    $imgMatches = [regex]::Matches($content, '<img[^>]+src=[''"]([^''"]+)[''"][^>]*>')
    foreach ($match in $imgMatches) {
        $src = $match.Groups[1].Value
        if ($src -match "^data:" -or -not ($src -match "^https?://")) { continue }
        
        try {
            $response = Invoke-WebRequest -Uri $src -Method Head -TimeoutSec 8 -UseBasicParsing -ErrorAction Stop
            if ($response.StatusCode -eq 200) { continue }
        } catch {}

        # Extract alt text
        $altMatch = [regex]::Match($match.Value, 'alt=[''"]([^''"]*)[''"]')
        $altText = if ($altMatch.Success) { $altMatch.Groups[1].Value } else { "N/A" }
        
        if (-not $brokenFound) {
            Write-Host "`n=== $($folder.Name) ===" -ForegroundColor Cyan
            $brokenFound = $true
        }
        Write-Host "  ALT: $altText" -ForegroundColor Yellow
        Write-Host "  URL: $src" -ForegroundColor Red
    }

    # Check CSS background-image in inline styles
    $bgMatches = [regex]::Matches($content, "style=['""][^'""]*background(?:-image)?:\s*url\(['""]?([^'"")\s]+)['""]?\)[^'""]*['""]")
    foreach ($match in $bgMatches) {
        $src = $match.Groups[1].Value
        if ($src -match "^data:" -or -not ($src -match "^https?://")) { continue }

        try {
            $response = Invoke-WebRequest -Uri $src -Method Head -TimeoutSec 8 -UseBasicParsing -ErrorAction Stop
            if ($response.StatusCode -eq 200) { continue }
        } catch {}

        if (-not $brokenFound) {
            Write-Host "`n=== $($folder.Name) ===" -ForegroundColor Cyan
            $brokenFound = $true
        }
        Write-Host "  ALT: [bg-image inline]" -ForegroundColor Yellow
        Write-Host "  URL: $src" -ForegroundColor Red
    }

    # Check CSS files
    $cssDir = Join-Path $folder.FullName "assist\css"
    if (Test-Path $cssDir) {
        $cssFiles = Get-ChildItem -Path $cssDir -Filter "*.css" -ErrorAction SilentlyContinue
        foreach ($cssFile in $cssFiles) {
            $cssContent = Get-Content -Path $cssFile.FullName -Raw -Encoding UTF8
            $cssBgMatches = [regex]::Matches($cssContent, "url\(['""]?([^'"")\s]+)['""]?\)")
            foreach ($match in $cssBgMatches) {
                $src = $match.Groups[1].Value
                if (-not ($src -match "^https?://")) { continue }
                
                try {
                    $response = Invoke-WebRequest -Uri $src -Method Head -TimeoutSec 8 -UseBasicParsing -ErrorAction Stop
                    if ($response.StatusCode -eq 200) { continue }
                } catch {}

                if (-not $brokenFound) {
                    Write-Host "`n=== $($folder.Name) ===" -ForegroundColor Cyan
                    $brokenFound = $true
                }
                Write-Host "  ALT: [CSS background in $($cssFile.Name)]" -ForegroundColor Yellow
                Write-Host "  URL: $src" -ForegroundColor Red
            }
        }
    }
}
