---
name: Database Error Report
about: Report issues related to "no such table" or database initialization errors
title: '[DB] '
labels: bug, database
assignees: ''
---

## Error Description

**Error Message:**
```
(Paste the full error message here)
```

**Error Type:**
- [ ] `no such table: localuser`
- [ ] `no such table: localauthsession`
- [ ] Database connection error
- [ ] Other database error (specify below)

## Have You Tried the Quick Fix?

Before reporting, please try these steps:

- [ ] Ran `python init_db.py`
- [ ] Checked that `DATABASE_URL` is set correctly
- [ ] Verified database is accessible
- [ ] Reviewed [QUICK_START.md](../../QUICK_START.md)
- [ ] Reviewed [DEPLOYMENT.md](../../DEPLOYMENT.md)

## Environment

**Platform:** (select one)
- [ ] Local Development
- [ ] Render
- [ ] Railway
- [ ] Fly.io
- [ ] Docker
- [ ] Other: _______________

**Operating System:**
- [ ] macOS
- [ ] Linux
- [ ] Windows
- [ ] Other: _______________

**Python Version:** (e.g., 3.11.5)
```
python --version
```

**Reflex Version:** (e.g., 0.4.0)
```
reflex --version
```

**Database:**
- [ ] PostgreSQL (production)
- [ ] SQLite (development)
- [ ] Other: _______________

## Steps to Reproduce

1. 
2. 
3. 

## Expected Behavior

What should happen?

## Actual Behavior

What actually happens?

## Logs

**Full Error Traceback:**
```
(Paste the complete error traceback here)
```

**Database Initialization Output:**
```bash
# Run this and paste the output:
python init_db.py
```

**Database Tables Check:**
```bash
# For SQLite:
sqlite3 reflex.db ".tables"

# For PostgreSQL:
psql $DATABASE_URL -c "\dt"

# Paste the output here:
```

## Configuration

**rxconfig.py Database URL (sanitized):**
```python
# Remove passwords before pasting:
DATABASE_URL = "postgresql://user:****@host/database"
```

**Environment Variables Set:**
- [ ] `DATABASE_URL`
- [ ] `PRODUCTION`
- [ ] `BACKEND_PORT`
- [ ] `FRONTEND_PORT`

## Additional Context

Add any other context about the problem here.

## Checklist

- [ ] I have read the [QUICK_START.md](../../QUICK_START.md) guide
- [ ] I have tried running `python init_db.py`
- [ ] I have checked my database connection
- [ ] I have reviewed the [troubleshooting section](../../DEPLOYMENT.md#troubleshooting)
- [ ] I have sanitized sensitive information (passwords, tokens, etc.)

## Possible Solution

If you have any ideas on how to fix this, please share them here.

---

**Note:** Most database errors can be fixed by running `python init_db.py` before starting the application. See [QUICK_START.md](../../QUICK_START.md) for details.