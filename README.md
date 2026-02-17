#  Boiler-ish Reflex Application
##  Can be used as a template for any type of marketplace, blog, or media full stack website.
A modern web application built with [Reflex](https://reflex.dev) featuring authentication, responsive design, and PostgreSQL database support.

**IMPORTANT: This application requires PostgreSQL (not SQLite).**

##  Database Error Fix
###  this is the most prominent error so far

`no such table: localuser` error

#### Fix

```bash
 # Initialize the database
python init_db.py

 # Start the app
reflex run
```
See [QUICK_START.md](QUICK_START.md) for more details.


##  Documentation

- **[QUICK_START.md](QUICK_START.md)** - Fix database errors and get running fast
- **[POSTGRES_SETUP.md](POSTGRES_SETUP.md)** - PostgreSQL setup guide
- **[DEPLOYMENT.md](DEPLOYMENT.md)** - Complete deployment guide for production
- **[docs/](docs/)** - Additional documentation


##  Features

- **Authentication** - Secure login/logout with `reflex-local-auth`
- **Responsive Design** - Mobile-first, works on all devices
- **Database** - PostgreSQL required for production and development
- **Auto-Configuration** - Detects Render, Railway, Fly.io environments
- **Dynamic Ports** - Automatically finds available ports
- **CORS Protection** - Configurable CORS for security
- **Modern UI** - Clean, professional interface

##  Quick Start


###  Prerequisites

- Python 3.11 or higher, (I would recommend keeping your python venv set to 3.11, as reflex is having regression issues with 3.14 see https://github.com/reflex-dev/reflex/issues/5964)#5964
- Node.js 16+ (for frontend)
- **PostgreSQL** (required - see [POSTGRES_SETUP.md](POSTGRES_SETUP.md))

###  Installation 

. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd Reflex-Repo
   ```

. Create virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   Windows: .venv\Scripts\activate
   ```

. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

. Initialize database:
   ```bash
   python init_db.py
   ```

. Start the application:
   ```bash
   reflex run
   ```

. Open your browser:
   ```
   http://localhost:
   ```

###  Deployment

-- Quick Deploy Commands --

. Build Command:
```bash
pip install -r requirements.txt && python init_db.py
```

. Start Command:
```bash
reflex run --env prod
```

-- Environment Variables --

Set these in your deployment platform:

- `DATABASE_URL` - PostgreSQL connection string (required for production)
- `PRODUCTION=true` - Enable production mode
- `BACKEND_PORT=` - Backend port (optional)
- `FRONTEND_PORT=` - Frontend port (optional)

. Platform Support

-  Render - Auto-detected, zero config
-  Railway - Auto-detected, zero config
-  Fly.io - Auto-detected, zero config
-  Docker - Dockerfile included
-  Generic - Works anywhere

See [DEPLOYMENT.md](DEPLOYMENT.md) for platform-specific instructions.

 -- Project Structure --

```
Reflex-Repo/
├── lmrex/                       Main application package
│   ├── state/                   State management
│   │   └── auth_state.py       Authentication state (with error handling)
│   ├── ui/                      UI components
│   │   ├── index.py            Home page
│   │   ├── login.py            Login page
│   │   ├── account.py          User account page
│   │   └── ...                 Other pages
│   ├── routes/                  Route definitions
│   │   └── routes.py           Application routes
│   └── lmrex.py                App entry point
├── shell/                       Utility scripts
│   └── start_reflex.sh         Enhanced startup script
├── alembic_migrations/          Database migrations
├── init_db.py                   Database initialization script 
├── deploy_start.sh             Production deployment script 
├── rxconfig.py                 Reflex configuration
├── requirements.txt            Python dependencies
├── QUICK_START.md              Quick start guide 
└── DEPLOYMENT.md               Deployment documentation 
```

 = New files that fix the database error

###  Development 

. Running with Custom Ports

```bash
 Method : Environment variables
BACKEND_PORT= FRONTEND_PORT= reflex run

 Method : Enhanced script
./shell/start_reflex.sh -b  -f 

 Method : Let it auto-detect
reflex run   Finds available ports automatically
```

. Database Management

```bash
# Initialize database
python init_db.py

# Create migration
reflex db makemigrations -m "description"

# Apply migrations
reflex db migrate

# Check migration status
reflex db heads
```

. Clean Rebuild

```bash
# Remove build artifacts
rm -rf .web .states

# Reinitialize
reflex init
reflex run
```

###  Troubleshooting

####  Database Issues

> [!IMPORTANT]
. Problem: `no such table: localuser`
```bash
python init_db.py
```

> [!IMPORTANT]
. Problem: PostgreSQL connection fails locally
- The app automatically falls back to SQLite for local development
- No action needed!

> [!IMPORTANT]
. Problem: `Authentication not working`
```bash
rm -rf .states
python init_db.py
reflex run
```

####  Frontend Issues

> [!IMPORTANT]
. Problem: `Frontend won't load`
```bash
rm -rf .web
reflex init
cd .web && npm install --legacy-peer-deps
cd .. && reflex run
```

> [!IMPORTANT]
. Problem: `Icon warnings`
- The app uses Lucide icons
- Warnings about invalid icons are non-critical
- Replace `check_circle` with `check_check` or `circle_check` if desired

####  Port Issues

> [!IMPORTANT]
. Problem: Port already in use
```bash
 Kill existing processes
pkill -f "reflex run"

 Or use the auto-port script
./shell/start_reflex.sh
```

See [DEPLOYMENT.md](DEPLOYMENT.md) for complete troubleshooting guide.

###  Authentication

The app uses `reflex-local-auth` for secure authentication:

- Username/password authentication
- Session management
- Password hashing with bcrypt
- Protected routes
- User account management

. Creating Users

Users can register through the login page, or you can create them programmatically:

```python
from reflex_local_auth.local_auth import LocalUser
from sqlmodel import Session, select
from rxconfig import config
from sqlalchemy import create_engine

engine = create_engine(config.db_url)
with Session(engine) as session:
    user = LocalUser(username="admin", password="password")
    session.add(user)
    session.commit()
```

###  Dependencies

Key dependencies:

- reflex - Web framework
- reflex-local-auth - Authentication
- sqlalchemy - Database ORM
- sqlmodel - SQL toolkit
- psycopg-binary - PostgreSQL driver
- alembic - Database migrations

See `requirements.txt` for complete list.

  What's New

 v. (February )

 Database Error Fixed!
- Added `init_db.py` initialization script
- Enhanced `auth_state.py` with error handling
- Smart database fallback (PostgreSQL → SQLite)
- Automated deployment script

 Improved Deployment
- Platform auto-detection (Render, Railway, Fly.io)
- Zero-config deployment
- Better error messages
- Health check endpoints

 Better Developer Experience
- Enhanced startup script with port detection
- Comprehensive documentation
- Quick start guide
- Troubleshooting help

  Contributing

Contributions are welcome! Please:

. Fork the repository
. Create a feature branch
. Make your changes
. Test thoroughly (including database initialization)
. Submit a pull request

  License

[Your License Here]

  Acknowledgments

- Built with [Reflex](https://reflex.dev)
- Authentication by [reflex-local-auth](https://github.com/reflex-dev/reflex-local-auth)
- Inspired by modern web development practices

  Support

- Quick Fix: See [QUICK_START.md](QUICK_START.md)
- Deployment: See [DEPLOYMENT.md](DEPLOYMENT.md)
- Issues: Open an issue on GitHub
- Docs: Check the [docs/](docs/) folder

 Github Username
- mdub
 Email
- maweeks.@gmail.com



---

Made with  using Reflex

Last Updated: February
