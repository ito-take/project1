import argparse
import os
import re
import subprocess
import sys
import tomllib

BASE_PATH = os.getcwd()
TOML_PATH = 'config/config.toml'
WORKFLOWS_PATH = '.github/workflows'
SCRIPT_PATH = 'script'

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-t", "--target",
        required=False
    )

    parser.add_argument(
        "-m", "--mode",
        required=False
    )

    parser.add_argument(
        "-v", "--version",
        required=False
    )

    parser.add_argument(
        "-wt", "--workflow_target",
        required=False
    )

    return parser.parse_args()

def toml_decorder():
    toml_path = os.path.join(BASE_PATH, os.path.normpath(TOML_PATH))

    with open(toml_path, "rb") as f:
        return tomllib.load(f)

def main():
    args = parse_args()
    toml = toml_decorder()
    
    
    
    
if __name__ == "__main__":
    main()