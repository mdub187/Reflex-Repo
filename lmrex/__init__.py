# from path import ROOT_DIR as ROOT_DIR
from .imports import os

# Get the absolute path of the current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

dir = f"{current_dir}/imports.py"

if __name__ == "__main__":
    print(dir)
