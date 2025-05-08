#!/usr/bin/python3
import importlib.util
import sys
import os
if __name__ == "__main__":
    if len(sys.argv) >1 and sys.argv[1] == "bis":
        filepath = "/tmp/hidden_4_bis.pyc"
    else:
        filepath = "/tmp/hidden_4.pyc"


    spec = importlib.util.spec_from_file_location("hidden_4", filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    for name in sorted(dir(module)):
        if not name.startswith("__"):
            print(name)
