import os
import re
import subprocess
import sys
import tomllib

BASE_PATH = os.getcwd()
TOML_PATH = 'tools/config.toml'


def toml_decorder():
  toml_path = os.path.join(BASE_PATH, TOML_PATH)
  with toml_path.open("rb") as f:
        return tomllib.load(f)

