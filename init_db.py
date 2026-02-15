#!/usr/bin/env python3
"""
Database Initialization Script for Reflex Application
Run this before starting the application to ensure database tables exist.

Usage:
    python init_db.py
"""

import sys
import os
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

def init_database():
    """Initialize database tables"""
    print("=" * 60)
    print("Database Initialization Script")
    print("=" * 60)
    
    try:
        # Import configuration
        print("Loading configuration...")
        from rxconfig import config
        print(f"   Database URL: {config.db_url[:50]}...")
        
        # Import SQLAlchemy and SQLModel tools
        from sqlalchemy import create_engine, inspect
        import sqlmodel
        
        # Import models to ensure they're registered
        print("Loading models...")
        from reflex_local_auth.local_auth import LocalUser, LocalAuthSession
        
        # Create engine
        print("Connecting to database...")
        engine = create_engine(config.db_url)
        
        # Test connection
        try:
            with engine.connect() as conn:
                result = conn.execute(sqlmodel.text("SELECT 1"))
                result.fetchone()
            print("Database connection successful")
        except Exception as e:
            print(f"Database connection failed: {e}")
            return False
        
        # Check existing tables
        print("Checking existing tables...")
        inspector = inspect(engine)
        existing_tables = inspector.get_table_names()
        print(f"   Found {len(existing_tables)} existing tables: {existing_tables}")
        
        # Define required tables
        required_tables = {'localuser', 'localauthsession'}
        missing_tables = required_tables - set(existing_tables)
        
        if missing_tables:
            print(f"Missing tables: {missing_tables}")
            print("Creating database tables...")
            
            # Create tables using SQLModel
            sqlmodel.SQLModel.metadata.create_all(engine)
            
            print("Tables created successfully")
        else:
            print("All required tables exist")
        
        # Verify tables were created
        print("Verifying tables...")
        inspector = inspect(engine)
        final_tables = inspector.get_table_names()
        print(f"   Total tables: {len(final_tables)}")
        
        verification_missing = required_tables - set(final_tables)
        if verification_missing:
            print(f"Still missing tables: {verification_missing}")
            return False
        
        # Show table details
        for table in required_tables:
            if table in final_tables:
                columns = inspector.get_columns(table)
                print(f"   Table '{table}': {len(columns)} columns")
        
        print("=" * 60)
        print("Database initialization complete!")
        print("=" * 60)
        return True
        
    except ImportError as e:
        print(f"Import error: {e}")
        print("   Make sure all dependencies are installed:")
        print("   pip install reflex reflex-local-auth sqlalchemy sqlmodel")
        return False
        
    except Exception as e:
        print(f"Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = init_database()
    sys.exit(0 if success else 1)