# lmrex/components/check_tables.py
import os
import sys
from pathlib import Path
from sqlmodel import create_engine, inspect

# Get the absolute path to the project root
project_root = Path(__file__).parent.parent.absolute()

# Add the project root to the Python path
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

# Now import your models
from lmrex.models.user_model import LocalAuthSession, LocalUser
def check_tables():
    """Check if required tables exist in the database."""
    try:
        # Use the same database URL as your application
        DATABASE_URL = (
            "postgresql://pandaflex_user:c8lHPEQ5jULajyLPnyytlQYTTo4d6Nth@dpg-d68gs406fj8s73c3rnsg-a/pandaflex"  # Update this with your actual database URL
        )
        engine = create_engine(DATABASE_URL)
        inspector = inspect(engine)
        print("Tables in the database:")
        print(inspector.get_table_names())
        required_tables = ["localuser", "localauthsession"]
        missing_tables = []
        for table in required_tables:
            exists = table in inspector.get_table_names()
            print(f"Table '{table}' exists: {exists}")
            if not exists:
                missing_tables.append(table)
        if missing_tables:
            print(f"Missing tables detected: {', '.join(missing_tables)}")
            print("Attempting to create missing tables...")

            from sqlmodel import SQLModel

            SQLModel.metadata.create_all(engine)

            print(
                "Tables created successfully. Please try running your application again."
            )
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("Please check your database configuration and try again.")

if __name__ == "__main__":
    check_tables()
