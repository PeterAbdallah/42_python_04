#!/usr/bin/env python3

def secure_archive(fname: str, operation: str | None = "read",
                   content: str | None = None) -> tuple[bool, str]:
    try:
        # READ
        if operation == "read":
            with open(fname, "r") as f:
                buffer = f.read()
            return (True, buffer)
        # WRITE
        elif operation == "write" and content is not None:
            with open(fname, "w") as f:
                f.write(content)
            return (True, "Content successfully written to file")
        else:
            return (False, "Invalid mode")
    except Exception as e:
        return (False, str(e))


def ft_vault_security() -> None:
    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/mnt/c/Windows/System32/config/SAM"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    t = secure_archive("test.txt")
    print(t)

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    if t[0]:
        print(secure_archive("test2.txt", "write", t[1]))


if __name__ == "__main__":
    ft_vault_security()
