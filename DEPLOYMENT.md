# Deployment Guide for Reflex Application

This guide covers deploying your Reflex application with proper database initialization to avoid the `no such table` error.

## Table of Contents
- [The Database Issue](#the-database-issue)
- [Quick Fix](#quick-fix)
- [Local Development](#local-development)
- [Production Deployment](#production-deployment)
- [Platform-Specific Instructions](#platform-specific-instructions)
- [Troubleshooting](#troubleshooting)

## The Database Issue

### Problem
The error `sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) no such table: localuser` occurs when the application tries to access database tables that haven't been created yet. This happens during app initialization when computed properties try to query the database.

### Root Cause
1. The `reflex-local-auth` library requires `localuser` and `localauthsession` tables
2. These tables must be created before the app starts
3. The app's `AuthState` computed properties (`user_email`, `is_logged_in`, etc.) access the database during initialization
4. If tables don't exist, the app crashes

### Solution Overview
We've implemented multiple layers of protection:
1. **Database initialization script** (`init_db.py`) - Creates tables before app startup
2. **Try-catch blocks** in `auth_state.py` - Gracefully handles missing tables during initialization
3. **Deployment script** (`deploy_start.sh`) - Ensures proper initialization order

## Quick Fix

If you're experiencing the database error right now:

### Option 1: Run the initialization script
```bash
python init_db.py
```

### Option 2: Use Reflex CLI
```bash
reflex db init
reflex db migrate
```

### Option 3: Use the deployment script
```bash
chmod +x deploy_start.sh
./deploy_start.sh
```

## Local Development

### Initial Setup

1. **Clone and navigate to the repository:**
   ```bash
   cd Reflex-Repo
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database:**
   ```bash
   python init_db.py
   ```
   
   This script will:
   - Check for existing tables
   - Create missing tables
   - Verify the setup
   - Provide detailed output

5. **Start the application:**
   ```bash
   # Using the enhanced startup script
   ./shell/start_reflex.sh
   
   # Or using Reflex directly
   reflex run
   ```

### Database Configuration

The application automatically detects your environment:

- **Local Development**: Uses SQLite (`sqlite:///reflex.db`) by default
- **Production**: Uses PostgreSQL from `DATABASE_URL` environment variable

You can override this by setting the `DATABASE_URL` environment variable:
```bash
export DATABASE_URL="postgresql://user:pass@host:port/dbname"
```

## Production Deployment

### Pre-Deployment Checklist

- [ ] Ensure `DATABASE_URL` environment variable is set
- [ ] Verify all dependencies are in `requirements.txt`
- [ ] Test database connection from production environment
- [ ] Set `PRODUCTION=true` environment variable
- [ ] Configure CORS origins for your domain

### Deployment Steps

#### Step 1: Build Commands

Add this to your platform's build command:
```bash
pip install -r requirements.txt && python init_db.py
```

Or use the full deployment script:
```bash
chmod +x deploy_start.sh && ./deploy_start.sh
```

#### Step 2: Start Command

Use one of these start commands:
```bash
# Option 1: Using deployment script (recommended)
./deploy_start.sh

# Option 2: Direct Reflex command
reflex run --env prod

# Option 3: With explicit initialization
python init_db.py && reflex run --env prod
```

#### Step 3: Environment Variables

Set these environment variables in your platform:

**Required:**
- `DATABASE_URL` - PostgreSQL connection string
- `PRODUCTION=true` - Enables production mode

**Optional:**
- `BACKEND_PORT=8000` - Backend port (default: 8000)
- `FRONTEND_PORT=3000` - Frontend port (default: 3000)
- `DEPLOY_URL` - Your app's public URL (auto-detected on Render/Railway/Fly.io)

### Database Migration

For database schema changes:

```bash
# Create a new migration
reflex db makemigrations -m "description of changes"

# Apply migrations
reflex db migrate

# Or use the init script which handles both
python init_db.py
```

## Platform-Specific Instructions

### Render

1. **Environment Variables:**
   ```
   DATABASE_URL=postgresql://...  (auto-provided by Render PostgreSQL)
   PRODUCTION=true
   RENDER=true
   ```

2. **Build Command:**
   ```bash
   pip install -r requirements.txt && python init_db.py
   ```

3. **Start Command:**
   ```bash
   reflex run --env prod
   ```

4. **Notes:**
   - Render automatically provides `RENDER_EXTERNAL_URL`
   - Database URL is auto-detected from Render PostgreSQL addon
   - CORS is automatically configured for Render domains

### Railway

1. **Environment Variables:**
   ```
   DATABASE_URL=${{Postgres.DATABASE_URL}}
   PRODUCTION=true
   ```

2. **Build Command:**
   ```bash
   pip install -r requirements.txt && python init_db.py
   ```

3. **Start Command:**
   ```bash
   reflex run --env prod
   ```

4. **Notes:**
   - Railway automatically provides `RAILWAY_PUBLIC_DOMAIN`
   - Use Railway's PostgreSQL plugin for managed database

### Fly.io

1. **Environment Variables:**
   ```
   DATABASE_URL=postgresql://...
   PRODUCTION=true
   ```

2. **Deploy:**
   ```bash
   fly deploy
   ```

3. **Run migrations:**
   ```bash
   fly ssh console
   python init_db.py
   ```

4. **Notes:**
   - Use Fly.io's PostgreSQL for database
   - App automatically detects `FLY_APP_NAME`

### Docker

Example `Dockerfile`:
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Initialize database and start app
RUN python init_db.py
CMD ["reflex", "run", "--env", "prod"]
```

## Troubleshooting

### Issue: "no such table: localuser"

**Symptoms:**
- Application crashes on startup
- Error mentions `localuser` or `localauthsession` tables

**Solutions:**
1. Run `python init_db.py` before starting the app
2. Check that `DATABASE_URL` is correctly set
3. Verify database connection with: `python -c "from rxconfig import config; print(config.db_url)"`
4. Manually run: `reflex db init && reflex db migrate`

### Issue: "Database is not initialized"

**Symptoms:**
- Warning message during startup
- Authentication features don't work

**Solutions:**
1. Run the initialization script: `python init_db.py`
2. Check database permissions
3. Verify the database URL is accessible from your environment

### Issue: Connection Refused / Database Not Found

**Symptoms:**
- Can't connect to PostgreSQL
- "role does not exist" errors

**Solutions:**
1. **For local development:** The app will fall back to SQLite automatically
2. **For production:** Verify `DATABASE_URL` is correct and database exists
3. Check database credentials and host accessibility
4. Ensure PostgreSQL service is running

### Issue: Tables Exist But Still Getting Errors

**Symptoms:**
- Tables are created but auth still fails
- Intermittent authentication issues

**Solutions:**
1. The updated `auth_state.py` includes try-catch blocks for resilience
2. Clear the `.states` directory: `rm -rf .states`
3. Restart the application
4. Check for migration conflicts: `reflex db heads`

### Issue: Frontend Not Loading

**Symptoms:**
- Backend works but frontend shows errors
- "Cannot find module" errors

**Solutions:**
1. Ensure Node.js is installed (version 16 or higher)
2. Delete `.web` directory and reinitialize: `rm -rf .web && reflex init`
3. Install frontend dependencies: `cd .web && npm install --legacy-peer-deps`

### Issue: Port Already in Use

**Symptoms:**
- "Address already in use" error
- Can't start on default ports

**Solutions:**
1. The app automatically finds available ports in development
2. Kill existing processes: `pkill -f "reflex run"`
3. Use custom ports: `BACKEND_PORT=8080 FRONTEND_PORT=3001 reflex run`
4. Use the enhanced startup script: `./shell/start_reflex.sh`

## Database Schema

### Tables Created

The application uses these tables from `reflex-local-auth`:

**localuser:**
- `id` (Integer, Primary Key)
- `username` (String, Unique)
- `password_hash` (Binary)
- `enabled` (Boolean)

**localauthsession:**
- `id` (Integer, Primary Key)
- `user_id` (Integer, Foreign Key)
- `session_id` (String, Unique)
- `expiration` (DateTime)

### Viewing Tables

```bash
# SQLite
sqlite3 reflex.db ".tables"
sqlite3 reflex.db ".schema localuser"

# PostgreSQL
psql $DATABASE_URL -c "\dt"
psql $DATABASE_URL -c "\d localuser"
```

## Best Practices

1. **Always initialize database before starting the app in production**
2. **Use environment variables for database configuration**
3. **Test database migrations in a staging environment first**
4. **Back up your database before running migrations**
5. **Use the provided scripts (`init_db.py`, `deploy_start.sh`) for consistent setup**
6. **Monitor database connection pool in production**
7. **Set up database backups on your platform**

## Files Reference

- **`init_db.py`** - Database initialization script
- **`deploy_start.sh`** - Complete deployment startup script
- **`shell/start_reflex.sh`** - Enhanced local development script
- **`lmrex/state/auth_state.py`** - Authentication state with error handling
- **`rxconfig.py`** - Application configuration
- **`alembic_migrations/`** - Database migration files

## Support

If you continue to experience issues:

1. Check the application logs for detailed error messages
2. Verify all environment variables are set correctly
3. Test database connectivity independently
4. Review the platform-specific documentation
5. Ensure you're using compatible versions of all dependencies

## Version Information

- Python: 3.11+
- Reflex: Latest version
- SQLAlchemy: 2.x
- PostgreSQL: 12+ (for production)
- SQLite: 3.x (for local development)

---

Last Updated: February 2026