# Reflex Application

A modern web application built with [Reflex](https://reflex.dev) featuring authentication, responsive design, and PostgreSQL/SQLite database support.

## 🚨 Database Error Fix

**Seeing `no such table: localuser` error?** We've got you covered!

### Quick Fix (2 minutes)

```bash
# 1. Initialize the database
python init_db.py

# 2. Start the app
reflex run
```

**That's it!** See [QUICK_START.md](QUICK_START.md) for more details.

## 📚 Documentation

- **[QUICK_START.md](QUICK_START.md)** - Fix database errors and get running fast
- **[DEPLOYMENT.md](DEPLOYMENT.md)** - Complete deployment guide for production
- **[docs/](docs/)** - Additional documentation

## ✨ Features

- 🔐 **Authentication** - Secure login/logout with `reflex-local-auth`
- 🎨 **Responsive Design** - Mobile-first, works on all devices
- 📊 **Database Support** - PostgreSQL (production) and SQLite (development)
- 🚀 **Auto-Configuration** - Detects Render, Railway, Fly.io environments
- 🔄 **Dynamic Ports** - Automatically finds available ports
- 🛡️ **CORS Protection** - Configurable CORS for security
- 🎭 **Modern UI** - Clean, professional interface

## 🏃 Quick Start

### Prerequisites

- Python 3.11 or higher
- Node.js 16+ (for frontend)
- PostgreSQL (for production) or SQLite (auto-configured for dev)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd Reflex-Repo
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize database:**
   ```bash
   python init_db.py
   ```

5. **Start the application:**
   ```bash
   reflex run
   ```

6. **Open your browser:**
   ```
   http://localhost:3000
   ```

## 🚀 Deployment

### Quick Deploy Commands

**Build Command:**
```bash
pip install -r requirements.txt && python init_db.py
```

**Start Command:**
```bash
reflex run --env prod
```

### Environment Variables

Set these in your deployment platform:

- `DATABASE_URL` - PostgreSQL connection string (required for production)
- `PRODUCTION=true` - Enable production mode
- `BACKEND_PORT=8000` - Backend port (optional)
- `FRONTEND_PORT=3000` - Frontend port (optional)

### Platform Support

- ✅ Render - Auto-detected, zero config
- ✅ Railway - Auto-detected, zero config
- ✅ Fly.io - Auto-detected, zero config
- ✅ Docker - Dockerfile included
- ✅ Generic - Works anywhere

See [DEPLOYMENT.md](DEPLOYMENT.md) for platform-specific instructions.

## 🗂️ Project Structure

```
Reflex-Repo/
├── lmrex/                      # Main application package
│   ├── state/                  # State management
│   │   └── auth_state.py      # Authentication state (with error handling)
│   ├── ui/                     # UI components
│   │   ├── index.py           # Home page
│   │   ├── login.py           # Login page
│   │   ├── account.py         # User account page
│   │   └── ...                # Other pages
│   ├── routes/                 # Route definitions
│   │   └── routes.py          # Application routes
│   └── lmrex.py               # App entry point
├── shell/                      # Utility scripts
│   └── start_reflex.sh        # Enhanced startup script
├── alembic_migrations/         # Database migrations
├── init_db.py                  # Database initialization script ⭐
├── deploy_start.sh            # Production deployment script ⭐
├── rxconfig.py                # Reflex configuration
├── requirements.txt           # Python dependencies
├── QUICK_START.md             # Quick start guide ⭐
└── DEPLOYMENT.md              # Deployment documentation ⭐
```

⭐ = New files that fix the database error

## 🔧 Development

### Running with Custom Ports

```bash
# Method 1: Environment variables
BACKEND_PORT=8080 FRONTEND_PORT=3001 reflex run

# Method 2: Enhanced script
./shell/start_reflex.sh -b 8080 -f 3001

# Method 3: Let it auto-detect
reflex run  # Finds available ports automatically
```

### Database Management

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

### Clean Rebuild

```bash
# Remove build artifacts
rm -rf .web .states

# Reinitialize
reflex init
reflex run
```

## 🛠️ Troubleshooting

### Database Issues

**Problem:** `no such table: localuser`
```bash
python init_db.py
```

**Problem:** PostgreSQL connection fails locally
- The app automatically falls back to SQLite for local development
- No action needed!

**Problem:** Authentication not working
```bash
rm -rf .states
python init_db.py
reflex run
```

### Frontend Issues

**Problem:** Frontend won't load
```bash
rm -rf .web
reflex init
cd .web && npm install --legacy-peer-deps
cd .. && reflex run
```

**Problem:** Icon warnings
- The app uses Lucide icons
- Warnings about invalid icons are non-critical
- Replace `check_circle` with `check_check` or `circle_check` if desired

### Port Issues

**Problem:** Port already in use
```bash
# Kill existing processes
pkill -f "reflex run"

# Or use the auto-port script
./shell/start_reflex.sh
```

See [DEPLOYMENT.md](DEPLOYMENT.md) for complete troubleshooting guide.

## 🔐 Authentication

The app uses `reflex-local-auth` for secure authentication:

- Username/password authentication
- Session management
- Password hashing with bcrypt
- Protected routes
- User account management

### Creating Users

Users can register through the login page, or you can create them programmatically:

```python
from reflex_local_auth.local_auth import LocalUser
from sqlmodel import Session, select
from rxconfig import config
from sqlalchemy import create_engine

engine = create_engine(config.db_url)
with Session(engine) as session:
    user = LocalUser(username="admin", password="password123")
    session.add(user)
    session.commit()
```

## 📦 Dependencies

Key dependencies:

- **reflex** - Web framework
- **reflex-local-auth** - Authentication
- **sqlalchemy** - Database ORM
- **sqlmodel** - SQL toolkit
- **psycopg2-binary** - PostgreSQL driver
- **alembic** - Database migrations

See `requirements.txt` for complete list.

## 🌟 What's New

### v2.0 (February 2026)

✅ **Database Error Fixed!**
- Added `init_db.py` initialization script
- Enhanced `auth_state.py` with error handling
- Smart database fallback (PostgreSQL → SQLite)
- Automated deployment script

✅ **Improved Deployment**
- Platform auto-detection (Render, Railway, Fly.io)
- Zero-config deployment
- Better error messages
- Health check endpoints

✅ **Better Developer Experience**
- Enhanced startup script with port detection
- Comprehensive documentation
- Quick start guide
- Troubleshooting help

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly (including database initialization)
5. Submit a pull request

## 📄 License

[Your License Here]

## 🙏 Acknowledgments

- Built with [Reflex](https://reflex.dev)
- Authentication by [reflex-local-auth](https://github.com/reflex-dev/reflex-local-auth)
- Inspired by modern web development practices

## 📞 Support

- **Quick Fix:** See [QUICK_START.md](QUICK_START.md)
- **Deployment:** See [DEPLOYMENT.md](DEPLOYMENT.md)
- **Issues:** Open an issue on GitHub
- **Docs:** Check the [docs/](docs/) folder

---

**Made with ❤️ using Reflex**

Last Updated: February 2026