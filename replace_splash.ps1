$content = Get-Content -Path "c:\Users\Yashvii\OneDrive\Documents\gg\index.html" -Raw

$old_css = @"
    /* SPLASH */
    #splash {
      background: linear-gradient(160deg, #001a5c 0%, #003087 60%, #0050c8 100%);
      align-items: center;
      justify-content: center;
      gap: 28px
    }
"@

$new_css = @"
    /* SPLASH */
    #splash {
      position: relative;
      align-items: center;
      justify-content: center;
      gap: 20px;
      overflow: hidden;
    }
    .splash-bg {
      position: absolute;
      inset: 0;
      background-image: url('college.jpg');
      background-size: cover;
      background-position: center;
      filter: brightness(0.45);
      z-index: 0;
    }
    .splash-content {
      position: relative;
      z-index: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 18px;
    }
    .splash-college-logo {
      width: 120px;
      height: 120px;
      border-radius: 50%;
      background: white;
      padding: 10px;
      object-fit: contain;
      box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    }
    .splash-college-name {
      color: #ffffff;
      font-size: 18px;
      font-weight: 800;
      font-family: 'Poppins', sans-serif;
      text-align: center;
      text-shadow: 0 2px 8px rgba(0,0,0,0.5);
      padding: 0 24px;
      line-height: 1.4;
    }
"@

$content = $content.Replace($old_css, $new_css)

$pattern = '(?s)<div id="splash" class="screen active">.*?</div>\s*<!-- LOGIN -->'
$replacement = @"
<div id="splash" class="screen active">
      <div class="splash-bg"></div>
      <div class="splash-content">
        <img src="logo.png" alt="GGCT Logo" class="splash-college-logo" />
        <div class="splash-college-name">Gyan Ganga College of Technology</div>
        <div class="splash-dots">
          <div class="dot"></div>
          <div class="dot"></div>
          <div class="dot"></div>
        </div>
      </div>
    </div>
    <!-- LOGIN -->
"@

$content = [regex]::Replace($content, $pattern, $replacement)

$content | Out-File -FilePath "c:\Users\Yashvii\OneDrive\Documents\gg\index.html" -Encoding utf8
Write-Host "Replacement successful!"
