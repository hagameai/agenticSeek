@echo off
echo Starting installation for Windows...

REM Check if uv is installed
uv --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: uv is not installed. Please install uv first.
    echo You can install it using: powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
    pause
    exit /b 1
)

REM Initialize uv project if pyproject.toml doesn't exist
if not exist "pyproject.toml" (
    echo Initializing uv project...
    uv init --python 3.10
    if %errorlevel% neq 0 (
        echo Failed to initialize uv project
        pause
        exit /b 1
    )
)

REM Sync the project (creates venv and installs dependencies)
echo Setting up Python environment with uv...
uv sync --python 3.10
if %errorlevel% neq 0 (
    echo Failed to sync uv project
    pause
    exit /b 1
)

REM Add specific packages
echo Adding pyreadline3...
uv add pyreadline3
if %errorlevel% neq 0 (
    echo Failed to add pyreadline3
    pause
    exit /b 1
)

echo Adding Selenium...
uv add selenium
if %errorlevel% neq 0 (
    echo Failed to add selenium
    pause
    exit /b 1
)

REM Add dependencies from requirements.txt if it exists
if exist "requirements.txt" (
    echo Adding dependencies from requirements.txt...
    uv add -r requirements.txt
    if %errorlevel% neq 0 (
        echo Warning: Some packages from requirements.txt failed to install.
    )
)

echo Installation complete for Windows!
echo To activate the environment, run: .venv\Scripts\activate
echo Or run commands with: uv run ^<command^>
echo.
echo Note: pyAudio installation may require additional steps on Windows.
echo If pyAudio fails to install, please install portaudio manually and try again.
echo Also, chromedriver-autoinstaller should handle chromedriver automatically.
echo If needed, download chromedriver manually from: https://sites.google.com/chromium.org/driver/getting-started
pause