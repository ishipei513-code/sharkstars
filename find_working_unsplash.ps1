$baseDir = "d:\sharkstars\demos"
$demoFolders = Get-ChildItem -Path $baseDir -Directory | Sort-Object Name

# Dictionary to store working URLs
$workingUrls = @{}

foreach ($folder in $demoFolders) {
    $indexPath = Join-Path $folder.FullName "index.html"
    if (-not (Test-Path $indexPath)) { continue }
    $content = Get-Content -Path $indexPath -Raw -Encoding UTF8

    $imgMatches = [regex]::Matches($content, 'https://images\.unsplash\.com/photo-[a-zA-Z0-9\-]+')
    foreach ($match in $imgMatches) {
        $url = $match.Value
        
        # Check if URL works
        try {
            $response = Invoke-WebRequest -Uri $url -Method Head -TimeoutSec 5 -UseBasicParsing -ErrorAction Stop
            if ($response.StatusCode -eq 200) {
                if (-not $workingUrls.ContainsKey($folder.Name)) {
                    $workingUrls[$folder.Name] = @()
                }
                if ($url -notin $workingUrls[$folder.Name]) {
                    $workingUrls[$folder.Name] += $url
                }
            }
        } catch {
            # Broken, ignore
        }
    }
}

foreach ($site in $workingUrls.Keys | Sort-Object) {
    Write-Host "Site: $site ($($workingUrls[$site].Count) valid Unsplash images)"
    foreach ($url in $workingUrls[$site]) {
        Write-Host "  $url"
    }
}
