_This project has been created as part of the 42 curriculum by pabdalla_

# Data Archivist - Digital Preservation in the Cyber Archives

## Evaluator Instructions

### Running the scripts
Replace with necessary values
```bash
python3 {exercise.py} [file]
# or directly if the shebang is set:
./{exercise_path.py} [file]
```

### Checking code standards
```bash
flake8      # style linter
mypy ./     # type checker
```

---

## Overview

This project teaches file I/O operations in Python through a series of progressive exercises
set in a cyberpunk archival system. Starting from basic file reading and advancing through
writing, data transformation, stream management, and safe context-managed file access,
each exercise builds directly on the previous one, forming a complete file handling pipeline
by the end.

---

## Concepts Covered

- Reading files with `open()`, `.read()`, and `.close()`
- Writing and overwriting files with `open()` in write mode and `.write()`
- Transforming file content in-memory before saving
- Reading user input from `sys.stdin` directly (without `input()`)
- Routing error messages to `sys.stderr` instead of `sys.stdout`
- Using `.readline()` and `.flush()` on standard streams
- Managing file resources safely with the `with` statement (context manager)
- Returning structured results from functions using tuples
- Handling file-related exceptions (`FileNotFoundError`, `PermissionError`, etc.)
- Type hints with `typing.IO` and `mypy` compliance

---

## Key Python Concepts

### File Opening and Modes
- `open(filename, mode)` returns a file object (`typing.IO`)
- Common modes: `"r"` for reading (default), `"w"` for writing (creates or overwrites)
- Always close files after use with `.close()` — or use `with` to do it automatically
- `open()` raises `FileNotFoundError` if the file doesn't exist, and `PermissionError` if access is denied

### Reading Files
- `.read()` returns the entire file contents as a single string
- `.readline()` reads one line at a time — useful for processing streams incrementally
- The file must be closed after reading to release the system resource

### Writing Files
- Opening a file in `"w"` mode creates it if it doesn't exist and **truncates** it if it does
- `.write(content)` writes a string to the file — no automatic newline is added
- Always ensure the file is closed (or the `with` block ends) before the data is fully flushed to disk

### Standard Streams
- `sys.stdin` — the standard input stream; `.readline()` reads one line without needing `input()`
- `sys.stdout` — the standard output stream; used by `print()` by default
- `sys.stderr` — the standard error stream; error messages should go here, not to stdout
- `sys.stdout.flush()` / `sys.stderr.flush()` — force buffered output to be written immediately

### The `with` Statement (Context Manager)
- `with open(filename) as f:` automatically closes the file when the block exits
- The file is closed even if an exception is raised inside the block — no need for `finally`
- This is the preferred and safest way to handle files in Python
- Before exercise 3, `with` must **not** be used, manual `.close()` is required

### Returning Results as Tuples
- Functions can return multiple values packed in a tuple: `return (True, content)`
- The caller can unpack them: `success, result = secure_archive(filename)`
- Using `(bool, str)` as a return type is a clean pattern for signalling success/failure alongside a message

---

## Exercise Summary

| Exercise | File | Concepts |
|----------|------|----------|
| 0 | `ex0/ft_ancient_text.py` | `open()`, `.read()`, `.close()`, error handling, `sys.argv` |
| 1 | `ex1/ft_archive_creation.py` | Writing files, transforming content, `input()`, write mode |
| 2 | `ex2/ft_stream_management.py` | `sys.stdin`, `sys.stdout`, `sys.stderr`, `.readline()`, `.flush()` |
| 3 | `ex3/ft_vault_security.py` | `with` statement, context managers, tuple return values |

---