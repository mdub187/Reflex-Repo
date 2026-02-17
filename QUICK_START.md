# Quick Start Guide - Fix Database Error

## Seeing "no such table: localuser" Error?

This quick guide will get you up and running in 2 minutes.

**IMPORTANT: This application requires PostgreSQL, not SQLite.**

## Step 1: Initialize the Database

Run this ONE command:

```bash
python init_db.py
```

That's it! This creates all required database tables.

## Step 2: Start the Application

```bash
reflex run
```

Or use the enhanced startup script:

```bash
./shell/start_reflex.sh
```

## What Was Fixed?

We've implemented multiple fixes for the database initialization issue:

1. **`init_db.py`** - Automated database setup script for PostgreSQL
2. **`auth_state.py`** - Added error handling for missing tables (catches both SQLite and PostgreSQL errors)
3. **`deploy_start.sh`** - Production deployment script with built-in initialization
4. **`rxconfig.py`** - PostgreSQL configuration with proper connection handling

## PostgreSQL Setup

**This app requires PostgreSQL.** Set up your database:

1. **For Render:** Add a PostgreSQL database service
2. **For Railway:** Add PostgreSQL plugin
3. **For Fly.io:** Run `fly postgres create`
4. **For Local:** Install PostgreSQL locally or use a cloud instance

## Deployment (Render/Railway/Fly.io)

### Build Command:
```bash
pip install -r requirements.txt && python init_db.py
```

### Start Command:
```bash
reflex run --env prod
```

### Environment Variables:
- `DATABASE_URL` - Your PostgreSQL connection string
- `PRODUCTION=true` - Enable production mode

## 🔧 Common Issues

### Issue: Script won't run
```bash
chmod +x init_db.py deploy_start.sh
```

### Issue: PostgreSQL connection fails locally
You need PostgreSQL running. Install it locally or use your production database URL:
```bash
export DATABASE_URL="postgresql://user:pass@host:port/dbname"
```

### Issue: Tables exist but still getting errors
```bash
rm -rf .states
reflex run
```

### Issue: Frontend won't load
```bash
rm -rf .web
reflex init
```

## 📚 Need More Details?

See `DEPLOYMENT.md` for:
- Complete deployment guide
- Platform-specific instructions
- Troubleshooting steps
- Database schema details

## How It Works

The database initialization happens in this order:

1. **Check** if tables exist
2. **Create** missing tables using `reflex db init`
3. **Verify** tables were created successfully
4. **Start** the application

The `auth_state.py` file now has try-catch blocks that gracefully handle cases where tables don't exist during app initialization, preventing crashes. It catches both `OperationalError` (SQLite) and `ProgrammingError` (PostgreSQL).

## For Developers

If you're modifying the database schema:

```bash
# Create migration
reflex db makemigrations -m "your change description"

# Apply migration
reflex db migrate

# Or use the init script (does both)
python init_db.py
```

## Why This Happened

The `reflex-local-auth` library requires database tables (`localuser` and `localauthsession`) for authentication. During app initialization, computed properties in `AuthState` try to query these tables. If they don't exist, the app crashes.

Our fix ensures tables are created **before** the app tries to use them, and adds graceful error handling as a safety net.

---

**Still having issues?** Check the logs and refer to `DEPLOYMENT.md` for detailed troubleshooting.
