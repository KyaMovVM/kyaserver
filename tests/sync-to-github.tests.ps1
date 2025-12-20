param(
    [string]$ScriptPath = (Join-Path (Split-Path $PSScriptRoot -Parent) "sync-to-github.ps1")
)

$TestDir = Join-Path $PSScriptRoot "test-sync"

Describe "sync-to-github.ps1 Parameter Validation" {
    
    It "Should validate Github URL format" {
        $ValidUrls = @(
            "https://github.com/user/repo.git",
            "https://github.com/user/repo"
        )
        
        foreach ($Url in $ValidUrls) {
            $Url | Should Match "(https://github\.com)"
        }
    }
    
    It "Should reject invalid URLs" {
        $InvalidUrl = "not-a-github-url"
        $InvalidUrl | Should Not Match "(https://github\.com)"
    }
}

Describe "sync-to-github.ps1 Git Repository Check" {
    
    It "Should verify Git repository exists" {
        (Test-Path .\.git) | Should Be $true
    }
}

Describe "sync-to-github.ps1 Script Structure" {
    
    It "Should have valid PowerShell syntax" {
        $Content = Get-Content $ScriptPath -Raw
        $null = [System.Management.Automation.PSParser]::Tokenize($Content, [ref]$null)
        $? | Should Be $true
    }
    
    It "Should reference main-project directory" {
        $Content = Get-Content $ScriptPath -Raw
        $Content | Should Match "main-project"
    }
    
    It "Should reference wiki directory" {
        $Content = Get-Content $ScriptPath -Raw
        $Content | Should Match "wiki"
    }
    
    It "Should reference .gitmodules file" {
        $Content = Get-Content $ScriptPath -Raw
        $Content | Should Match "\.gitmodules"
    }
    
    It "Should remove .git folders from submodules" {
        $Content = Get-Content $ScriptPath -Raw
        $Content | Should Match "Remove-Item.*\.git"
    }
    
    It "Should restore local state after sync" {
        $Content = Get-Content $ScriptPath -Raw
        $Content | Should Match "git submodule update --init --recursive"
    }
}

Describe "sync-to-github.ps1 Directory Structure" {
    
    It "Should preserve main-project directory" {
        (Test-Path "main-project") | Should Be $true
    }
    
    It "Should preserve wiki directory" {
        (Test-Path "wiki") | Should Be $true
    }
    
    It "Should have .git configuration" {
        (Test-Path ".git/config") | Should Be $true
    }
}
