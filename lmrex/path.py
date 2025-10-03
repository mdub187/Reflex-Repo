from imports import Path

# Get the path object for the current script
script_path = Path(__file__).resolve()

# Assuming the project root is two levels up from the script (e.g., if script is in 'src/sub_dir/')
ROOT_DIR = script_path.parent.parent
import_dir = f"{ROOT_DIR / 'imports.py'}"
