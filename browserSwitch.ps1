function Set-DefaultBrowser {
    param($defaultBrowser)

    $regKey      = "HKCU:\Software\Microsoft\Windows\Shell\Associations\UrlAssociations\{0}\UserChoice"
    #$regKeyFtp   = $regKey -f 'ftp'
    $regKeyHttp  = $regKey -f 'http'
    $regKeyHttps = $regKey -f 'https'

    switch -Regex ($defaultBrowser.ToLower())
    {
        # Firefox
        'ff|firefox' {
            #Set-ItemProperty $regKeyFtp   -name ProgId FirefoxURL
            Set-ItemProperty $regKeyHttp  -name ProgId FirefoxURL
            Set-ItemProperty $regKeyHttps -name ProgId FirefoxURL
            break
        }
        # Google Chrome
        'cr|google|chrome' {
            #Set-ItemProperty $regKeyFtp   -name ProgId ChromeHTML
            Set-ItemProperty $regKeyHttp  -name ProgId ChromeHTML
            Set-ItemProperty $regKeyHttps -name ProgId ChromeHTML
            break
        }
        # Opera
        'op*' {
            #Set-ItemProperty $regKeyFtp   -name ProgId Opera.Protocol
            Set-ItemProperty $regKeyHttp  -name ProgId Opera.Protocol
            Set-ItemProperty $regKeyHttps -name ProgId Opera.Protocol
            break
        }
    } 
}

function Get-DefaultBrowser {
    return (Get-ItemProperty HKCU:\Software\Microsoft\windows\Shell\Associations\UrlAssociations\http\UserChoice).Progid
}

$currentBrowser = Get-DefaultBrowser
Write-Host $currentBrowser
switch -Regex ($currentBrowser.ToLower()) {
    # Firefox
    'ff|firefox' {
        Write-Host "Switching to chrome..."
        Set-DefaultBrowser "cr"
        break
    }
    # Google Chrome
    'cr|google|chrome' {
        Write-Host "Switching to firefox..."
        Set-DefaultBrowser "ff"
        break
    }
    'edge|msedge|msedgehtm' {
        Write-Host "Switching to firefox..."
        Set-DefaultBrowser "ff"
        break
    }
}
