#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1

    if argc == 0:
        print("0 arguments.")
    else:
        print(f"{argc} {'argument' if argc == 1 else 'arguments'}:")
        for i in range(1, argc + 1):
            print(f"{i}: {sys.argv[i]}")
