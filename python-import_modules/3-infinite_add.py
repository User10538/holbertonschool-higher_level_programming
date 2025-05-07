#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg_total = 0
for i in range(1, len(sys.argv)):
    arg_total += int(sys.argv[i])
print(arg_total)
