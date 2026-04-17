Add-Type -AssemblyName System.Drawing
function Resize-Image {
    param([string]$Src, [string]$Dest, [int]$W, [int]$H)
    try {
        $img = [System.Drawing.Image]::FromFile($Src)
        $bmp = New-Object System.Drawing.Bitmap($W, $H)
        $g = [System.Drawing.Graphics]::FromImage($bmp)
        $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
        $g.DrawImage($img, 0, 0, $W, $H)
        $bmp.Save($Dest, [System.Drawing.Imaging.ImageFormat]::Jpeg)
        $g.Dispose()
        $bmp.Dispose()
        $img.Dispose()
        Write-Host "Resized $Src to $Dest"
    } catch {
        Write-Host "Error reszing $Src : $_"
    }
}
$dir = "d:\sharkstars\assist\images\thumbnails"
Resize-Image "$dir\agency-01.png" "$dir\agency-01-small.jpg" 800 450
Resize-Image "$dir\influencer-01.png" "$dir\influencer-01-small.jpg" 800 450
Resize-Image "$dir\yoga-01.png" "$dir\yoga-01-small.jpg" 800 450
Resize-Image "$dir\model-01.jpg" "$dir\model-01-small.jpg" 800 450
