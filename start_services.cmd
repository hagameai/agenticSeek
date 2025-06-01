@echo off

if "%1"=="full" (
    echo Starting full deployment...
) else (
    echo Starting partial deployment... (backend run on host), use "full" to run all services in containers
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