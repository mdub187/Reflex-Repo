#!/bin/bash
# Simple startup without extras

echo "Starting Reflex (Simple Mode - skipping Tailwind plugins)..."

# Kill existing
lsof -ti:3000,8000 | xargs kill -9 2>/dev/null
pkill -9 -f "reflex run" 2>/dev/null
pkill -9 bun 2>/dev/null

sleep 2

# Start with basic frontend only
cd .web 2>/dev/null || { echo "No .web dir"; exit 1; }
npm install --legacy-peer-deps --prefer-offline > /dev/null 2>&1 &
NPM_PID=$!

echo "Installing base packages (PID: $NPM_PID)..."
wait $NPM_PID

cd ..
echo "Packages installed"
echo "Starting Reflex..."

# Start reflex
reflex run
