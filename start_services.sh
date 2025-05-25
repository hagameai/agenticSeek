#!/bin/bash

source .env

command_exists() {
    command -v "$1" &> /dev/null
}

#
# Check if Docker is installed é running
#

if ! command_exists docker; then
    echo "Error: Docker is not installed. Please install Docker first."
    echo "On Ubuntu: sudo apt install docker.io"
    echo "On macOS/Windows: Install Docker Desktop from https://www.docker.com/get-started/"
    exit 1
fi

# Check if Docker daemon is running
echo "Checking if Docker daemon is running..."
if ! docker info &> /dev/null; then
    echo "Error: Docker daemon is not running or inaccessible."
    if [ "$(uname)" = "Linux" ]; then
        echo "Trying to start Docker service (may require sudo)..."
        if sudo systemctl start docker &> /dev/null; then
            echo "Docker started successfully."
        else
            echo "Failed to start Docker. Possible issues:"
            echo "1. Run this script with sudo: sudo bash setup_searxng.sh"
            echo "2. Check Docker installation: sudo systemctl status docker"
            echo "3. Add your user to the docker group: sudo usermod -aG docker $USER (then log out and back in)"
            exit 1
        fi
    else
        echo "Please start Docker manually:"
        echo "- On macOS/Windows: Open Docker Desktop."
        echo "- On Linux: Run 'sudo systemctl start docker' or check your distro's docs."
        exit 1
    fi
else
    echo "Docker daemon is running."
fi

# Check if Docker Compose is installed
if ! command_exists docker-compose && ! docker compose version >/dev/null 2>&1; then
    echo "Error: Docker Compose is not installed. Please install it first."
    echo "On Ubuntu: sudo apt install docker-compose"
    echo "Or via pip: pip install docker-compose"
    exit 1
fi

if command_exists docker-compose; then
    COMPOSE_CMD="docker-compose"
else
    COMPOSE_CMD="docker compose"
fi

# Check if docker-compose.yml exists
if [ ! -f "docker-compose.yml" ]; then
    echo "Error: docker-compose.yml not found in the current directory."
    exit 1
fi

# bundle based approach, commented out in favor of direct download for now
# Download and extract Chrome bundle if not present
#echo "Checking Chrome bundle..."
#if [ ! -d "chrome_bundle/chrome136" ]; then
#    echo "Chrome bundle not found. Downloading..."
#    mkdir -p chrome_bundle
#    curl -L https://github.com/Fosowl/agenticSeek/releases/download/utility/chrome136.zip -o /tmp/chrome136.zip
#    if [ $? -ne 0 ]; then
#        echo "Error: Failed to download Chrome bundle"
#        exit 1
#    fi
#    unzip -q /tmp/chrome136.zip -d chrome_bundle/
#    if [ $? -ne 0 ]; then
#        echo "Error: Failed to extract Chrome bundle"
#        exit 1
#    fi
#    rm /tmp/chrome136.zip
#    echo "Chrome bundle downloaded and extracted successfully"
#else
#    echo "Chrome bundle already exists"
#fi

# Stop all running containers to ensure a clean state
echo "Warning: stopping all docker containers (t-4 seconds)..."
sleep 4
docker stop $(docker ps -a -q)
echo "All containers stopped"

# First start backend and wait for it to be healthy
echo "Starting backend service..."
if ! $COMPOSE_CMD up -d backend; then
    echo "Error: Failed to start backend container."
    exit 1
fi

# Wait for backend to be healthy (check if it's running and not restarting)
echo "Waiting for backend to be ready..."
for i in {1..30}; do
    if [ "$(docker inspect -f '{{.State.Running}}' backend)" = "true" ] && \
       [ "$(docker inspect -f '{{.State.Restarting}}' backend)" = "false" ]; then
        echo "backend is ready!"
        break
    fi
    if [ $i -eq 30 ]; then
        echo "Error: backend failed to start properly after 30 seconds"
        $COMPOSE_CMD logs backend 
        exit 1
    fi
    sleep 1
done

# start remaining services for searxng, redis, frontend services

if ! $COMPOSE_CMD up; then
    echo "Error: Failed to start containers. Check Docker logs with '$COMPOSE_CMD logs'."
    echo "Possible fixes: Run with sudo or ensure port 8080 is free."
    exit 1
fi
sleep 10