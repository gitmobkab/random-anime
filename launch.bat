@echo off
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo "it looks like python is not installed."
    echo "if you think it's an error, try executing the file manually with 'python random_anime.py'"
    echo "if indeed python is not installed please install the latest version on the official website or update python (>=3.7)"
    pause
    exit /b
)

REM Install packages
pip install requests rich
pause
