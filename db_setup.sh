#!/bin/bash

# Database Setup and Connection Helper Script
# This script helps you set up and switch between SQLite and PostgreSQL

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
POSTGRES_USER="mdub"
POSTGRES_HOST="localhost"
POSTGRES_PORT="5432"
POSTGRES_DB="reflex_dev"
SQLITE_PATH="sqlite:///reflex.db"

# Functions
print_header() {
    echo -e "${BLUE}========================================${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}========================================${NC}"
}

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ $1${NC}"
}

# Check if PostgreSQL is running
check_postgres() {
    if pg_isready -h "$POSTGRES_HOST" -p "$POSTGRES_PORT" > /dev/null 2>&1; then
        return 0
    else
        return 1
    fi
}

# Test database connection
test_connection() {
    local db_type=$1
    
    if [ "$db_type" == "postgres" ]; then
        if psql -h "$POSTGRES_HOST" -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c "SELECT 1;" > /dev/null 2>&1; then
            print_success "PostgreSQL connection successful"
            return 0
        else
            print_error "PostgreSQL connection failed"
            return 1
        fi
    elif [ "$db_type" == "sqlite" ]; then
        if [ -f "reflex.db" ]; then
            print_success "SQLite database exists at reflex.db"
            return 0
        else
            print_warning "SQLite database not found (will be created on first use)"
            return 0
        fi
    fi
}

# Setup PostgreSQL
setup_postgres() {
    print_header "Setting Up PostgreSQL"
    
    # Check if PostgreSQL is installed
    if ! command -v psql &> /dev/null; then
        print_error "PostgreSQL is not installed"
        print_info "Install with: brew install postgresql@14"
        exit 1
    fi
    
    # Check if PostgreSQL is running
    if ! check_postgres; then
        print_warning "PostgreSQL is not running"
        print_info "Starting PostgreSQL..."
        brew services start postgresql@14 || brew services start postgresql@16 || brew services start postgresql@17
        sleep 2
        
        if ! check_postgres; then
            print_error "Failed to start PostgreSQL"
            exit 1
        fi
    fi
    
    print_success "PostgreSQL is running"
    
    # Check if database exists
    if psql -h "$POSTGRES_HOST" -U "$POSTGRES_USER" -d postgres -lqt | cut -d \| -f 1 | grep -qw "$POSTGRES_DB"; then
        print_success "Database '$POSTGRES_DB' exists"
    else
        print_info "Creating database '$POSTGRES_DB'..."
        psql -h "$POSTGRES_HOST" -U "$POSTGRES_USER" -d postgres -c "CREATE DATABASE $POSTGRES_DB;" > /dev/null
        print_success "Database '$POSTGRES_DB' created"
    fi
    
    # Test connection
    test_connection "postgres"
    
    # Set environment variable
    export DATABASE_URL="postgresql://$POSTGRES_USER@$POSTGRES_HOST:$POSTGRES_PORT/$POSTGRES_DB"
    
    print_success "PostgreSQL setup complete"
    print_info "Connection string: $DATABASE_URL"
}

# Setup SQLite
setup_sqlite() {
    print_header "Setting Up SQLite"
    
    export DATABASE_URL="$SQLITE_PATH"
    
    test_connection "sqlite"
    
    print_success "SQLite setup complete"
    print_info "Connection string: $DATABASE_URL"
}

# Initialize database tables
init_tables() {
    print_header "Initializing Database Tables"
    
    if [ -f "init_db.py" ]; then
        print_info "Running init_db.py..."
        python init_db.py
    else
        print_info "Running reflex db init..."
        reflex db init
    fi
    
    print_success "Database tables initialized"
}

# Show connection info for GUI apps
show_connection_info() {
    print_header "Database Connection Information"
    
    if [[ "$DATABASE_URL" == postgresql://* ]]; then
        echo ""
        echo "Database Type: PostgreSQL"
        echo "Host: $POSTGRES_HOST"
        echo "Port: $POSTGRES_PORT"
        echo "Database: $POSTGRES_DB"
        echo "Username: $POSTGRES_USER"
        echo "Password: (none required for local)"
        echo ""
        echo "Connection String:"
        echo "  $DATABASE_URL"
        echo ""
        print_info "Use these settings in pgAdmin, DBeaver, TablePlus, etc."
        echo ""
        print_info "pgAdmin Quick Setup:"
        echo "  1. Right-click 'Servers' → 'Register' → 'Server'"
        echo "  2. General Tab - Name: 'Reflex Local Dev'"
        echo "  3. Connection Tab:"
        echo "     - Host: $POSTGRES_HOST"
        echo "     - Port: $POSTGRES_PORT"
        echo "     - Database: $POSTGRES_DB"
        echo "     - Username: $POSTGRES_USER"
        echo "  4. Click 'Save'"
        
    elif [[ "$DATABASE_URL" == sqlite://* ]]; then
        echo ""
        echo "Database Type: SQLite"
        echo "File Path: reflex.db"
        echo ""
        echo "Connection String:"
        echo "  $DATABASE_URL"
        echo ""
        print_info "Use DB Browser for SQLite or similar tools"
        print_info "File location: $(pwd)/reflex.db"
    fi
    
    echo ""
}

# List tables
list_tables() {
    print_header "Database Tables"
    
    if [[ "$DATABASE_URL" == postgresql://* ]]; then
        psql -h "$POSTGRES_HOST" -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c "\dt"
    elif [[ "$DATABASE_URL" == sqlite://* ]]; then
        if [ -f "reflex.db" ]; then
            sqlite3 reflex.db ".tables"
        else
            print_warning "SQLite database not found"
        fi
    fi
}

# Export to .env file
export_to_env() {
    print_header "Exporting to .env file"
    
    if [ -f ".env" ]; then
        # Backup existing .env
        cp .env .env.backup
        print_info "Backed up existing .env to .env.backup"
    fi
    
    # Update or create .env
    if grep -q "DATABASE_URL=" .env 2>/dev/null; then
        # Update existing
        if [[ "$OSTYPE" == "darwin"* ]]; then
            sed -i '' "s|^DATABASE_URL=.*|DATABASE_URL=$DATABASE_URL|" .env
        else
            sed -i "s|^DATABASE_URL=.*|DATABASE_URL=$DATABASE_URL|" .env
        fi
        print_success "Updated DATABASE_URL in .env"
    else
        # Add new
        echo "DATABASE_URL=$DATABASE_URL" >> .env
        print_success "Added DATABASE_URL to .env"
    fi
    
    print_info "To load automatically, add to your shell profile:"
    echo "  echo 'export DATABASE_URL=\"$DATABASE_URL\"' >> ~/.zshrc"
}

# Main menu
show_menu() {
    print_header "Reflex Database Setup Helper"
    echo ""
    echo "1) Setup PostgreSQL (recommended for production-like environment)"
    echo "2) Setup SQLite (simple, file-based)"
    echo "3) Test current database connection"
    echo "4) Initialize/migrate database tables"
    echo "5) Show connection info (for pgAdmin, etc.)"
    echo "6) List database tables"
    echo "7) Export DATABASE_URL to .env file"
    echo "8) Start Reflex app with current database"
    echo "9) Exit"
    echo ""
}

# Main script
main() {
    # Check if running from project root
    if [ ! -f "rxconfig.py" ]; then
        print_error "Please run this script from the project root directory"
        exit 1
    fi
    
    # Check if virtual environment is activated
    if [ -z "$VIRTUAL_ENV" ]; then
        print_warning "Virtual environment not activated"
        print_info "Activating .venv..."
        if [ -f ".venv/bin/activate" ]; then
            source .venv/bin/activate
        else
            print_error "Virtual environment not found. Run: python -m venv .venv"
            exit 1
        fi
    fi
    
    # Check for existing DATABASE_URL
    if [ -n "$DATABASE_URL" ]; then
        print_info "Current DATABASE_URL: $DATABASE_URL"
    fi
    
    if [ $# -eq 0 ]; then
        # Interactive mode
        while true; do
            show_menu
            read -p "Choose an option (1-9): " choice
            echo ""
            
            case $choice in
                1)
                    setup_postgres
                    ;;
                2)
                    setup_sqlite
                    ;;
                3)
                    if [[ "$DATABASE_URL" == postgresql://* ]]; then
                        test_connection "postgres"
                    elif [[ "$DATABASE_URL" == sqlite://* ]]; then
                        test_connection "sqlite"
                    else
                        print_error "No DATABASE_URL set"
                    fi
                    ;;
                4)
                    init_tables
                    ;;
                5)
                    show_connection_info
                    ;;
                6)
                    list_tables
                    ;;
                7)
                    export_to_env
                    ;;
                8)
                    print_info "Starting Reflex app..."
                    reflex run
                    ;;
                9)
                    print_success "Goodbye!"
                    exit 0
                    ;;
                *)
                    print_error "Invalid option"
                    ;;
            esac
            
            echo ""
            read -p "Press Enter to continue..."
            clear
        done
    else
        # Command line mode
        case $1 in
            postgres|pg)
                setup_postgres
                show_connection_info
                ;;
            sqlite)
                setup_sqlite
                show_connection_info
                ;;
            test)
                if [[ "$DATABASE_URL" == postgresql://* ]]; then
                    test_connection "postgres"
                elif [[ "$DATABASE_URL" == sqlite://* ]]; then
                    test_connection "sqlite"
                else
                    print_error "No DATABASE_URL set"
                fi
                ;;
            init)
                init_tables
                ;;
            info)
                show_connection_info
                ;;
            tables)
                list_tables
                ;;
            export)
                export_to_env
                ;;
            *)
                echo "Usage: $0 [postgres|sqlite|test|init|info|tables|export]"
                echo ""
                echo "  postgres - Setup PostgreSQL database"
                echo "  sqlite   - Setup SQLite database"
                echo "  test     - Test database connection"
                echo "  init     - Initialize database tables"
                echo "  info     - Show connection information"
                echo "  tables   - List database tables"
                echo "  export   - Export DATABASE_URL to .env file"
                echo ""
                echo "Run without arguments for interactive mode"
                exit 1
                ;;
        esac
    fi
}

# Run main function
main "$@"