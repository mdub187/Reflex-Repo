#!/bin/bash
# Deployment Startup Script for Reflex Application
# Ensures database is initialized before starting the application
# Compatible with Render, Railway, Fly.io, and other platforms

set -e  # Exit on error

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo "================================================================"
echo -e "${BLUE}Starting Reflex Application Deployment${NC}"
echo "================================================================"
echo ""

# Detect environment
if [ -n "$RENDER" ]; then
    echo -e "${GREEN}Render deployment detected${NC}"
    PLATFORM="Render"
elif [ -n "$RAILWAY_ENVIRONMENT" ]; then
    echo -e "${GREEN}🚂 Railway deployment detected${NC}"
    PLATFORM="Railway"
elif [ -n "$FLY_APP_NAME" ]; then
    echo -e "${GREEN}🪰 Fly.io deployment detected${NC}"
    PLATFORM="Fly.io"
else
    echo -e "${YELLOW}💻 Local/Generic deployment${NC}"
    PLATFORM="Generic"
fi

echo ""
echo "================================================================"
echo -e "${BLUE}Step 1: Environment Check${NC}"
echo "================================================================"

# Check Python version
PYTHON_VERSION=$(python --version 2>&1)
echo -e "${GREEN}✓ Python: $PYTHON_VERSION${NC}"

# Check if virtual environment exists and activate if needed
if [ -d ".venv" ] && [ -z "$VIRTUAL_ENV" ]; then
    echo -e "${YELLOW}Activating virtual environment...${NC}"
    source .venv/bin/activate
    echo -e "${GREEN}✓ Virtual environment activated${NC}"
elif [ -n "$VIRTUAL_ENV" ]; then
    echo -e "${GREEN}✓ Virtual environment already active${NC}"
else
    echo -e "${YELLOW}⚠ No virtual environment found (this is OK for containerized deployments)${NC}"
fi

# Verify Reflex is installed
if command -v reflex &> /dev/null; then
    REFLEX_VERSION=$(reflex --version 2>&1 || echo "unknown")
    echo -e "${GREEN}✓ Reflex installed: $REFLEX_VERSION${NC}"
else
    echo -e "${RED} Reflex is not installed${NC}"
    echo "Installing Reflex..."
    pip install reflex reflex-local-auth
fi

echo ""
echo "================================================================"
echo -e "${BLUE}Step 2: Database Initialization${NC}"
echo "================================================================"

# Initialize database tables
echo -e "${YELLOW}Running database initialization script...${NC}"
python init_db.py

if [ $? -eq 0 ]; then
    echo -e "${GREEN}Database initialization completed successfully${NC}"
else
    echo -e "${YELLOW}⚠️  Database initialization had warnings${NC}"
    echo "   Attempting to continue anyway..."

    # Try running reflex db init as fallback
    echo -e "${YELLOW}Trying 'reflex db init' as fallback...${NC}"
    reflex db init || echo -e "${YELLOW}⚠️  'reflex db init' also had issues, continuing anyway${NC}"
fi

echo ""
echo "================================================================"
echo -e "${BLUE}Step 3: Frontend Setup${NC}"
echo "================================================================"

# Initialize Reflex (creates .web directory and installs frontend dependencies)
if [ ! -d ".web" ]; then
    echo -e "${YELLOW}Initializing Reflex frontend...${NC}"
    reflex init

    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✓ Frontend initialized${NC}"
    else
        echo -e "${RED} Frontend initialization failed${NC}"
        exit 1
    fi
else
    echo -e "${GREEN}✓ Frontend already initialized${NC}"
fi

# Check if node_modules exists, if not, install dependencies
if [ ! -d ".web/node_modules" ]; then
    echo -e "${YELLOW}Installing frontend dependencies...${NC}"
    cd .web

    # Try npm first, then fallback to bun if available
    if command -v npm &> /dev/null; then
        npm install --legacy-peer-deps --prefer-offline
        if [ $? -eq 0 ]; then
            echo -e "${GREEN}✓ Frontend dependencies installed with npm${NC}"
        else
            echo -e "${YELLOW}⚠️  npm install had issues, trying bun...${NC}"
            if command -v bun &> /dev/null; then
                bun install
                echo -e "${GREEN}✓ Frontend dependencies installed with bun${NC}"
            else
                echo -e "${RED} Frontend dependency installation failed${NC}"
                cd ..
                exit 1
            fi
        fi
    elif command -v bun &> /dev/null; then
        bun install
        echo -e "${GREEN}✓ Frontend dependencies installed with bun${NC}"
    else
        echo -e "${RED} Neither npm nor bun found${NC}"
        cd ..
        exit 1
    fi

    cd ..
else
    echo -e "${GREEN}✓ Frontend dependencies already installed${NC}"
fi

echo ""
echo "================================================================"
echo -e "${BLUE}Step 4: Configuration Summary${NC}"
echo "================================================================"

# Display configuration
echo "Platform: $PLATFORM"
echo "Database URL: ${DATABASE_URL:0:50}..." || echo "Database URL: Using default SQLite"
echo "Backend Port: ${BACKEND_PORT:-8000}"
echo "Frontend Port: ${FRONTEND_PORT:-3000}"
echo "Deploy URL: ${RENDER_EXTERNAL_URL:-${RAILWAY_PUBLIC_DOMAIN:-${FLY_APP_NAME:-localhost}}}"

echo ""
echo "================================================================"
echo -e "${GREEN}Deployment preparation complete!${NC}"
echo "================================================================"
echo ""
echo -e "${BLUE}Starting Reflex server...${NC}"
echo ""

# Set production flag
export PRODUCTION=true

# Start Reflex in production mode
exec reflex run --env prod
