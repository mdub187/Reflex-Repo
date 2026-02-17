# Dynamic Ports - Quick Reference

## What's Working

Your Reflex app now automatically finds available ports!

---

## Usage

### Default (Automatic)
```bash
./start_reflex.sh
```
Automatically finds next available port if 8000/3000 are in use

### Custom Ports
```bash
./start_reflex.sh -b 8080 -f 3001
```

### Environment Variables
```bash
BACKEND_PORT=9000 FRONTEND_PORT=4000 ./start_reflex.sh
```

---

## How It Works

**In `rxconfig.py`:**
- Tries to bind to port 8000
- If in use, tries 8001, 8002, etc.
- Same for frontend (3000 → 3001 → 3002...)
- Up to 10 attempts

**Example output:**
```
Using backend port: 8001
Using frontend port: 3001
```

---

## Quick Examples

### Run Multiple Apps Simultaneously
```bash
# Terminal 1 - First app
cd project1
./start_reflex.sh
# Uses: 8000, 3000

# Terminal 2 - Second app
cd project2  
./start_reflex.sh
# Uses: 8001, 3001 (automatically!)
```

### Force Specific Ports
```bash
./start_reflex.sh -b 8080 -f 3080
```

### Clean Rebuild
```bash
./start_reflex.sh --clean
```

---

## Configuration

### Change Starting Port

Edit `rxconfig.py`:
```python
backend_port = find_available_port(9000)   # Start from 9000
frontend_port = find_available_port(4000)  # Start from 4000
```

### Change Max Attempts

```python
backend_port = find_available_port(8000, max_attempts=50)
```

---

## Troubleshooting

### Port still in use?
```bash
# Kill processes on ports
lsof -ti:8000,3000 | xargs kill -9

# Or use the script's auto-detection
./start_reflex.sh  # Will find next available
```

### See what's using ports?
```bash
lsof -i :8000-8010
```

---

## Full Documentation

See `DYNAMIC_PORTS_GUIDE.md` for complete documentation.

---

**Created**: 2025-02-12  
**Status**: Working!
