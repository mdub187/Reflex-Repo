# 🔌 Dynamic Port Configuration Guide

Complete guide for using dynamic port selection in your Reflex application.

---

## 📋 Overview

Your Reflex app now supports **automatic dynamic port selection**. If a port is already in use, the system will automatically find the next available port.

### Features

- ✅ Automatic port detection in `rxconfig.py`
- ✅ Manual port specification via command line
- ✅ Environment variable support
- ✅ Fallback to next available port
- ✅ CORS automatically configured for dynamic ports

---

## 🚀 Quick Start

### Method 1: Automatic Port Selection (Default)

Simply start the app - it will find available ports automatically:

```bash
./start_reflex.sh
```

**What happens:**
- Checks if port 8000 is available for backend
- If not, tries 8001, 8002, etc. (up to 10 ports)
- Same for frontend starting at 3000
- Prints which ports are being used

**Example output:**
```
✅ Using backend port: 8000
✅ Using frontend port: 3000
```

Or if ports are in use:
```
⚠️  Port 3000 is in use. Finding alternative...
✅ Using frontend port: 3001
```

---

### Method 2: Specify Custom Ports

Use command line arguments:

```bash
# Use specific ports
./start_reflex.sh --backend-port 8080 --frontend-port 3001

# Short form
./start_reflex.sh -b 8080 -f 3001
```

---

### Method 3: Environment Variables

Set ports via environment variables:

```bash
# One-time use
BACKEND_PORT=9000 FRONTEND_PORT=4000 ./start_reflex.sh

# Or export for session
export BACKEND_PORT=9000
export FRONTEND_PORT=4000
./start_reflex.sh
```

---

## 🛠️ How It Works

### In `rxconfig.py`

The configuration file now includes a `find_available_port()` function:

```python
def find_available_port(start_port: int, max_attempts: int = 10) -> int:
    """
    Find an available port starting from start_port.
    Tries up to max_attempts consecutive ports.
    """
    for port in range(start_port, start_port + max_attempts):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(("", port))
                return port
        except OSError:
            continue
    raise RuntimeError("No available port found")
```

**Process:**
1. Import `socket` module
2. Try to bind to a port
3. If successful → port is available, return it
4. If fails (OSError) → port in use, try next one
5. Repeat up to 10 times
6. If all fail → raise error (fallback to defaults)

### In `start_reflex.sh`

The startup script includes:
- Port availability checking
- Automatic port increment
- Process cleanup
- Clear status messages

---

## 📊 Configuration Examples

### Example 1: Default Configuration

```python
# rxconfig.py - Automatic port detection
backend_port = find_available_port(8000)   # Tries 8000-8009
frontend_port = find_available_port(3000)  # Tries 3000-3009

config = rx.Config(
    backend_port=backend_port,
    frontend_port=frontend_port,
    api_url=f"http://localhost:{backend_port}",
    deploy_url=f"http://localhost:{frontend_port}",
)
```

### Example 2: Custom Starting Ports

```python
# Start checking from different ports
backend_port = find_available_port(9000)   # Tries 9000-9009
frontend_port = find_available_port(4000)  # Tries 4000-4009
```

### Example 3: More Attempts

```python
# Try more ports before giving up
backend_port = find_available_port(8000, max_attempts=50)
```

### Example 4: Environment Variable Override

```python
import os

# Use env var if set, otherwise auto-detect
backend_port = int(os.getenv('BACKEND_PORT', 
    find_available_port(8000)))
```

---

## 🎯 Use Cases

### Development with Multiple Apps

Running multiple Reflex apps simultaneously:

```bash
# Terminal 1 - App 1
cd project1
./start_reflex.sh
# Uses: Backend 8000, Frontend 3000

# Terminal 2 - App 2
cd project2
./start_reflex.sh
# Automatically uses: Backend 8001, Frontend 3001
```

### CI/CD Pipelines

Avoid port conflicts in automated testing:

```bash
# In your CI script
export BACKEND_PORT=$(shuf -i 8000-9000 -n 1)
export FRONTEND_PORT=$(shuf -i 3000-4000 -n 1)
./start_reflex.sh
```

### Docker Compose

Map to dynamic ports:

```yaml
services:
  reflex:
    build: .
    environment:
      - BACKEND_PORT=8080
      - FRONTEND_PORT=3001
    ports:
      - "8080:8080"
      - "3001:3001"
```

### Team Environments

Each team member can run on different ports:

```bash
# Developer 1
BACKEND_PORT=8000 ./start_reflex.sh

# Developer 2
BACKEND_PORT=8100 ./start_reflex.sh

# Developer 3
BACKEND_PORT=8200 ./start_reflex.sh
```

---

## 🔧 Advanced Configuration

### Custom Port Ranges

Edit `rxconfig.py` to define custom port ranges:

```python
# Only use ports in specific range
def find_available_port_in_range(start: int, end: int) -> int:
    """Find available port within specific range"""
    for port in range(start, end + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(("", port))
                return port
        except OSError:
            continue
    raise RuntimeError(f"No available port in range {start}-{end}")

# Use only ports 8080-8090
backend_port = find_available_port_in_range(8080, 8090)
```

### Port from File

Read ports from a configuration file:

```python
import json
from pathlib import Path

# Read from ports.json
ports_file = Path("ports.json")
if ports_file.exists():
    with open(ports_file) as f:
        ports = json.load(f)
        backend_port = ports.get("backend", find_available_port(8000))
        frontend_port = ports.get("frontend", find_available_port(3000))
else:
    backend_port = find_available_port(8000)
    frontend_port = find_available_port(3000)
```

### Save Used Ports

Write ports to file for other processes to read:

```python
# Save ports after finding them
backend_port = find_available_port(8000)
frontend_port = find_available_port(3000)

with open(".ports.json", "w") as f:
    json.dump({
        "backend": backend_port,
        "frontend": frontend_port
    }, f)
```

---

## 🐛 Troubleshooting

### Issue: "Could not find available port"

**Symptom:**
```
RuntimeError: Could not find available port in range 8000-8009
```

**Solutions:**

1. **Increase max_attempts:**
   ```python
   backend_port = find_available_port(8000, max_attempts=50)
   ```

2. **Try different starting port:**
   ```bash
   ./start_reflex.sh -b 9000 -f 4000
   ```

3. **Check what's using ports:**
   ```bash
   lsof -i :8000-8010
   ```

4. **Kill processes using ports:**
   ```bash
   lsof -ti:8000 | xargs kill -9
   ```

---

### Issue: CORS errors after port change

**Symptom:**
```
Access to fetch at 'http://localhost:8001' from origin 'http://localhost:3002' 
has been blocked by CORS policy
```

**Solution:**

The `rxconfig.py` now automatically includes dynamic ports in CORS:

```python
cors_allowed_origins=[
    f"http://localhost:{frontend_port}",  # Dynamic
    f"http://127.0.0.1:{frontend_port}",  # Dynamic
    "http://localhost:3000",              # Default fallback
    "http://127.0.0.1:3000",              # Default fallback
]
```

If still having issues, add your specific ports:

```python
cors_allowed_origins=[
    "http://localhost:*",  # Allow all localhost ports (less secure)
    # Or be specific:
    "http://localhost:3001",
    "http://localhost:3002",
]
```

---

### Issue: Port already in use after restart

**Symptom:**
```
Warning: Unable to bind to :3000 due to: [Errno 48] Address already in use.
```

**Solution:**

The startup script should handle this, but you can manually:

```bash
# Kill all reflex processes
pkill -9 reflex

# Kill processes on specific ports
lsof -ti:3000,8000 | xargs kill -9

# Restart
./start_reflex.sh
```

---

### Issue: Environment variables not working

**Symptom:**
Ports don't change when using `BACKEND_PORT=9000`

**Solution:**

Make sure you're exporting the variable:

```bash
# Wrong (only sets for that command)
BACKEND_PORT=9000
./start_reflex.sh

# Correct (export for session)
export BACKEND_PORT=9000
./start_reflex.sh

# Or inline
BACKEND_PORT=9000 ./start_reflex.sh
```

---

## 📝 Command Reference

### Startup Script Options

```bash
./start_reflex.sh [options]

Options:
  -b, --backend-port PORT    Set backend port (default: 8000)
  -f, --frontend-port PORT   Set frontend port (default: 3000)
  --clean                    Clean rebuild (.web directory)
  -h, --help                 Show help message

Examples:
  ./start_reflex.sh                    # Auto-detect ports
  ./start_reflex.sh -b 8080           # Custom backend
  ./start_reflex.sh -f 3001           # Custom frontend
  ./start_reflex.sh -b 8080 -f 3001   # Both custom
  ./start_reflex.sh --clean           # Clean rebuild
```

### Check Port Usage

```bash
# List all processes using ports 8000-8010
lsof -i :8000-8010

# Check specific port
lsof -i :8000

# Kill process on port
lsof -ti:8000 | xargs kill -9

# Find available port (manual)
python3 -c "import socket; s=socket.socket(); s.bind(('', 0)); print(s.getsockname()[1]); s.close()"
```

### Environment Variables

```bash
# Set for current session
export BACKEND_PORT=9000
export FRONTEND_PORT=4000

# Check current values
echo $BACKEND_PORT
echo $FRONTEND_PORT

# Unset
unset BACKEND_PORT
unset FRONTEND_PORT

# Set in .bashrc or .zshrc for permanent
echo 'export BACKEND_PORT=9000' >> ~/.bashrc
```

---

## 🔒 Security Considerations

### Development

- ✅ Dynamic ports are fine for local development
- ✅ Automatic detection prevents conflicts
- ✅ CORS is configured for detected ports

### Production

- ⚠️ Use fixed ports in production
- ⚠️ Configure firewall rules for specific ports
- ⚠️ Set explicit CORS origins (no wildcards)
- ⚠️ Use environment variables, not auto-detection

**Production `rxconfig.py`:**

```python
import os

config = rx.Config(
    backend_port=int(os.getenv('BACKEND_PORT', 8000)),
    frontend_port=int(os.getenv('FRONTEND_PORT', 3000)),
    # Explicit CORS for production
    cors_allowed_origins=[
        os.getenv('FRONTEND_URL', 'https://yourdomain.com'),
    ],
)
```

---

## 💡 Best Practices

### 1. Use Defaults for Solo Development
```bash
# Just start it
./start_reflex.sh
```

### 2. Use Custom Ports for Team Development
```bash
# Each developer has their range
# Developer 1: 8000-8009
# Developer 2: 8100-8109
# Developer 3: 8200-8209
./start_reflex.sh -b 8100 -f 3100
```

### 3. Use Environment Variables for CI/CD
```bash
# In your CI pipeline
export BACKEND_PORT=8080
export FRONTEND_PORT=3080
./start_reflex.sh
```

### 4. Document Your Port Assignments
Create a `PORTS.md` in your team repo:
```markdown
# Port Assignments

- Dev Server: 8000/3000
- Staging: 8080/3080  
- Production: 80/443
- Team Member 1: 8100/3100
- Team Member 2: 8200/3200
```

### 5. Use Port Files for Multi-Process Apps
```python
# App 1 saves its ports
with open(".app1_ports.json", "w") as f:
    json.dump({"backend": 8000, "frontend": 3000}, f)

# App 2 reads and avoids them
with open(".app1_ports.json") as f:
    used = json.load(f)
    backend_port = find_available_port(used["backend"] + 1)
```

---

## 📚 Additional Resources

### Related Files
- `rxconfig.py` - Port configuration logic
- `start_reflex.sh` - Startup script with port detection
- `TROUBLESHOOTING.md` - General troubleshooting guide

### Useful Commands
```bash
# See all listening ports
lsof -iTCP -sTCP:LISTEN -P -n

# Test if port is open
nc -zv localhost 8000

# Get random available port
python3 -c "import socket; s=socket.socket(); s.bind(('', 0)); print(s.getsockname()[1])"
```

---

## ✅ Summary

Your Reflex app now has intelligent port management:

- **Automatic**: Finds available ports automatically
- **Flexible**: Override via CLI, env vars, or config
- **Robust**: Handles port conflicts gracefully
- **Team-Friendly**: Multiple apps can run simultaneously

**For most cases, just use:**
```bash
./start_reflex.sh
```

The system will handle the rest!

---

**Created**: 2025-02-12  
**Last Updated**: 2025-02-12  
**Reflex Version**: 0.8.26