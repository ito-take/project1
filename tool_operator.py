import os
import re
import subprocess
import sys
import tomllib

BASE_PATH = os.getcwd()
TOML_PATH = 'config/config.toml'


def toml_decorder():
  toml_path = os.path.join(BASE_PATH, os.path.normpath(TOML_PATH))

  with open(toml_path, "rb") as f:
        return tomllib.load(f)

def main():
    toml = toml_decorder()
    print(toml)


if __name__ == "__main__":
    main()