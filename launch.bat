@echo off
cls
echo "Checking for python installation..."
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo "it looks like python is not installed."
    echo "if you think it's an error, try executing the file manually with 'python random_anime.py'"
    echo "if indeed python is not installed please install the latest version on the official website or update python (>=3.7)"
    pause
    exit /b
)
echo "By default, the launcher will try to download the required libraries."
echo "if you already have them installed you can skip by typing 'n'"


set /p answer="install or update required libraries ?[y/n]:"

if "%answer%"=="y" (
    echo "Installing packages..."
    pip install requests rich
) else (
    echo "Skipping packages installation..."
)

echo "Launching python script..."
cls
python random_anime.py
