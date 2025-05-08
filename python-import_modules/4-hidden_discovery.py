#!/usr/bin/python3
import importlib.util
import sys
import os

if __name__ == "__main__":
    url = "https://github.com/hs-hq/0x02.py/raw/main/hidden_4.pyc"
    filepath = "/tmp/hidden_4.pyc"

    #download the file from website using curl
    os.system(f"curl -s -L -o {filepath} {url}")

    spec = importlib.util.spec_from_file_location("hidden_4", filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    for name in sorted(dir(module)):
        if not name.startswith("__"):
            print(name)
