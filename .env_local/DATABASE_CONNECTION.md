# Database Connection Information

## Current Setup
- **Database Type**: PostgreSQL
- **Database Name**: `reflex_dev`
- **Host**: `localhost`
- **Port**: `5432`
- **Username**: `mdub`
- **Password**: (No password required for local connections)

## pgAdmin Connection Settings

### How to Connect in pgAdmin:

1. **Open pgAdmin** and right-click on "Servers" → "Register" → "Server"

2. **General Tab:**
   - **Name**: `Reflex Local Dev`

3. **Connection Tab:**
   - **Host name/address**: `localhost`
   - **Port**: `5432`
   - **Maintenance database**: `reflex_dev`
   - **Username**: `mdub`
   - **Password**: (leave blank or check "Save password")

4. **SSL Tab:**
   - **SSL mode**: `Prefer` (or `Disable` for local)

5. Click **Save**

### Troubleshooting pgAdmin Connection

If pgAdmin can't connect:

```bash
# 1. Check PostgreSQL is running
pg_isready -h localhost -p 5432

# 2. Test connection from command line
psql -h localhost -U mdub -d reflex_dev

# 3. Check pg_hba.conf allows local connections
# Location: /opt/homebrew/var/postgresql@14/pg_hba.conf
# Should have: host    all    all    127.0.0.1/32    trust
```

## Other Database GUI Apps

### DBeaver Connection:
- **Driver**: PostgreSQL
- **Host**: `localhost`
- **Port**: `5432`
- **Database**: `reflex_dev`
- **Username**: `mdub`
- **Authentication**: Database Native

### TablePlus Connection:
- **Connection Type**: PostgreSQL
- **Host**: `localhost`
- **Port**: `5432`
- **Database**: `reflex_dev`
- **User**: `mdub`

### Postico Connection:
- **Host**: `localhost`
- **Port**: `5432`
- **Database**: `reflex_dev`
- **User**: `mdub`

## Environment Variable Setup

To use PostgreSQL with your Reflex app:

### Option 1: Set for current terminal session
```bash
export DATABASE_URL="postgresql://mdub@localhost:5432/reflex_dev"
```

### Option 2: Add to .env file
Create a file `.env` in your project root:
```
DATABASE_URL=postgresql://mdub@localhost:5432/reflex_dev
```

### Option 3: Add to shell profile (permanent)
```bash
# Add to ~/.zshrc or ~/.bashrc
echo 'export DATABASE_URL="postgresql://mdub@localhost:5432/reflex_dev"' >> ~/.zshrc
source ~/.zshrc
```

## Initialize Database Tables

After setting DATABASE_URL, run:

```bash
# Activate virtual environment
source .venv/bin/activate

# Initialize database
reflex db init

# Or use the custom init script
python init_db.py
```

## Verify Connection

```bash
# Test from Python
python -c "from rxconfig import config; print(config.db_url)"

# Test from command line
psql -h localhost -U mdub -d reflex_dev -c "SELECT version();"
```

## Common Issues

### Issue: "password authentication failed"
**Solution**: Check your pg_hba.conf file and ensure it allows connections from localhost

### Issue: "database does not exist"
**Solution**: 
```bash
psql -h localhost -U mdub -d postgres -c "CREATE DATABASE reflex_dev;"
```

### Issue: "could not connect to server"
**Solution**: Start PostgreSQL
```bash
brew services start postgresql@14
```

### Issue: "peer authentication failed"
**Solution**: Use `-h localhost` to force TCP/IP connection instead of Unix socket

## Connection String Format

```
postgresql://[username]:[password]@[host]:[port]/[database]
```

Examples:
```
# No password (local trusted connection)
postgresql://mdub@localhost:5432/reflex_dev

# With password
postgresql://mdub:mypassword@localhost:5432/reflex_dev

# Production (Render, Railway, etc)
postgresql://user:password@host.region.provider.com:5432/database
```

## Quick Commands

```bash
# List all databases
psql -h localhost -U mdub -d postgres -c "\l"

# List all tables in reflex_dev
psql -h localhost -U mdub -d reflex_dev -c "\dt"

# Connect to database
psql -h localhost -U mdub -d reflex_dev

# Drop and recreate database (CAREFUL!)
psql -h localhost -U mdub -d postgres -c "DROP DATABASE IF EXISTS reflex_dev;"
psql -h localhost -U mdub -d postgres -c "CREATE DATABASE reflex_dev;"
```
