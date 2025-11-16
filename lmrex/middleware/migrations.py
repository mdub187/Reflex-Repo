# lmrex/middleware/migrations.py

import os
from sqlalchemy import create_engine
from alembic.config import Config
from alembic import command
from lmrex.models import Base


class MigrationManager:
    """Handles database initialization and Alembic migrations"""

    def __init__(self, db_url: str = "sqlite:///database.db"):
        self.db_url = db_url or os.getenv("DATABASE_URL", "sqlite:///database.db")
        self.engine = create_engine(self.db_url)

    def init_database(self):
        """Initialize database and create tables"""
        try:
            Base.metadata.create_all(bind=self.engine)
            print("✓ Database tables created successfully")
        except Exception as e:
            print(f"✗ Error creating database tables: {e}")
            raise

    def run_migrations(self):
        """Run Alembic migrations to bring database to latest version"""
        try:
            alembic_cfg = Config("alembic.ini")
            command.upgrade(alembic_cfg, "head")
            print("✓ Database migrations applied successfully")
        except Exception as e:
            print(f"✗ Error running migrations: {e}")
            # Don't raise here - allow app to continue even if migrations fail

    def get_current_revision(self):
        """Get current Alembic revision"""
        try:
            alembic_cfg = Config("alembic.ini")
            return command.current(alembic_cfg)
        except Exception as e:
            print(f"Error getting current revision: {e}")
            return None

    def get_migration_history(self):
        """Get migration history"""
        try:
            alembic_cfg = Config("alembic.ini")
            return command.history(alembic_cfg)
        except Exception as e:
            print(f"Error getting migration history: {e}")
            return None

    def create_migration(self, message: str):
        """Create a new migration"""
        try:
            alembic_cfg = Config("alembic.ini")
            command.revision(alembic_cfg, autogenerate=True, message=message)
            print(f"✓ Migration created: {message}")
        except Exception as e:
            print(f"✗ Error creating migration: {e}")
            raise

    def downgrade_migration(self, revision: str = "-1"):
        """Downgrade to specific revision"""
        try:
            alembic_cfg = Config("alembic.ini")
            command.downgrade(alembic_cfg, revision)
            print(f"✓ Downgraded to revision: {revision}")
        except Exception as e:
            print(f"✗ Error downgrading migration: {e}")
            raise

    def initialize(self):
        """Complete database initialization process"""
        print("🚀 Initializing database...")

        # Create tables first
        self.init_database()

        # Then run migrations
        self.run_migrations()

        # Show current status
        current_rev = self.get_current_revision()
        if current_rev:
            print(f"📊 Current database revision: {current_rev}")
        else:
            print("📊 No migrations applied yet")

        print("✅ Database initialization complete!")


def init_database_on_startup():
    """Convenience function to initialize database on app startup"""
    migration_manager = MigrationManager()
    migration_manager.initialize()
    return migration_manager


if __name__ == "__main__":
    # Allow running migrations directly
    import sys

    manager = MigrationManager()

    if len(sys.argv) > 1:
        command = sys.argv[1]

        if command == "init":
            manager.initialize()
        elif command == "upgrade":
            manager.run_migrations()
        elif command == "current":
            print(manager.get_current_revision())
        elif command == "history":
            print(manager.get_migration_history())
        elif command == "create" and len(sys.argv) > 2:
            manager.create_migration(sys.argv[2])
        elif command == "downgrade":
            revision = sys.argv[2] if len(sys.argv) > 2 else "-1"
            manager.downgrade_migration(revision)
        else:
            print(
                "Available commands: init, upgrade, current, history, create <message>, downgrade [revision]"
            )
    else:
        manager.initialize()
