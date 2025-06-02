@echo off

if "%1"=="full" (
    echo Starting full deployment...
) else (
    echo Starting partial deployment... (backend run on host), use "full" to run all services in containers
)

where openssl >nul 2>&1
if %ERRORLEVEL% == 0 (
    for /f %%i in ('openssl rand -hex 32') do set SEARXNG_SECRET_KEY=%%i
) else (
    where python3 >nul 2>&1
    if %ERRORLEVEL% == 0 (
        for /f %%i in ('python3 -c "import secrets; print(secrets.token_hex(32))"') do set SEARXNG_SECRET_KEY=%%i
    ) else (
        echo Error: Neither openssl nor python is available to generate a secret key.
        exit /b 1
    )
)

REM Stop all containers
echo Stopping containers...
docker stop $(docker ps -aq) >nul 2>&1

REM Generate secret key
for /f %%i in ('powershell -command "[System.Web.Security.Membership]::GeneratePassword(64,0)"') do set SEARXNG_SECRET_KEY=%%i

if "%1"=="full" (
    docker compose up -d backend
    timeout /t 5 /nobreak >nul
    docker compose --profile full up
) else (
    docker compose --profile core up
)