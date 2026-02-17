#!/usr/bin/env python3
"""
PostgreSQL Database Initialization Script for Reflex App

This script creates all necessary database tables for the Reflex application.
Run this after setting up your PostgreSQL database.

Usage:
    export DATABASE_URL="postgresql://mdub@localhost:5432/reflex_dev"
    python init_db_postgres.py
"""

import os
import sys
from sqlalchemy import create_engine, inspect, text
from sqlalchemy.exc import OperationalError


def print_header(message):
    """Print a formatted header."""
    print("\n" + "=" * 70)
    print(f"  {message}")
    print("=" * 70)


def print_success(message):
    """Print a success message."""
    print(f"✓ {message}")


def print_error(message):
    """Print an error message."""
    print(f"✗ {message}")


def print_info(message):
    """Print an info message."""
    print(f"ℹ {message}")


def get_database_url():
    """Get database URL from environment or config."""
    # Try environment variable first
    db_url = os.getenv("DATABASE_URL")
    
    if not db_url:
        # Try loading from rxconfig
        try:
            sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
            from rxconfig import config
            db_url = config.db_url
            print_info(f"Using database URL from rxconfig")
        except Exception as e:
            print_error(f"Could not load database URL: {e}")
            return None
    else:
        print_info(f"Using database URL from environment variable")
    
    return db_url


def test_connection(engine):
    """Test database connection."""
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT version();"))
            version = result.fetchone()[0]
            print_success(f"Connected to PostgreSQL")
            print_info(f"Version: {version[:50]}...")
            return True
    except OperationalError as e:
        print_error(f"Connection failed: {e}")
        return False


def create_tables(engine):
    """Create all database tables."""
    print_header("Creating Database Tables")
    
    try:
        # Import all models to register them with SQLModel
        print_info("Loading models...")
        
        # Import reflex_local_auth models
        from reflex_local_auth.local_auth import LocalUser, LocalAuthSession
        print_success("Loaded authentication models")
        
        # Import custom models
        try:
            from lmrex.models.user_model import Admin, NewUser, UserGallery
            print_success("Loaded user models")
        except ImportError as e:
            print_info(f"Could not load custom user models: {e}")
        
        try:
            from lmrex.models.contact_model import Contact
            print_success("Loaded contact model")
        except ImportError as e:
            print_info(f"Could not load contact model: {e}")
        
        # Import SQLModel metadata
        from sqlmodel import SQLModel
        
        # Create all tables
        print_info("Creating tables in database...")
        SQLModel.metadata.create_all(engine)
        print_success("All tables created successfully")
        
        return True
        
    except Exception as e:
        print_error(f"Error creating tables: {e}")
        import traceback
        traceback.print_exc()
        return False


def list_tables(engine):
    """List all tables in the database."""
    print_header("Database Tables")
    
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    
    if tables:
        print_info(f"Found {len(tables)} table(s):")
        for table in sorted(tables):
            print(f"  • {table}")
            
            # Show column info
            columns = inspector.get_columns(table)
            for col in columns:
                col_type = str(col['type'])
                nullable = "NULL" if col['nullable'] else "NOT NULL"
                print(f"    - {col['name']}: {col_type} {nullable}")
    else:
        print_info("No tables found in database")
    
    return tables


def verify_required_tables(engine):
    """Verify that required tables exist."""
    print_header("Verifying Required Tables")
    
    inspector = inspect(engine)
    existing_tables = set(inspector.get_table_names())
    
    required_tables = {
        'localuser': 'Authentication users',
        'localauthsession': 'Authentication sessions',
    }
    
    optional_tables = {
        'admin': 'Admin users',
        'newuser': 'User registrations',
        'usergallery': 'User gallery items',
        'contact': 'Contact information',
    }
    
    all_good = True
    
    # Check required tables
    for table, description in required_tables.items():
        if table in existing_tables:
            print_success(f"{table:20} - {description}")
        else:
            print_error(f"{table:20} - MISSING! ({description})")
            all_good = False
    
    # Check optional tables
    print_info("\nOptional tables:")
    for table, description in optional_tables.items():
        if table in existing_tables:
            print_success(f"{table:20} - {description}")
        else:
            print_info(f"{table:20} - Not found ({description})")
    
    return all_good


def main():
    """Main initialization function."""
    print_header("PostgreSQL Database Initialization")
    
    # Get database URL
    db_url = get_database_url()
    if not db_url:
        print_error("No database URL configured!")
        print_info("Set DATABASE_URL environment variable:")
        print_info('  export DATABASE_URL="postgresql://mdub@localhost:5432/reflex_dev"')
        sys.exit(1)
    
    # Mask password in output
    display_url = db_url
    if '@' in db_url and ':' in db_url:
        parts = db_url.split('@')
        user_pass = parts[0].split('//')[-1]
        if ':' in user_pass:
            user, _ = user_pass.split(':', 1)
            display_url = db_url.replace(user_pass, f"{user}:****")
    
    print_info(f"Database: {display_url}")
    
    # Create engine
    print_info("Creating database engine...")
    try:
        engine = create_engine(db_url, echo=False)
    except Exception as e:
        print_error(f"Could not create engine: {e}")
        sys.exit(1)
    
    # Test connection
    print_header("Testing Database Connection")
    if not test_connection(engine):
        print_error("Cannot connect to database!")
        print_info("Make sure PostgreSQL is running:")
        print_info("  brew services start postgresql@14")
        print_info("And that the database exists:")
        print_info('  psql -h localhost -U mdub -d postgres -c "CREATE DATABASE reflex_dev;"')
        sys.exit(1)
    
    # Check existing tables
    inspector = inspect(engine)
    existing_tables = inspector.get_table_names()
    
    if existing_tables:
        print_info(f"\nFound {len(existing_tables)} existing table(s)")
        print_info("This will add any missing tables")
    else:
        print_info("\nNo existing tables found - will create all tables")
    
    # Create tables
    if not create_tables(engine):
        print_error("\nTable creation failed!")
        sys.exit(1)
    
    # List all tables
    tables = list_tables(engine)
    
    # Verify required tables
    if not verify_required_tables(engine):
        print_error("\nSome required tables are missing!")
        sys.exit(1)
    
    # Success!
    print_header("Initialization Complete")
    print_success("Database is ready to use!")
    print_info("\nYou can now:")
    print_info("  1. Connect with pgAdmin using the connection info in PGADMIN_QUICK_REFERENCE.txt")
    print_info("  2. Run your Reflex app: reflex run")
    print_info("  3. View tables: psql -h localhost -U mdub -d reflex_dev -c '\\dt'")
    
    print("\n" + "=" * 70 + "\n")


if __name__ == "__main__":
    main()