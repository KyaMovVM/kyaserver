#!/usr/bin/env pwsh

# Script to run sync-to-github.ps1 tests using Pester

param(
    [switch]$Verbose
)

Write-Host "sync-to-github.ps1 Test Suite" -ForegroundColor Green
Write-Host "==============================" -ForegroundColor Green
Write-Host ""

# Check if Pester is installed
$PesterModule = Get-Module -Name Pester -ListAvailable
if (-not $PesterModule) {
    Write-Host "Installing Pester..." -ForegroundColor Yellow
    Install-Module -Name Pester -Force -SkipPublisherCheck
}

# Import Pester
Import-Module Pester

# Get the test file path
$TestFile = Join-Path $PSScriptRoot "tests\sync-to-github.tests.ps1"
$ScriptFile = Join-Path $PSScriptRoot "sync-to-github.ps1"

if (-not (Test-Path $TestFile)) {
    Write-Error "Test file not found: $TestFile"
    exit 1
}

if (-not (Test-Path $ScriptFile)) {
    Write-Error "Script file not found: $ScriptFile"
    exit 1
}

# Run tests
Write-Host "Running tests from: $TestFile" -ForegroundColor Cyan
Write-Host ""

$Results = Invoke-Pester -Path $TestFile -PassThru

# Summary
Write-Host ""
Write-Host "==============================" -ForegroundColor Green
Write-Host "Test Results Summary" -ForegroundColor Green
Write-Host "==============================" -ForegroundColor Green
Write-Host "Total Tests:  $($Results.Tests.Count)" -ForegroundColor Cyan
Write-Host "Passed:       $($Results.Tests.Passed.Count)" -ForegroundColor Green
Write-Host "Failed:       $($Results.Tests.Failed.Count)" -ForegroundColor $(if ($Results.Tests.Failed.Count -gt 0) { "Red" } else { "Green" })
Write-Host "Skipped:      $($Results.Tests.Skipped.Count)" -ForegroundColor Yellow
Write-Host ""

# Exit with test result status
if ($Results.Tests.Failed.Count -gt 0) {
    exit 1
} else {
    exit 0
}
