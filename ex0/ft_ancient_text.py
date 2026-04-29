#!/usr/bin/env python3

import typing
import sys


def ft_ancient_text() -> None:
    print("=== Cyber Archives Recovery ===")
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    filename = sys.argv[1]
    print(f"Accessing file '{filename}'")
    try:
        f: typing.IO[str] = open(filename, "r")
        print("---\n")
        print(f.read())
        print("\n---")
        f.close()
        print(f"File '{filename}' closed.")
    except Exception as e:
        print(f"Error opening file '{filename}': {e}")
    # ACCESS DENIED PATH
    # /mnt/c/Windows/System32/config/SAM


if __name__ == "__main__":
    ft_ancient_text()
