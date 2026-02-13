# rxconfig.py
import reflex as rx
import socket


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


# Dynamically find available ports
try:
    backend_port = find_available_port(8000)
    frontend_port = find_available_port(3000)
    
    print(f"✅ Using backend port: {backend_port}")
    print(f"✅ Using frontend port: {frontend_port}")
except RuntimeError as e:
    print(f"⚠️  Warning: {e}")
    print("Falling back to default ports...")
    backend_port = 8000
    frontend_port = 3000


config = rx.Config(
    app_name="lmrex",
    
    # Dynamic port configuration
    backend_port=backend_port,
    frontend_port=frontend_port,
    api_url=f"http://localhost:{backend_port}",
    deploy_url=f"http://localhost:{frontend_port}",
    backend_host="0.0.0.0",
    
    # CORS - include dynamic frontend port
    cors_allowed_origins=[
        f"http://localhost:{frontend_port}",
        f"http://127.0.0.1:{frontend_port}",
        # Also allow default ports for compatibility
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    
    # Stylesheets
    stylesheets=[
        "assets/styles.css",
        "assets/styles/styles.css",
        ".web/styles/tailwind.css",
    ],
    
    # Plugins - temporarily disabled to avoid bun installation timeouts
    # Uncomment when you want to enable Tailwind V4
    # plugins=[
    #     rx.plugins.TailwindV4Plugin(),
    # ],
    
    # Disabled plugins
    disable_plugins=[
        "reflex.plugins.sitemap.SitemapPlugin",
    ],
)