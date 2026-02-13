#!/bin/bash

# Project Cleanup Script for Reflex-Repo
# Removes build artifacts, cache files, and optimizes structure

set -e

echo "🧹 Starting Project Cleanup..."
echo "================================"

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Counter for cleaned items
CLEANED_COUNT=0

echo ""
echo -e "${BLUE}1. Removing Python cache files (.pyc, .pyo)...${NC}"
PYCS=$(find . -path ./.venv -prune -o -type f \( -name "*.pyc" -o -name "*.pyo" \) -print | wc -l | xargs)
if [ "$PYCS" -gt 0 ]; then
    find . -path ./.venv -prune -o -type f \( -name "*.pyc" -o -name "*.pyo" \) -delete
    echo -e "${GREEN}✓ Removed $PYCS .pyc/.pyo files${NC}"
    CLEANED_COUNT=$((CLEANED_COUNT + PYCS))
else
    echo -e "${GREEN}✓ No .pyc/.pyo files found${NC}"
fi

echo ""
echo -e "${BLUE}2. Removing __pycache__ directories...${NC}"
PYCACHE_DIRS=$(find . -path ./.venv -prune -o -type d -name "__pycache__" -print | wc -l | xargs)
if [ "$PYCACHE_DIRS" -gt 0 ]; then
    find . -path ./.venv -prune -o -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
    echo -e "${GREEN}✓ Removed $PYCACHE_DIRS __pycache__ directories${NC}"
    CLEANED_COUNT=$((CLEANED_COUNT + PYCACHE_DIRS))
else
    echo -e "${GREEN}✓ No __pycache__ directories found${NC}"
fi

echo ""
echo -e "${BLUE}3. Checking for duplicate alembic directory...${NC}"
if [ -d "alembic" ] && [ -d "alembic_migrations" ]; then
    echo -e "${YELLOW}⚠️  Found duplicate alembic directories${NC}"
    echo -e "${YELLOW}   Keep: alembic_migrations/ (has 2 migrations)${NC}"
    echo -e "${YELLOW}   Remove: alembic/ (has 1 migration)${NC}"
    read -p "Do you want to remove the duplicate 'alembic/' directory? (y/N) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        rm -rf alembic/
        echo -e "${GREEN}✓ Removed duplicate alembic/ directory${NC}"
        CLEANED_COUNT=$((CLEANED_COUNT + 1))
    else
        echo -e "${YELLOW}⊘ Skipped - keeping alembic/ directory${NC}"
    fi
else
    echo -e "${GREEN}✓ No duplicate alembic directory found${NC}"
fi

echo ""
echo -e "${BLUE}4. Removing .pytest_cache...${NC}"
if [ -d ".pytest_cache" ]; then
    rm -rf .pytest_cache
    echo -e "${GREEN}✓ Removed .pytest_cache${NC}"
    CLEANED_COUNT=$((CLEANED_COUNT + 1))
else
    echo -e "${GREEN}✓ No .pytest_cache found${NC}"
fi

echo ""
echo -e "${BLUE}5. Removing .ruff_cache...${NC}"
if [ -d ".ruff_cache" ]; then
    rm -rf .ruff_cache
    echo -e "${GREEN}✓ Removed .ruff_cache${NC}"
    CLEANED_COUNT=$((CLEANED_COUNT + 1))
else
    echo -e "${GREEN}✓ No .ruff_cache found${NC}"
fi

echo ""
echo -e "${BLUE}6. Checking .DS_Store files (macOS)...${NC}"
DSSTORE=$(find . -path ./.venv -prune -o -name ".DS_Store" -print | wc -l | xargs)
if [ "$DSSTORE" -gt 0 ]; then
    find . -path ./.venv -prune -o -name ".DS_Store" -delete
    echo -e "${GREEN}✓ Removed $DSSTORE .DS_Store files${NC}"
    CLEANED_COUNT=$((CLEANED_COUNT + DSSTORE))
else
    echo -e "${GREEN}✓ No .DS_Store files found${NC}"
fi

echo ""
echo -e "${BLUE}7. Checking for .pyc files in git tracking...${NC}"
if git rev-parse --git-dir > /dev/null 2>&1; then
    TRACKED_PYC=$(git ls-files | grep -c "\.pyc$" || true)
    if [ "$TRACKED_PYC" -gt 0 ]; then
        echo -e "${YELLOW}⚠️  Found $TRACKED_PYC .pyc files tracked by git${NC}"
        read -p "Remove them from git tracking? (y/N) " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            git ls-files | grep "\.pyc$" | xargs git rm --cached 2>/dev/null || true
            echo -e "${GREEN}✓ Removed .pyc files from git tracking${NC}"
        fi
    else
        echo -e "${GREEN}✓ No .pyc files in git tracking${NC}"
    fi
else
    echo -e "${YELLOW}⊘ Not a git repository, skipping git checks${NC}"
fi

echo ""
echo -e "${BLUE}8. Checking disk usage...${NC}"
BEFORE_SIZE=$(du -sh . 2>/dev/null | awk '{print $1}')
echo -e "   Project size: ${YELLOW}${BEFORE_SIZE}${NC}"
echo ""
echo -e "   Breakdown:"
if [ -d ".venv" ]; then
    VENV_SIZE=$(du -sh .venv 2>/dev/null | awk '{print $1}')
    echo -e "   - .venv/: ${VENV_SIZE}"
fi
if [ -d ".web" ]; then
    WEB_SIZE=$(du -sh .web 2>/dev/null | awk '{print $1}')
    echo -e "   - .web/: ${WEB_SIZE}"
fi
if [ -d "lmrex" ]; then
    LMREX_SIZE=$(du -sh lmrex 2>/dev/null | awk '{print $1}')
    echo -e "   - lmrex/: ${LMREX_SIZE}"
fi

echo ""
echo "================================"
echo -e "${GREEN}✓ Cleanup Complete!${NC}"
echo -e "   Total items cleaned: ${YELLOW}${CLEANED_COUNT}${NC}"
echo ""
echo -e "${BLUE}Optional: Deep Clean${NC}"
echo "To perform a deep clean (rebuild frontend), run:"
echo -e "  ${YELLOW}rm -rf .web .states && reflex init${NC}"
echo ""
echo -e "${BLUE}Optional: Update Git${NC}"
echo "If you made changes to tracked files, commit them:"
echo -e "  ${YELLOW}git add .gitignore${NC}"
echo -e "  ${YELLOW}git commit -m \"chore: cleanup build artifacts and update .gitignore\"${NC}"
echo ""
echo -e "${GREEN}🎉 Your project is now clean and optimized!${NC}"