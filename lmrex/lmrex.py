# lmrex/lmrex.py
"""
Main application entry point with database initialization
"""

import reflex as rx
from sqlalchemy import inspect
from sqlalchemy.exc import OperationalError
import sys

def init_database():
    """Initialize database tables if they don't exist"""
    try:
        # Import config to get db_url
        from rxconfig import config

        # Import models to ensure they're registered
        import reflex_local_auth

        # Get the database engine from the config
        from sqlalchemy import create_engine
        engine = create_engine(config.db_url)

        # Check if tables exist
        inspector = inspect(engine)
        existing_tables = inspector.get_table_names()

        # Check for required auth tables
        required_tables = {'localuser', 'localauthsession'}
        missing_tables = required_tables - set(existing_tables)

        if missing_tables:
            print(f"Missing database tables: {missing_tables}")
            print("Initializing database tables...")

            # Run reflex db init to create tables
            import subprocess
            result = subprocess.run(
                [sys.executable, "-m", "reflex", "db", "init"],
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                print("Database tables created successfully")
            else:
                print(f"Database init warning: {result.stderr}")
                # Continue anyway - tables might be created by other means
        else:
            print("Database tables exist")

    except Exception as e:
        print(f"Database initialization warning: {e}")
        print("Continuing - tables will be created on first use")

# Initialize database before importing routes
print("Initializing application...")
init_database()

# Now import and setup routes
from lmrex.routes.routes import add_routes, app
from lmrex.ui.responsive_utils import apply_responsive_styles

# Build the app once
add_routes()

if __name__ == "__main__":
    apply_responsive_styles()
    print("Hello, World!")
