#!/usr/bin/env python3

import sys
import typing


def ft_stream_management() -> None:
    print("=== Cyber Archives Recovery & Preservation ===")
    if len(sys.argv) != 2:
        sys.stdout.write("Usage: ft_ancient_text.py <file>")
        return

    filename = sys.argv[1]
    print(f"Accessing file '{filename}'")
    try:
        f: typing.IO[str] = open(filename, "r")
        content = f.read()
        lines = content.splitlines()
        print("---\n")
        print(content)
        print("\n---")
        f.close()
        print(f"File '{filename}' closed.")
    except Exception as e:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
        return
    # ACCESS DENIED PATH
    # /mnt/c/Windows/System32/config/SAM

    new_content = ""
    print("\nTransform data:")
    print("---\n")
    for line in lines:
        new_line = line + "#"
        print(new_line)
        new_content += new_line + "\n"
    print("\n---")

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_file = sys.stdin.readline().strip()

    if new_file == "":
        print("Not saving data.")
    else:
        try:
            f2 = open(new_file, "w")
            f2.write(new_content)
            f2.close()
            print(f"Saving data to '{new_file}'")
            print(f"Data saved in file '{new_file}'.")
        except Exception as e:
            sys.stderr.write(f"[STDERR] Error opening file\
 '{new_file}': {e}\n")
            sys.stderr.write("Data not saved.\n")


if __name__ == "__main__":
    ft_stream_management()
