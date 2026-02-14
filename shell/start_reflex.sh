#!/bin/bash

# Enhanced Reflex Startup Script with Dynamic Port Selection
# Automatically finds available ports and handles package installation

set -e

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Default ports
BACKEND_PORT=${BACKEND_PORT:-8000}
FRONTEND_PORT=${FRONTEND_PORT:-3000}

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -b|--backend-port)
            BACKEND_PORT="$2"
            shift 2
            ;;
        -f|--frontend-port)
            FRONTEND_PORT="$2"
            shift 2
            ;;
        --clean)
            CLEAN_BUILD=true
            shift
            ;;
        -h|--help)
            echo "Usage: $0 [options]"
            echo ""
            echo "Options:"
            echo "  -b, --backend-port PORT    Set backend port (default: 8000)"
            echo "  -f, --frontend-port PORT   Set frontend port (default: 3000)"
            echo "  --clean                    Clean rebuild (.web directory)"
            echo "  -h, --help                 Show this help message"
            echo ""
            echo "Environment variables:"
            echo "  BACKEND_PORT               Backend port (default: 8000)"
            echo "  FRONTEND_PORT              Frontend port (default: 3000)"
            echo ""
            echo "Examples:"
            echo "  $0                         # Use default ports"
            echo "  $0 -b 8080 -f 3001        # Use custom ports"
            echo "  $0 --clean                 # Clean rebuild"
            echo "  BACKEND_PORT=9000 $0      # Use env variable"
            exit 0
            ;;
        *)
            echo -e "${RED}Unknown option: $1${NC}"
            echo "Use -h or --help for usage information"
            exit 1
            ;;
    esac
done

echo -e "${BLUE}🚀 Starting Reflex Application...${NC}"
echo "=================================="

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Function to check if port is available
check_port() {
    local port=$1
    if lsof -Pi :$port -sTCP:LISTEN -t >/dev/null 2>&1 ; then
        return 1  # Port in use
    else
        return 0  # Port available
    fi
}

# Function to find next available port
find_available_port() {
    local start_port=$1
    local max_attempts=${2:-10}
    
    for ((port=start_port; port<start_port+max_attempts; port++)); do
        if check_port $port; then
            echo $port
            return 0
        fi
    done
    
    return 1
}

# Kill any existing processes on specified ports
echo -e "${YELLOW}Checking for processes on ports $BACKEND_PORT and $FRONTEND_PORT...${NC}"

if lsof -Pi :$BACKEND_PORT -sTCP:LISTEN -t >/dev/null 2>&1; then
    echo -e "${YELLOW}⚠️  Port $BACKEND_PORT is in use. Finding alternative...${NC}"
    NEW_BACKEND_PORT=$(find_available_port $BACKEND_PORT)
    if [ $? -eq 0 ]; then
        BACKEND_PORT=$NEW_BACKEND_PORT
        echo -e "${GREEN}✓ Using backend port: $BACKEND_PORT${NC}"
    else
        echo -e "${RED}❌ Could not find available backend port${NC}"
        exit 1
    fi
else
    echo -e "${GREEN}✓ Backend port $BACKEND_PORT is available${NC}"
fi

if lsof -Pi :$FRONTEND_PORT -sTCP:LISTEN -t >/dev/null 2>&1; then
    echo -e "${YELLOW}⚠️  Port $FRONTEND_PORT is in use. Finding alternative...${NC}"
    NEW_FRONTEND_PORT=$(find_available_port $FRONTEND_PORT)
    if [ $? -eq 0 ]; then
        FRONTEND_PORT=$NEW_FRONTEND_PORT
        echo -e "${GREEN}✓ Using frontend port: $FRONTEND_PORT${NC}"
    else
        echo -e "${RED}❌ Could not find available frontend port${NC}"
        exit 1
    fi
else
    echo -e "${GREEN}✓ Frontend port $FRONTEND_PORT is available${NC}"
fi

# Export ports for rxconfig.py to use (if needed)
export BACKEND_PORT
export FRONTEND_PORT

# Kill any hanging processes
echo -e "${YELLOW}Cleaning up old processes...${NC}"
pkill -9 -f "reflex run" 2>/dev/null && echo -e "${GREEN}✓ Killed old reflex processes${NC}" || true
pkill -9 -f "bun install" 2>/dev/null && echo -e "${GREEN}✓ Killed hanging bun processes${NC}" || true

sleep 2

# Check if virtual environment is activated
if [[ -z "$VIRTUAL_ENV" ]]; then
    echo -e "${YELLOW}Activating virtual environment...${NC}"
    if [ -d ".venv" ]; then
        source .venv/bin/activate
        echo -e "${GREEN}✓ Virtual environment activated${NC}"
    else
        echo -e "${RED}❌ No .venv found. Please create a virtual environment first.${NC}"
        exit 1
    fi
fi

# Verify Reflex is installed
if ! command -v reflex &> /dev/null; then
    echo -e "${RED}❌ Reflex is not installed. Run: pip install reflex${NC}"
    exit 1
fi

echo -e "${GREEN}✓ All prerequisites met${NC}"
echo ""

# Clean rebuild if requested
if [ "$CLEAN_BUILD" = true ]; then
    echo -e "${YELLOW}Performing clean rebuild...${NC}"
    rm -rf .web .states
    echo -e "${GREEN}✓ Cleaned .web and .states directories${NC}"
fi

# Check if .web directory exists and has node_modules
if [ ! -d ".web/node_modules" ]; then
    echo -e "${BLUE}Initializing .web directory...${NC}"
    reflex init
    
    echo -e "${BLUE}Installing frontend packages with npm...${NC}"
    cd .web
    npm install --legacy-peer-deps --prefer-offline
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✓ All packages installed${NC}"
    else
        echo -e "${RED}❌ Package installation failed${NC}"
        cd ..
        exit 1
    fi
    cd ..
else
    echo -e "${GREEN}✓ Frontend packages already installed${NC}"
fi

echo ""
echo -e "${GREEN}Starting Reflex server...${NC}"
echo "=================================="
echo ""
echo -e "Backend will run on:  ${BLUE}http://localhost:$BACKEND_PORT${NC}"
echo -e "Frontend will run on: ${BLUE}http://localhost:$FRONTEND_PORT${NC}"
echo ""
echo -e "${YELLOW}Note: Dynamic port selection is enabled in rxconfig.py${NC}"
echo -e "${YELLOW}If ports are in use, Reflex will find the next available port${NC}"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Start Reflex
exec reflex run