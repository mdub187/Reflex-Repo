# pgAdmin Setup Guide for Reflex Database

## 📋 Connection Information

Use these exact settings to connect pgAdmin to your local Reflex database:

```
Host:     localhost
Port:     5432
Database: reflex_dev
Username: mdub
Password: (leave blank)
```

**Connection String:**
```
postgresql://mdub@localhost:5432/reflex_dev
```

---

## 🚀 Quick Setup (Step-by-Step)

### Step 1: Open pgAdmin

Launch pgAdmin 4 from your Applications folder or via Spotlight.

### Step 2: Register New Server

1. In the left sidebar, **right-click** on **"Servers"**
2. Select **"Register"** → **"Server..."**

### Step 3: General Tab

In the dialog that opens:

1. **Name:** `Reflex Local Dev` (or any name you prefer)
2. **Server Group:** Servers (default)
3. **Background Color:** (optional, for visual organization)
4. **Connect now?** ✓ (check this box)

Click to move to the **Connection** tab.

### Step 4: Connection Tab

Enter the following information **exactly**:

| Field | Value |
|-------|-------|
| **Host name/address** | `localhost` |
| **Port** | `5432` |
| **Maintenance database** | `reflex_dev` |
| **Username** | `mdub` |
| **Password** | (leave empty) |
| **Save password?** | ✓ (optional, for convenience) |

### Step 5: SSL Tab (Optional)

For local development:

- **SSL mode:** `Prefer` or `Disable`

(Local connections typically don't need SSL)

### Step 6: Advanced Tab (Optional)

You can usually leave these at defaults:

- **DB restriction:** (leave empty to see all databases)
- **Shared:** (unchecked)

### Step 7: Save

Click the **"Save"** button at the bottom right.

---

## ✅ Verify Connection

After saving, you should see:

1. **"Reflex Local Dev"** appear in the left sidebar under "Servers"
2. A **green checkmark** or connected icon next to it
3. Expand it to see:
   - Databases → reflex_dev → Schemas → public → Tables

### Expected Tables

You should see tables like:
- `localuser`
- `localauthsession`
- `admin`
- `contact`
- `usergallery`
- (other tables based on your models)

---

## 🔧 Troubleshooting

### Issue 1: "could not connect to server"

**Symptoms:** Connection error immediately after clicking Save

**Solutions:**

```bash
# 1. Check if PostgreSQL is running
pg_isready -h localhost -p 5432

# 2. If not running, start it
brew services start postgresql@14
# OR
brew services start postgresql@16

# 3. Wait 5 seconds and try again
```

### Issue 2: "password authentication failed for user mdub"

**Symptoms:** Password error even though you left password blank

**Solutions:**

**Option A: Use Trust Authentication (Local Development)**

1. Find your pg_hba.conf file:
```bash
# For Homebrew PostgreSQL 14
/opt/homebrew/var/postgresql@14/pg_hba.conf

# For Homebrew PostgreSQL 16
/opt/homebrew/var/postgresql@16/pg_hba.conf
```

2. Edit the file and ensure this line exists:
```
host    all    all    127.0.0.1/32    trust
```

3. Restart PostgreSQL:
```bash
brew services restart postgresql@14
```

**Option B: Set a Password**

```bash
# Connect to PostgreSQL
psql -h localhost -U mdub -d postgres

# Set password
ALTER USER mdub WITH PASSWORD 'your_password';
\q
```

Then in pgAdmin, enter the password you just set.

### Issue 3: "database reflex_dev does not exist"

**Solution:** Create the database

```bash
psql -h localhost -U mdub -d postgres -c "CREATE DATABASE reflex_dev;"
```

Then try connecting again in pgAdmin.

### Issue 4: Server appears but is grayed out

**Symptoms:** Server icon is gray/disconnected

**Solutions:**

1. Right-click the server → **"Connect Server"**
2. If it asks for a password, try leaving it blank or entering your system password
3. Check "Save password" so it doesn't ask again

### Issue 5: "peer authentication failed"

**Symptoms:** Error mentioning "peer authentication"

**Solution:** This happens when PostgreSQL expects Unix socket authentication.

In pgAdmin Connection settings:
- Make sure **"Host name/address"** is set to `localhost` (not blank)
- This forces TCP/IP connection instead of Unix socket

---

## 🎨 Alternative Database GUI Tools

If pgAdmin doesn't work for you, try these alternatives:

### 1. **DBeaver** (Free, Cross-platform)

**Download:** https://dbeaver.io/

**Connection Settings:**
- Driver: PostgreSQL
- Host: `localhost`
- Port: `5432`
- Database: `reflex_dev`
- Username: `mdub`
- Authentication: Database Native
- Password: (leave blank)

### 2. **TablePlus** (macOS, Paid with free trial)

**Download:** https://tableplus.com/

**Connection Settings:**
- Connection Type: PostgreSQL
- Name: Reflex Local
- Host: `localhost`
- Port: `5432`
- Database: `reflex_dev`
- User: `mdub`

### 3. **Postico** (macOS, Paid)

**Download:** https://eggerapps.at/postico/

**Connection Settings:**
- Host: `localhost`
- Port: `5432`
- Database: `reflex_dev`
- User: `mdub`

### 4. **DataGrip** (JetBrains, Paid)

**Download:** https://www.jetbrains.com/datagrip/

**Connection Settings:**
- Driver: PostgreSQL
- Host: `localhost`
- Port: `5432`
- Database: `reflex_dev`
- User: `mdub`

---

## 🔄 Switching from SQLite to PostgreSQL

If you're currently using SQLite and want to switch to PostgreSQL:

### Method 1: Using the Setup Script

```bash
# Make the script executable (first time only)
chmod +x db_setup.sh

# Run the setup script
./db_setup.sh postgres

# Initialize tables
./db_setup.sh init
```

### Method 2: Manual Setup

```bash
# 1. Set environment variable
export DATABASE_URL="postgresql://mdub@localhost:5432/reflex_dev"

# 2. Initialize database tables
reflex db init

# 3. Run the app
reflex run
```

### Method 3: Using .env.local file

1. Create or edit `.env.local`:
```bash
echo "DATABASE_URL=postgresql://mdub@localhost:5432/reflex_dev" > .env.local
```

2. Update `rxconfig.py` to load from .env.local:
```python
from dotenv import load_dotenv
load_dotenv('.env.local')
```

3. Restart your app

---

## 📊 Useful SQL Queries for pgAdmin

Once connected, you can run these queries in pgAdmin's Query Tool:

### View all tables
```sql
SELECT table_name 
FROM information_schema.tables 
WHERE table_schema = 'public';
```

### View all users
```sql
SELECT * FROM localuser;
```

### Count records in each table
```sql
SELECT 
  schemaname,
  tablename,
  (SELECT COUNT(*) FROM (SELECT * FROM schemaname || '.' || tablename) AS t) as row_count
FROM pg_tables
WHERE schemaname = 'public';
```

### Check table structure
```sql
SELECT column_name, data_type, character_maximum_length
FROM information_schema.columns
WHERE table_name = 'localuser';
```

### View recent sessions
```sql
SELECT * FROM localauthsession
ORDER BY expiration DESC
LIMIT 10;
```

---

## 🔐 Security Notes

### For Local Development
- Using trust authentication (no password) is **acceptable** for local development
- Your database is only accessible from your machine

### For Production
- **Always** use strong passwords
- **Never** expose database ports to the internet
- Use SSL/TLS connections
- Consider using connection pooling (PgBouncer)
- Set up proper user permissions (don't use superuser)

---

## 💡 Tips & Tricks

### 1. Save Frequently Used Queries
- In pgAdmin, go to **Tools** → **Query Tool**
- Write your query, then **File** → **Save** to save it for later

### 2. View Table Data Easily
- Right-click any table → **View/Edit Data** → **All Rows**

### 3. Export Data
- Right-click table → **Import/Export Data**
- Choose format (CSV, JSON, etc.)

### 4. Backup Database
```bash
# Command line backup
pg_dump -h localhost -U mdub reflex_dev > backup.sql

# Restore
psql -h localhost -U mdub reflex_dev < backup.sql
```

### 5. Monitor Active Connections
```sql
SELECT * FROM pg_stat_activity;
```

---

## 📚 Additional Resources

- **pgAdmin Documentation:** https://www.pgadmin.org/docs/
- **PostgreSQL Documentation:** https://www.postgresql.org/docs/
- **Reflex Database Docs:** https://reflex.dev/docs/database/overview/
- **SQLAlchemy ORM:** https://docs.sqlalchemy.org/

---

## ✨ Quick Command Reference

```bash
# Check if PostgreSQL is running
pg_isready -h localhost -p 5432

# List all databases
psql -h localhost -U mdub -d postgres -c "\l"

# Connect to database
psql -h localhost -U mdub -d reflex_dev

# List tables in database
psql -h localhost -U mdub -d reflex_dev -c "\dt"

# View table structure
psql -h localhost -U mdub -d reflex_dev -c "\d localuser"

# Run SQL file
psql -h localhost -U mdub -d reflex_dev -f script.sql

# Create database
psql -h localhost -U mdub -d postgres -c "CREATE DATABASE reflex_dev;"

# Drop database (CAREFUL!)
psql -h localhost -U mdub -d postgres -c "DROP DATABASE reflex_dev;"
```

---

## 🆘 Still Having Issues?

If you're still having trouble connecting:

1. **Check the connection info file:**
   ```bash
   cat .env/DATABASE_CONNECTION.md
   ```

2. **Test connection from command line:**
   ```bash
   psql -h localhost -U mdub -d reflex_dev
   ```

3. **View PostgreSQL logs:**
   ```bash
   # Homebrew PostgreSQL 14
   tail -f /opt/homebrew/var/log/postgresql@14.log
   ```

4. **Run the diagnostic script:**
   ```bash
   ./db_setup.sh test
   ```

5. **Check the Reflex app connection:**
   ```bash
   python -c "from rxconfig import config; print(config.db_url)"
   ```

---

**Last Updated:** 2024-02-17
**Your Database:** reflex_dev
**Your Username:** mdub
**Host:** localhost:5432