# PostgreSQL Setup Guide

## Overview

This Reflex application **requires PostgreSQL** for authentication and data storage. This guide covers setting up PostgreSQL for both local development and production deployment.

## Why PostgreSQL?

- Production-ready relational database
- Required by reflex-local-auth for user authentication
- Handles concurrent connections efficiently
- Supported by all major cloud platforms

## Quick Start

### For Production (Already using PostgreSQL)

```bash
# Set your DATABASE_URL
export DATABASE_URL="postgresql://user:password@host:port/database"

# Create tables
python init_db.py

# Start app
reflex run
```

### For Local Development

You need PostgreSQL installed locally or use your production database.

## Local PostgreSQL Installation

### macOS (using Homebrew)

```bash
# Install PostgreSQL
brew install postgresql@14

# Start PostgreSQL service
brew services start postgresql@14

# Create database
createdb reflex_dev

# Create user
psql postgres -c "CREATE USER reflex_user WITH PASSWORD 'your_password';"
psql postgres -c "GRANT ALL PRIVILEGES ON DATABASE reflex_dev TO reflex_user;"

# Set DATABASE_URL
export DATABASE_URL="postgresql://reflex_user:your_password@localhost:5432/reflex_dev"
```

### Linux (Ubuntu/Debian)

```bash
# Install PostgreSQL
sudo apt update
sudo apt install postgresql postgresql-contrib

# Start PostgreSQL service
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Create database and user
sudo -u postgres psql -c "CREATE DATABASE reflex_dev;"
sudo -u postgres psql -c "CREATE USER reflex_user WITH PASSWORD 'your_password';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE reflex_dev TO reflex_user;"

# Set DATABASE_URL
export DATABASE_URL="postgresql://reflex_user:your_password@localhost:5432/reflex_dev"
```

### Windows

```bash
# Download and install PostgreSQL from:
# https://www.postgresql.org/download/windows/

# Using pgAdmin or psql, create database and user:
CREATE DATABASE reflex_dev;
CREATE USER reflex_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE reflex_dev TO reflex_user;

# Set DATABASE_URL (in PowerShell)
$env:DATABASE_URL="postgresql://reflex_user:your_password@localhost:5432/reflex_dev"
```

### Docker (Quick Local Setup)

```bash
# Run PostgreSQL in Docker
docker run --name reflex-postgres \
  -e POSTGRES_USER=reflex_user \
  -e POSTGRES_PASSWORD=your_password \
  -e POSTGRES_DB=reflex_dev \
  -p 5432:5432 \
  -d postgres:14

# Set DATABASE_URL
export DATABASE_URL="postgresql://reflex_user:your_password@localhost:5432/reflex_dev"
```

## Initialize Database Tables

After setting up PostgreSQL, create the required tables:

```bash
# Method 1: Using init_db.py (recommended)
python init_db.py

# Method 2: Using setup_postgres.py (with detailed output)
python setup_postgres.py

# Method 3: Using direct Python
python -c "
from sqlalchemy import create_engine
import sqlmodel
from reflex_local_auth.local_auth import LocalUser, LocalAuthSession
import os

engine = create_engine(os.getenv('DATABASE_URL'))
sqlmodel.SQLModel.metadata.create_all(engine)
print('Tables created')
"
```

## Production Deployment

### Render

1. Create a PostgreSQL database:
   - Go to Dashboard > New > PostgreSQL
   - Note the connection details

2. Link to your web service:
   - Render automatically provides `DATABASE_URL`
   - No manual configuration needed

3. Build command:
   ```bash
   pip install -r requirements.txt && python init_db.py
   ```

### Railway

1. Add PostgreSQL plugin:
   - Click "+ New" > Database > Add PostgreSQL

2. Set environment variable:
   ```
   DATABASE_URL=${{Postgres.DATABASE_URL}}
   ```

3. Build command:
   ```bash
   pip install -r requirements.txt && python init_db.py
   ```

### Fly.io

1. Create PostgreSQL app:
   ```bash
   fly postgres create
   ```

2. Attach to your app:
   ```bash
   fly postgres attach <postgres-app-name>
   ```

3. Deploy:
   ```bash
   fly deploy
   ```

### Generic Hosting

1. Provision PostgreSQL database
2. Get connection string in format:
   ```
   postgresql://username:password@host:port/database
   ```
3. Set as environment variable:
   ```bash
   export DATABASE_URL="postgresql://username:password@host:port/database"
   ```
4. Run initialization:
   ```bash
   python init_db.py
   ```

## Database Connection String Format

```
postgresql://[user[:password]@][host][:port][/database]
```

Example:
```
postgresql://myuser:mypass@localhost:5432/mydb
```

With SSL (common for cloud databases):
```
postgresql://myuser:mypass@host.com:5432/mydb?sslmode=require
```

## Verifying Connection

### Test Connection

```bash
# Using Python
python -c "
import psycopg2
import os
conn = psycopg2.connect(os.getenv('DATABASE_URL'))
print('Connection successful!')
conn.close()
"
```

### Check Tables

```bash
# Using psql
psql $DATABASE_URL -c "\dt"

# Expected output:
#               List of relations
#  Schema |       Name        | Type  |    Owner    
# --------+-------------------+-------+-------------
#  public | localauthsession  | table | reflex_user
#  public | localuser         | table | reflex_user
```

### View Table Structure

```bash
# Using psql
psql $DATABASE_URL -c "\d localuser"
psql $DATABASE_URL -c "\d localauthsession"
```

## Required Tables

The application needs these tables for authentication:

### localuser

| Column        | Type         | Description              |
|---------------|--------------|--------------------------|
| id            | INTEGER      | Primary key              |
| username      | VARCHAR(255) | Unique username          |
| password_hash | BYTEA        | Hashed password          |
| enabled       | BOOLEAN      | Account enabled flag     |

### localauthsession

| Column      | Type         | Description              |
|-------------|--------------|--------------------------|
| id          | INTEGER      | Primary key              |
| user_id     | INTEGER      | Foreign key to localuser |
| session_id  | VARCHAR(255) | Unique session ID        |
| expiration  | TIMESTAMP    | Session expiration time  |

## Troubleshooting

### Connection Refused

**Problem:** Can't connect to PostgreSQL

**Solutions:**
- Check PostgreSQL is running: `pg_isready`
- Verify port is correct (default: 5432)
- Check firewall settings
- For cloud databases, verify IP whitelist

### Authentication Failed

**Problem:** Password incorrect or user doesn't exist

**Solutions:**
- Verify username and password in DATABASE_URL
- Check user exists: `psql -c "\du"`
- Reset password if needed:
  ```sql
  ALTER USER reflex_user WITH PASSWORD 'new_password';
  ```

### Database Does Not Exist

**Problem:** Database not found

**Solutions:**
- Create database: `createdb reflex_dev`
- Or via SQL: `CREATE DATABASE reflex_dev;`
- Verify database name in DATABASE_URL

### Tables Not Created

**Problem:** init_db.py runs but tables missing

**Solutions:**
- Check database permissions:
  ```sql
  GRANT ALL PRIVILEGES ON DATABASE reflex_dev TO reflex_user;
  ```
- Run setup_postgres.py for detailed output
- Check for errors in output

### SSL/TLS Issues

**Problem:** SSL connection errors

**Solutions:**
- Add `?sslmode=require` to DATABASE_URL for cloud databases
- Or disable SSL for local dev: `?sslmode=disable`

## Environment Variables

Set these in your environment:

```bash
# Required
export DATABASE_URL="postgresql://user:pass@host:port/database"

# Optional
export PRODUCTION=true           # For production mode
export BACKEND_PORT=8000         # Backend port
export FRONTEND_PORT=3000        # Frontend port
```

Make it persistent by adding to shell config:

```bash
# For bash
echo 'export DATABASE_URL="postgresql://..."' >> ~/.bashrc

# For zsh
echo 'export DATABASE_URL="postgresql://..."' >> ~/.zshrc
```

## Security Best Practices

1. **Never commit DATABASE_URL** to version control
2. **Use strong passwords** for database users
3. **Restrict database access** to necessary IPs only
4. **Use SSL/TLS** for production connections
5. **Regular backups** - enable automated backups on your platform
6. **Separate databases** for dev/staging/production

## Database Backups

### Manual Backup

```bash
# Backup
pg_dump $DATABASE_URL > backup.sql

# Restore
psql $DATABASE_URL < backup.sql
```

### Platform-Specific

- **Render:** Automatic daily backups included
- **Railway:** Enable backups in database settings
- **Fly.io:** Use `fly postgres backup` commands

## Migration Guide

If you need to migrate from SQLite to PostgreSQL:

```bash
# 1. Export SQLite data (if applicable)
sqlite3 reflex.db .dump > sqlite_dump.sql

# 2. Set up PostgreSQL
export DATABASE_URL="postgresql://..."

# 3. Create tables
python init_db.py

# 4. Migrate data (manual process, structure may differ)
# Review and adapt sqlite_dump.sql for PostgreSQL syntax
```

## Support

- **Quick issues:** See QUICK_START.md
- **Deployment:** See DEPLOYMENT.md
- **General setup:** See README.md

## Additional Resources

- PostgreSQL Official Docs: https://www.postgresql.org/docs/
- psycopg2 Documentation: https://www.psycopg.org/docs/
- SQLAlchemy with PostgreSQL: https://docs.sqlalchemy.org/en/14/dialects/postgresql.html

---

Last Updated: February 2026