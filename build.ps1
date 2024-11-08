# DOT503 ASSESSMENT 2 - BUILD AND DEPLOYMENT INSTRUCTION

# Clean up previous builds
Write-Output "CLEANING PREV BUILD"
Remove-Item -Recurse -Force dist -ErrorAction SilentlyContinue
New-Item -ItemType Directory -Path dist

# run the unit test file
Write-Output "UNIT TEST ONGOING"
python -m unittest test_simple_calc.py

# checker
if ($LASTEXITCODE -ne 0) {
    Write-Output "UNIT TEST FAILED. ABORTING BUILD."
    exit 1
}

# build the project
Write-Output "PROCEEDING TO BUILD"
Copy-Item simple_calc.py dist/

# package the application
Write-Output "PROCEEDING TO PACKAGING"
Compress-Archive -Path "dist\simple_calc.py" -DestinationPath "dist\simple_calc_package.zip"
Write-Output "PACKAGE CREATED -- PATH: dist\simple_calc_package.zip"

# when build is complete
Write-Output "BUILD AND PACKAGING DONE"