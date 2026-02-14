# Reflex WebSocket Connection Troubleshooting Guide

## Problem: WebSocket Connection Failures

When you see errors like:
```
Firefox can't establish a connection to the server at ws://localhost:8000/_event/
```
This means the frontend cannot connect to the backend WebSocket server.

---

## Quick Fix Checklist

### 1. **Stop All Existing Processes**
```bash
# Kill processes on ports 3000 and 8000
lsof -ti:3000,8000 | xargs kill -9 2>/dev/null
```

### 2. **Clean Rebuild**
```bash
# Remove build artifacts
rm -rf .web .states

# Reinitialize
reflex init
```

### 3. **Start Fresh**
```bash
# Use the startup script
./start_reflex.sh

# OR manually
reflex run --loglevel info
```

---

## Common Issues & Solutions

### Issue 1: Backend Not Running
**Symptoms:**
- WebSocket connection errors
- Cannot reach `http://localhost:8000`

**Solution:**
```bash
# Check if backend is running
lsof -i :8000

# If nothing, start Reflex
reflex run
```

### Issue 2: Port Conflicts
**Symptoms:**
- "Address already in use" errors
- Random port assignments

**Solution:**
```bash
# Kill processes on occupied ports
lsof -ti:8000 | xargs kill -9
lsof -ti:3000 | xargs kill -9

# Restart Reflex
reflex run
```

### Issue 3: Corrupted Build Cache
**Symptoms:**
- WebSocket connects but immediately disconnects
- Stale frontend code

**Solution:**
```bash
# Complete clean rebuild
rm -rf .web .states __pycache__
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null
reflex init
reflex run
```

### Issue 4: CORS Configuration
**Symptoms:**
- WebSocket connection blocked by browser
- CORS policy errors in console

**Solution:**
Check `rxconfig.py` has correct CORS settings:
```python
config = rx.Config(
    app_name="lmrex",
    backend_port=8000,
    frontend_port=3000,
    api_url="http://localhost:8000",
    deploy_url="http://localhost:3000",
    backend_host="0.0.0.0",
    cors_allowed_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
)
```

### Issue 5: Version Mismatch
**Symptoms:**
- Incompatibility errors
- Unexpected behavior

**Solution:**
```bash
# Update Reflex to latest version
pip install --upgrade reflex

# Update requirements
pip freeze > requirements.txt

# Clean rebuild
rm -rf .web .states
reflex init
```

### Issue 6: Bun Installation Timeout/Failures
**Symptoms:**
```
Warning: There was an error running command: ['.../bun', 'install', '--legacy-peer-deps']. 
Falling back to: ['.../npm', 'install', '--legacy-peer-deps'].
```
- Bun hangs during `Resolving dependencies`
- Process times out after several minutes
- Multiple fallback warnings during startup

**Solution:**
Pre-install packages with npm before starting Reflex:
```bash
cd .web
npm install --legacy-peer-deps

# Install required packages
npm add --legacy-peer-deps -D @tailwindcss/postcss@4.1.18 @tailwindcss/typography@0.5.19 tailwindcss@4.1.18
npm add --legacy-peer-deps sonner@2.0.7 @radix-ui/react-form@0.1.8 react-error-boundary@6.0.3 react-debounce-input@3.3.0 lucide-react@0.562.0 @radix-ui/themes@3.2.1

cd ..
reflex run
```

**Or use the updated startup script:**
```bash
./start_reflex.sh  # Now includes automatic npm pre-install
```

### Issue 7: Python 3.14 Pydantic Warning
**Symptoms:**
```
UserWarning: Core Pydantic V1 functionality isn't compatible with Python 3.14
```

**Solution:**
This is a warning, not an error. Reflex 0.8.26+ handles this internally. You can:
- Ignore it (it won't affect functionality)
- OR downgrade to Python 3.13 if you prefer

```bash
# Check Python version
python --version

# If using pyenv, switch versions
pyenv install 3.13.0
pyenv local 3.13.0
```

---

## Advanced Debugging

### Check Server Logs
```bash
# Run with debug logging
reflex run --loglevel debug

# Check for:
# - "Backend running on: http://0.0.0.0:8000"
# - "Frontend running on: http://localhost:3000"
```

### Verify Network Connectivity
```bash
# Test backend endpoint
curl http://localhost:8000/ping

# Check WebSocket endpoint (should return upgrade error, which is OK)
curl -i http://localhost:8000/_event/
```

### Check Browser Console
1. Open DevTools (F12)
2. Go to Console tab
3. Look for WebSocket connection errors
4. Check Network tab → WS filter → See connection attempts

### Verify State Manager
The app uses disk-based state management. Check:
```bash
# Ensure .states directory exists and is writable
ls -la .states/
```

---

## Environment-Specific Issues

### Docker/Container Issues
If running in Docker:
```yaml
# docker-compose.yml
services:
  reflex:
    ports:
      - "3000:3000"
      - "8000:8000"
    environment:
      - BACKEND_HOST=0.0.0.0
```

### Virtual Environment Issues
```bash
# Ensure venv is activated
source .venv/bin/activate  # Unix
# OR
.venv\Scripts\activate     # Windows

# Verify Reflex installation
which reflex
reflex --version
```

### Firewall/Security Software
Check if firewall is blocking:
- Port 3000 (Frontend)
- Port 8000 (Backend)
- WebSocket connections

---

## Still Having Issues?

### 1. Complete Reset
```bash
# Nuclear option - complete fresh start
rm -rf .web .states __pycache__
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null
rm -rf .venv

# Recreate environment
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Start fresh
reflex init
reflex run
```

### 2. Check System Resources
```bash
# Ensure you have enough memory and disk space
df -h .
free -h  # Linux
vm_stat  # macOS
```

### 3. Verify Dependencies
```bash
# Check all dependencies are installed
pip check

# Reinstall if needed
pip install --force-reinstall reflex
```

---

## Useful Commands Reference

```bash
# Start app with startup script
./start_reflex.sh

# Start app manually
reflex run

# Start with debug logging
reflex run --loglevel debug

# Initialize/reinitialize
reflex init

# Export frontend only
reflex export

# Check Reflex version
reflex --version

# List all processes on common ports
lsof -i :3000,8000

# Kill specific process
kill -9 <PID>

# Check Python version
python --version

# Check installed packages
pip list | grep reflex
```

---

## Configuration File Reference

**rxconfig.py** - Main configuration:
```python
import reflex as rx

config = rx.Config(
    app_name="lmrex",
    backend_port=8000,           # Backend server port
    frontend_port=3000,          # Frontend dev server port
    api_url="http://localhost:8000",  # Backend API URL
    deploy_url="http://localhost:3000",  # Frontend URL
    backend_host="0.0.0.0",      # Listen on all interfaces
    cors_allowed_origins=[       # CORS whitelist
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ],
    db_url="sqlite:///reflex.db",  # Database URL
    stylesheets=[...],           # CSS files
    plugins=[...],               # Reflex plugins
)
```

---

## Getting Help

1. **Reflex Discord**: https://discord.gg/reflex-dev
2. **GitHub Issues**: https://github.com/reflex-dev/reflex/issues
3. **Documentation**: https://reflex.dev/docs/getting-started/introduction/

---

## Prevention Tips

1. **Always use the startup script** - Ensures clean starts
2. **Keep Reflex updated** - `pip install --upgrade reflex`
3. **Use version control** - Commit working states
4. **Clean rebuilds regularly** - `rm -rf .web .states` before major changes
5. **Monitor logs** - Use `--loglevel debug` when developing

---
