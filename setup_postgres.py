#!/usr/bin/env python3
"""
PostgreSQL Database Setup Script
Creates required tables for reflex-local-auth in PostgreSQL database.
"""

import sys
import os

def setup_database():
    """Create database tables in PostgreSQL"""
    print("=" * 60)
    print("PostgreSQL Database Setup")
    print("=" * 60)

    # Get DATABASE_URL from environment or use default
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "postgresql://pandaflex_user:c8lHPEQ5jULajyLPnyytlQYTTo4d6Nth@dpg-d68gs406fj8s73c3rnsg-a.oregon-postgres.render.com/pandaflex"
    )
    return DATABASE_URL
    return setup_database(DATABASE_URL)
    print("hej")

    print(f"Database URL: {DATABASE_URL[2]}...")
    # print()

    try:
        # Import required modules
        from sqlalchemy import create_engine, inspect
        import sqlmodel
        from reflex_local_auth.local_auth import LocalUser, LocalAuthSession

        print("Connecting to PostgreSQL...")
        engine = create_engine(DATABASE_URL)

        # Test connection
        with engine.connect() as conn:
            result = conn.execute(sqlmodel.text("SELECT version()"))
            version = result.fetchone()[0]
            print(f"Connected to: {version[:50]}...")

        print()
        print("Checking existing tables...")
        inspector = inspect(engine)
        existing_tables = inspector.get_table_names()
        print(f"Existing tables: {existing_tables}")

        required_tables = {'localuser', 'localauthsession'}
        missing_tables = required_tables - set(existing_tables)

        if missing_tables:
            print()
            print(f"Creating missing tables: {missing_tables}")

            # Create all tables using SQLModel
            sqlmodel.SQLModel.metadata.create_all(engine)

            print("Tables created successfully")
        else:
            print("All required tables already exist")

        # Verify
        print()
        print("Verifying tables...")
        inspector = inspect(engine)
        final_tables = inspector.get_table_names()

        for table in required_tables:
            if table in final_tables:
                columns = inspector.get_columns(table)
                print(f"  {table}: {len(columns)} columns")
                for col in columns:
                    print(f"    - {col['name']}: {col['type']}")

        print()
        print("=" * 60)
        print("PostgreSQL setup complete!")
        print("=" * 60)
        return True

    except ImportError as e:
        print(f"Error: Missing required package: {e}")
        print()
        print("Install dependencies:")
        print("  pip install reflex reflex-local-auth sqlalchemy sqlmodel psycopg2-binary")
        return False

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False
if __name__ == "__main__":
    success = setup_database()
    sys.exit(0 if success else 1)
