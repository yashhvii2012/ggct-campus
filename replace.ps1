$ErrorActionPreference = "Stop"

$b64 = [System.IO.File]::ReadAllText("logo_b64.txt").Trim()
$content = [System.IO.File]::ReadAllText("ggct_campus.html")

$splashSvg = @"
    <svg class="splash-logo-svg" viewBox="0 0 52 52">
      <defs><radialGradient id="g1" cx="50%" cy="50%"><stop offset="0%" stop-color="#0050c8"/><stop offset="100%" stop-color="#001a5c"/></radialGradient></defs>
      <circle cx="26" cy="26" r="26" fill="url(#g1)"/>
      <circle cx="26" cy="26" r="20" fill="none" stroke="#FFB800" stroke-width="2.5"/>
      <circle cx="26" cy="26" r="9" fill="#FFB800"/>
      <line x1="26" y1="6" x2="26" y2="46" stroke="#FFB800" stroke-width="1.5" opacity=".4"/>
      <line x1="6" y1="26" x2="46" y2="26" stroke="#FFB800" stroke-width="1.5" opacity=".4"/>
      <line x1="12" y1="12" x2="40" y2="40" stroke="#FFB800" stroke-width="1" opacity=".25"/>
      <line x1="40" y1="12" x2="12" y2="40" stroke="#FFB800" stroke-width="1" opacity=".25"/>
    </svg>
"@

$loginSvg = @"
      <svg width="38" height="38" viewBox="0 0 52 52">
        <circle cx="26" cy="26" r="26" fill="#003087"/>
        <circle cx="26" cy="26" r="20" fill="none" stroke="#FFB800" stroke-width="2.5"/>
        <circle cx="26" cy="26" r="9" fill="#FFB800"/>
      </svg>
"@

$dropdown = @"
      <select id="branch-sel">
        <option value="">-- Select Branch --</option>
        <optgroup label="B.E. / B.Tech">
          <option>Computer Science Engineering (CSE)</option>
          <option>Information Technology (IT)</option>
          <option>Electronics &amp; Communication (EC)</option>
          <option>Electrical Engineering (EE)</option>
          <option>Mechanical Engineering (ME)</option>
          <option>Civil Engineering (CE)</option>
        </optgroup>
        <optgroup label="PG Programs">
          <option>MBA</option><option>MCA</option><option>M.Tech (CSE)</option><option>M.Tech (EC)</option>
        </optgroup>
        <optgroup label="Pharmacy">
          <option>B.Pharm</option><option>M.Pharm</option>
        </optgroup>
        <optgroup label="Diploma">
          <option>Diploma – Computer Science</option><option>Diploma – Mechanical</option><option>Diploma – Civil</option>
        </optgroup>
      </select>
"@

$splashImg = '    <img src="data:image/png;base64,' + $b64 + '" alt="GGCT Logo" style="width: 52px; height: 52px; object-fit: contain;">'
$loginImg = '      <img src="data:image/png;base64,' + $b64 + '" alt="GGCT Logo" style="width: 38px; height: 38px; object-fit: contain;">'

$newDropdown = @"
      <select id="branch-sel">
        <option value="">-- Select Branch --</option>
        <optgroup label="B.Tech">
          <option>Computer Science Engineering (CSE)</option>
          <option>CSE – AI &amp; Data Science (AIDS)</option>
          <option>CSE – AI &amp; Machine Learning (AIML)</option>
        </optgroup>
      </select>
"@

$content = $content -replace "`r`n", "`n"
$splashSvg = $splashSvg -replace "`r`n", "`n"
$loginSvg = $loginSvg -replace "`r`n", "`n"
$dropdown = $dropdown -replace "`r`n", "`n"

if ($content.Contains($splashSvg)) {
    $content = $content.Replace($splashSvg, $splashImg)
    Write-Output "Splash replaced"
} else {
    Write-Output "Splash not found"
}

if ($content.Contains($loginSvg)) {
    $content = $content.Replace($loginSvg, $loginImg)
    Write-Output "Login replaced"
} else {
    Write-Output "Login not found"
}

if ($content.Contains($dropdown)) {
    $content = $content.Replace($dropdown, $newDropdown)
    Write-Output "Dropdown replaced"
} else {
    Write-Output "Dropdown not found"
}

[System.IO.File]::WriteAllText("ggct_campus.html", $content)
Write-Output "Done"
