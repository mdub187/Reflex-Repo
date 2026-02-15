# rxconfig.py
import reflex as rx
import socket
import os
import psycopg2

def find_available_port(start_port: int, max_attempts: int = 10) -> int:
    """
    Find an available port starting from start_port.

    Args:
        start_port: The port to start checking from
        max_attempts: Maximum number of ports to try

    Returns:
        First available port found

    Raises:
        RuntimeError: If no available port found within max_attempts
    """
    for port in range(start_port, start_port + max_attempts):
        try:
            # Try to bind to the port
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(("", port))
                return port
        except OSError:
            # Port is in use, try next one
            continue

    raise RuntimeError(
        f"Could not find available port in range {start_port}-{start_port + max_attempts - 1}"
    )


# Detect environment
IS_PRODUCTION = os.getenv("PRODUCTION", "false").lower() == "true" or os.getenv("FLY_APP_NAME") is not None
IS_FLY = os.getenv("FLY_APP_NAME") is not None
IS_RAILWAY = os.getenv("RAILWAY_ENVIRONMENT") is not None
IS_RENDER = os.getenv("RENDER") is not None

# Get deployment URL from environment or use default
DEPLOY_URL = os.getenv("DEPLOY_URL", "")
FLY_APP_NAME = os.getenv("FLY_APP_NAME", "")
RAILWAY_PUBLIC_DOMAIN = os.getenv("RAILWAY_PUBLIC_DOMAIN", "")
RENDER_EXTERNAL_URL = os.getenv("RENDER_EXTERNAL_URL", "")

# Port configuration
if IS_PRODUCTION:
    # In production, use fixed ports that match your proxy configuration
    backend_port = int(os.getenv("BACKEND_PORT", "8000"))
    frontend_port = int(os.getenv("FRONTEND_PORT", "3000"))
    print(f"🚀 Production mode - Using backend port: {backend_port}, frontend port: {frontend_port}")
else:
    # In development, dynamically find available ports
    try:
        backend_port = find_available_port(8000)
        frontend_port = find_available_port(3000)
        print(f"✅ Development mode - Using backend port: {backend_port}, frontend port: {frontend_port}")
    except RuntimeError as e:
        print(f"⚠️  Warning: {e}")
        print("Falling back to default ports...")
        backend_port = 8000
        frontend_port = 3000

# URL configuration based on environment
if IS_FLY and FLY_APP_NAME:
    # Fly.io deployment
    deploy_url = f"https://{FLY_APP_NAME}.fly.dev"
    api_url = f"https://{FLY_APP_NAME}.fly.dev"
    print(f"🪰 Fly.io deployment detected: {deploy_url}")
elif IS_RAILWAY and RAILWAY_PUBLIC_DOMAIN:
    # Railway deployment
    deploy_url = f"https://{RAILWAY_PUBLIC_DOMAIN}"
    api_url = f"https://{RAILWAY_PUBLIC_DOMAIN}"
    print(f"🚂 Railway deployment detected: {deploy_url}")
elif IS_RENDER and RENDER_EXTERNAL_URL:
    # Render deployment
    deploy_url = RENDER_EXTERNAL_URL
    api_url = RENDER_EXTERNAL_URL
    print(f"🎨 Render deployment detected: {deploy_url}")
elif DEPLOY_URL:
    # Custom deployment URL provided
    deploy_url = DEPLOY_URL
    api_url = DEPLOY_URL
    print(f"🌐 Custom deployment URL: {deploy_url}")
elif IS_PRODUCTION:
    # Generic production - bind to all interfaces
    deploy_url = f"http://0.0.0.0:{frontend_port}"
    api_url = f"http://0.0.0.0:{backend_port}"
    print("🔧 Production mode with 0.0.0.0 binding")
else:
    # Local development
    deploy_url = f"http://localhost:{frontend_port}"
    api_url = f"http://localhost:{backend_port}"
    print("💻 Local development mode")

# CORS configuration
cors_origins = [
    f"http://localhost:{frontend_port}",
    f"http://127.0.0.1:{frontend_port}",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

# Add production URLs to CORS if in production
if IS_FLY and FLY_APP_NAME:
    cors_origins.extend([
        f"https://{FLY_APP_NAME}.fly.dev",
        f"http://{FLY_APP_NAME}.fly.dev",
    ])
elif IS_RAILWAY and RAILWAY_PUBLIC_DOMAIN:
    cors_origins.extend([
        f"https://{RAILWAY_PUBLIC_DOMAIN}",
        f"http://{RAILWAY_PUBLIC_DOMAIN}",
    ])
elif IS_RENDER and RENDER_EXTERNAL_URL:
    cors_origins.append(RENDER_EXTERNAL_URL)
elif DEPLOY_URL:
    cors_origins.append(DEPLOY_URL)

# Database configuration - use environment variable or default PostgreSQL
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://pandaflex_user:c8lHPEQ5jULajyLPnyytlQYTTo4d6Nth@dpg-d68gs406fj8s73c3rnsg-a.oregon-postgres.render.com/pandaflex"
)

# Verify PostgreSQL connection
try:
    test_conn = psycopg2.connect(DATABASE_URL)
    test_conn.close()
    print(f"✅ PostgreSQL connection successful")
except Exception as e:
    print(f"⚠️  PostgreSQL connection issue: {e}")
    print(f"   Using DATABASE_URL: {DATABASE_URL[:50]}...")

config = rx.Config(
    app_name="lmrex",

    # Database configuration
    db_url=DATABASE_URL,
    # Port configuration
    backend_port=backend_port,
    frontend_port=frontend_port,

    # URL configuration (environment-aware)
    api_url=api_url,
    deploy_url=deploy_url,

    # Host binding - 0.0.0.0 allows external connections
    backend_host="0.0.0.0",

    # CORS configuration
    cors_allowed_origins=cors_origins,
)
print(f"📊 Database: {config.db_url[:50]}...")

# Print configuration summary
print("=" * 60)
print(f"Environment: {'PRODUCTION' if IS_PRODUCTION else 'DEVELOPMENT'}")
print(f"Backend: {api_url}")
print(f"Frontend: {deploy_url}")
print(f"CORS Origins: {len(cors_origins)} configured")
print("=" * 60)
