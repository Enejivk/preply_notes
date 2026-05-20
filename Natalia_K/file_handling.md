# Python File Handling — Complete Study Notes

> **A comprehensive guide covering every aspect of file handling in Python, from the very basics to advanced concepts, with detailed explanations and practical examples.**

---

## Table of Contents

0. [Linux Commands — The Python Way](#0-linux-commands--the-python-way)
1. [Introduction to File Handling](#1-introduction-to-file-handling)
2. [Understanding Files and Paths](#2-understanding-files-and-paths)
3. [Opening and Closing Files](#3-opening-and-closing-files)
4. [Using Context Managers (with Statement)](#4-using-context-managers-with-statement)
5. [Reading Files](#5-reading-files)
6. [Writing to Files](#6-writing-to-files)
7. [Appending to Files](#7-appending-to-files)
8. [Working with File Cursor and Position](#8-working-with-file-cursor-and-position)
9. [Handling File Errors and Exceptions](#9-handling-file-errors-and-exceptions)
10. [Working with Binary Files](#10-working-with-binary-files)
11. [File and Directory Management with os](#11-file-and-directory-management-with-os)
12. [Using the pathlib Module](#12-using-the-pathlib-module)
13. [Working with CSV Files](#13-working-with-csv-files)
14. [Working with JSON Files](#14-working-with-json-files)
15. [Working with User Input and Files](#15-working-with-user-input-and-files)
16. [File Compression Basics](#16-file-compression-basics)
17. [Temporary Files](#17-temporary-files)
18. [Advanced File Handling Concepts](#18-advanced-file-handling-concepts)
19. [Best Practices in File Handling](#19-best-practices-in-file-handling)
20. [Practical Mini Projects](#20-practical-mini-projects)
21. [Final Capstone Projects](#21-final-capstone-projects)
22. [Bonus: Additional Topics](#22-bonus-additional-topics)

---

## 0. Linux Commands — The Python Way

> Before writing a single line of file handling code, you need to be comfortable with one idea: **the file system**. If you've used Linux or a terminal before, you already know commands like `pwd`, `ls`, `mkdir`, `cd`, `rm`, `cp`, and `mv`. This section shows you how to do everything those commands do — entirely in Python. This is your foundation. Everything in the rest of this guide builds on it.

---

### `pwd` — Print Working Directory

In the terminal: `pwd` tells you where you currently are.

In Python, use `os.getcwd()` or `Path.cwd()`:

```python
import os
from pathlib import Path

# os way
print(os.getcwd())
# Output: /home/user/projects

# pathlib way (modern, preferred)
print(Path.cwd())
# Output: /home/user/projects
```

---

### `ls` — List Directory Contents

In the terminal: `ls` lists files and folders. `ls -la` shows hidden files and details.

In Python:

```python
import os
from pathlib import Path

# List everything in the current directory
print(os.listdir("."))
# ['notes.txt', 'data', 'script.py', ...]

# pathlib way — iterdir() gives Path objects
for item in Path(".").iterdir():
    print(item)

# List ONLY files
for item in Path(".").iterdir():
    if item.is_file():
        print(item.name)

# List ONLY directories
for item in Path(".").iterdir():
    if item.is_dir():
        print(item.name)

# Like ls -la: show name, size, type
for item in Path(".").iterdir():
    kind = "FILE" if item.is_file() else "DIR "
    size = item.stat().st_size if item.is_file() else "-"
    print(f"[{kind}]  {str(size):>10}  {item.name}")

# List only .txt files (like ls *.txt)
for f in Path(".").glob("*.txt"):
    print(f.name)

# Recursive listing (like ls -R or find .)
for f in Path(".").rglob("*"):
    print(f)
```

---

### `cd` — Change Directory

In the terminal: `cd foldername` moves into a folder. `cd ..` goes up one level. `cd ~` goes home.

In Python:

```python
import os
from pathlib import Path

# Move into a folder
os.chdir("projects")
print(os.getcwd())   # /home/user/projects

# Go up one level (cd ..)
os.chdir("..")
print(os.getcwd())   # /home/user

# Go to home directory (cd ~)
os.chdir(Path.home())
print(os.getcwd())   # /home/user

# Go to an absolute path
os.chdir("/var/log")

# Best practice: always return to original dir after changing
original = os.getcwd()
os.chdir("some_folder")
# ... do work ...
os.chdir(original)   # Go back
```

> **Important:** `os.chdir()` changes the working directory for the **entire Python process**. If you're writing functions or scripts used by others, be careful — changing the CWD inside a function can have unexpected side effects. Prefer building full paths with `pathlib` instead of relying on `cd`.

---

### `mkdir` — Make Directory

In the terminal: `mkdir myfolder` creates a folder. `mkdir -p a/b/c` creates nested folders.

In Python:

```python
import os
from pathlib import Path

# Create a single directory (os way)
os.mkdir("reports")

# Create nested directories (like mkdir -p)
os.makedirs("data/raw/2024", exist_ok=True)
# exist_ok=True means: don't raise an error if it already exists

# pathlib way (clean and modern)
Path("output/charts").mkdir(parents=True, exist_ok=True)

# Create multiple folders at once
folders = ["data", "output", "logs", "config"]
for folder in folders:
    Path(folder).mkdir(exist_ok=True)
    print(f"Created: {folder}/")
```

---

### `touch` — Create an Empty File

In the terminal: `touch filename.txt` creates an empty file or updates its timestamp.

In Python:

```python
from pathlib import Path

# Create an empty file (pathlib way)
Path("notes.txt").touch()

# Create a file only if it doesn't exist
Path("important.txt").touch(exist_ok=True)

# os way — open for writing and immediately close
open("newfile.txt", "w").close()

# Create multiple empty files
files = ["readme.txt", "config.json", "data.csv"]
for filename in files:
    Path(filename).touch()
    print(f"Created: {filename}")
```

---

### `cp` — Copy Files and Directories

In the terminal: `cp source.txt destination.txt` copies a file. `cp -r folder/ backup/` copies a whole folder.

In Python, use `shutil`:

```python
import shutil
from pathlib import Path

# Copy a file
shutil.copy("source.txt", "destination.txt")

# Copy file AND preserve metadata (timestamps, permissions)
shutil.copy2("source.txt", "destination.txt")

# Copy into a folder (keeps original filename)
shutil.copy("report.txt", "archive/")
# Result: archive/report.txt

# Copy an entire folder (like cp -r)
shutil.copytree("my_project", "my_project_backup")

# Copy with pathlib paths
src = Path("data/input.csv")
dst = Path("backup/input.csv")
dst.parent.mkdir(parents=True, exist_ok=True)
shutil.copy2(src, dst)
```

---

### `mv` — Move or Rename Files

In the terminal: `mv old.txt new.txt` renames a file. `mv file.txt folder/` moves it.

In Python:

```python
import os
import shutil
from pathlib import Path

# Rename a file (os way)
os.rename("old_name.txt", "new_name.txt")

# Move a file to a different folder
shutil.move("report.txt", "archive/report.txt")

# Move an entire folder
shutil.move("temp_folder", "old/temp_folder")

# pathlib way — rename in the same directory
p = Path("draft.txt")
p.rename(p.parent / "final.txt")

# pathlib way — move to another directory
Path("notes.txt").rename(Path("documents/notes.txt"))
```

---

### `rm` — Remove Files and Directories

In the terminal: `rm file.txt` deletes a file. `rm -r folder/` deletes a folder and everything in it.

In Python:

```python
import os
import shutil
from pathlib import Path

# Delete a single file
os.remove("unwanted.txt")

# pathlib way
Path("unwanted.txt").unlink()

# Delete an EMPTY directory (like rmdir)
os.rmdir("empty_folder")
Path("empty_folder").rmdir()

# Delete a folder and ALL its contents (like rm -rf) — IRREVERSIBLE!
shutil.rmtree("old_project")

# Safe delete — check before removing
def safe_delete(path):
    p = Path(path)
    if p.is_file():
        p.unlink()
        print(f"Deleted file: {path}")
    elif p.is_dir():
        shutil.rmtree(p)
        print(f"Deleted directory: {path}")
    else:
        print(f"Not found: {path}")

safe_delete("temp.txt")
safe_delete("cache/")

# Delete all .log files in a folder
for log_file in Path("logs").glob("*.log"):
    log_file.unlink()
    print(f"Removed: {log_file.name}")
```

---

### `find` — Search for Files

In the terminal: `find . -name "*.txt"` finds all `.txt` files. `find . -type d` finds all directories.

In Python:

```python
from pathlib import Path
import os

# Find all .txt files recursively (like find . -name "*.txt")
for f in Path(".").rglob("*.txt"):
    print(f)

# Find all directories (like find . -type d)
for p in Path(".").rglob("*"):
    if p.is_dir():
        print(p)

# Find all files (like find . -type f)
for p in Path(".").rglob("*"):
    if p.is_file():
        print(p)

# Find files larger than 1MB
for p in Path(".").rglob("*"):
    if p.is_file() and p.stat().st_size > 1_000_000:
        print(f"{p}  ({p.stat().st_size // 1024} KB)")

# Find files by name (case-insensitive)
target = "config"
for p in Path(".").rglob("*"):
    if target.lower() in p.name.lower():
        print(p)

# os.walk version (older but still common)
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".py"):
            print(os.path.join(root, file))
```

---

### `cat` — Display File Contents

In the terminal: `cat file.txt` prints the contents of a file.

In Python:

```python
from pathlib import Path

# Print entire file (like cat)
print(Path("notes.txt").read_text())

# With line numbers (like cat -n)
with open("notes.txt", "r") as f:
    for i, line in enumerate(f, 1):
        print(f"{i:>4}  {line}", end="")

# Concatenate multiple files (that's what cat stands for!)
files = ["part1.txt", "part2.txt", "part3.txt"]
with open("combined.txt", "w") as out:
    for filename in files:
        out.write(Path(filename).read_text())
        out.write("\n")
```

---

### `chmod` — Change File Permissions

In the terminal: `chmod 755 script.py` sets permissions. `chmod +x script.py` makes it executable.

In Python:

```python
import os
import stat
from pathlib import Path

# Make a file executable (chmod +x)
path = "script.py"
current = os.stat(path).st_mode
os.chmod(path, current | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

# Set specific permission (chmod 644 — owner rw, group r, others r)
os.chmod("data.txt", stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)

# Check permissions
p = Path("script.py")
mode = p.stat().st_mode
print(f"Readable:   {bool(mode & stat.S_IRUSR)}")
print(f"Writable:   {bool(mode & stat.S_IWUSR)}")
print(f"Executable: {bool(mode & stat.S_IXUSR)}")

# os.access() — simpler permission check
print(os.access("data.txt", os.R_OK))  # Can we read?
print(os.access("data.txt", os.W_OK))  # Can we write?
print(os.access("script.py", os.X_OK)) # Can we execute?
```

---

### `du` / `df` — Disk Usage

In the terminal: `du -sh folder/` shows folder size. `df -h` shows disk space.

In Python:

```python
import shutil
import os
from pathlib import Path

# Disk space (like df -h)
usage = shutil.disk_usage("/")
print(f"Total : {usage.total / (1024**3):.1f} GB")
print(f"Used  : {usage.used  / (1024**3):.1f} GB")
print(f"Free  : {usage.free  / (1024**3):.1f} GB")

# Single file size (like ls -lh)
size = Path("video.mp4").stat().st_size
print(f"File size: {size / (1024**2):.2f} MB")

# Folder size (like du -sh folder/)
def folder_size(path):
    total = 0
    for f in Path(path).rglob("*"):
        if f.is_file():
            total += f.stat().st_size
    return total

size = folder_size("my_project")
print(f"Folder size: {size / 1024:.1f} KB")
```

---

### Quick Reference: Linux Command → Python Equivalent

| Linux Command | Python Equivalent |
|---------------|------------------|
| `pwd` | `os.getcwd()` / `Path.cwd()` |
| `ls` | `os.listdir()` / `Path.iterdir()` |
| `ls *.txt` | `Path(".").glob("*.txt")` |
| `ls -R` | `Path(".").rglob("*")` |
| `cd folder` | `os.chdir("folder")` |
| `mkdir folder` | `os.mkdir()` / `Path.mkdir()` |
| `mkdir -p a/b/c` | `os.makedirs(exist_ok=True)` / `Path.mkdir(parents=True)` |
| `touch file.txt` | `Path("file.txt").touch()` |
| `cp src dst` | `shutil.copy(src, dst)` |
| `cp -r src dst` | `shutil.copytree(src, dst)` |
| `mv old new` | `os.rename()` / `Path.rename()` / `shutil.move()` |
| `rm file` | `os.remove()` / `Path.unlink()` |
| `rmdir folder` | `os.rmdir()` / `Path.rmdir()` |
| `rm -rf folder` | `shutil.rmtree(folder)` |
| `find . -name "*.py"` | `Path(".").rglob("*.py")` |
| `cat file.txt` | `Path("file.txt").read_text()` |
| `chmod +x file` | `os.chmod(file, mode)` |
| `df -h` | `shutil.disk_usage(path)` |
| `du -sh folder` | custom `folder_size()` function |

---

### Project: Build a Python File System Explorer

**Problem Statement:**

You are going to build a command-line **File System Explorer** in Python — a program that lets a user navigate and manage their file system using a simple menu, without ever touching the terminal directly. Every action the user takes will be done through Python's `os`, `pathlib`, and `shutil` modules.

**What the program must do:**

The program runs in a loop and shows the user a menu. The user picks an option and the program executes it. The current working directory is always shown so the user knows where they are.

**Features to implement:**

1. **Show current location** — display the CWD (like `pwd`)
2. **List contents** — list all files and folders in the current directory with their type and size (like `ls -lh`)
3. **Change directory** — let the user type a folder name to move into it, or `..` to go up (like `cd`)
4. **Create a folder** — ask for a name and create it (like `mkdir`)
5. **Create a file** — ask for a filename and create an empty file (like `touch`)
6. **Delete a file or folder** — ask for a name and safely delete it (like `rm` / `rm -rf`)
7. **Rename / Move** — ask for old and new name (like `mv`)
8. **Search** — let the user type a pattern (e.g., `*.txt`) and find all matching files recursively (like `find`)
9. **Show file contents** — let user type a filename and print its contents (like `cat`)
10. **Show disk usage** — display how much disk space is available (like `df -h`)
11. **Exit**

**Requirements:**

- Wrap all operations in `try/except` so the program never crashes on bad input
- Always show the current directory in the prompt
- Confirm before deleting anything
- Display file sizes in human-readable format (KB, MB, GB)

**Starter structure:**

```python
import os
import shutil
from pathlib import Path

def format_size(size_bytes):
    """Convert bytes to human-readable string."""
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size_bytes < 1024:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f} PB"

def show_location():
    print(f"\n📁 Current directory: {Path.cwd()}")

def list_contents():
    # TODO: iterate Path.cwd(), show name, type, size
    pass

def change_directory():
    # TODO: ask for folder name, os.chdir(), handle errors
    pass

def create_folder():
    # TODO: ask for name, Path.mkdir()
    pass

def create_file():
    # TODO: ask for filename, Path.touch()
    pass

def delete_item():
    # TODO: ask for name, confirm, then os.remove() or shutil.rmtree()
    pass

def rename_item():
    # TODO: ask for old and new name, Path.rename()
    pass

def search_files():
    # TODO: ask for pattern, Path.cwd().rglob(pattern)
    pass

def show_file_contents():
    # TODO: ask for filename, read and print it
    pass

def show_disk_usage():
    # TODO: shutil.disk_usage(Path.cwd())
    pass

def main():
    while True:
        show_location()
        print("\n--- File System Explorer ---")
        print("1. List contents")
        print("2. Change directory")
        print("3. Create folder")
        print("4. Create file")
        print("5. Delete item")
        print("6. Rename / Move item")
        print("7. Search files")
        print("8. Show file contents")
        print("9. Disk usage")
        print("0. Exit")

        choice = input("\nChoose an option: ").strip()

        actions = {
            "1": list_contents,
            "2": change_directory,
            "3": create_folder,
            "4": create_file,
            "5": delete_item,
            "6": rename_item,
            "7": search_files,
            "8": show_file_contents,
            "9": show_disk_usage,
        }

        if choice == "0":
            print("Goodbye!")
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
```

**Your challenge:** Fill in every `pass` with real code using the Python equivalents you learned in this section. When you're done, you'll have a fully working file manager built entirely in Python.

---

## 1. Introduction to File Handling

### What File Handling Means

File handling refers to the ability of a program to **create, read, update, and delete** files stored on a computer's disk. In Python, this is done through built-in functions and modules that let you interact with the file system in a controlled, systematic way.

Think of a file as a container on your hard drive — it holds data that survives even after your program closes. File handling is how your program reaches into that container.

### Why File Handling Is Important

Without file handling, every program would lose all its data the moment it stopped running. File handling solves this by giving programs **persistent storage** — a way to save, retrieve, and modify data between sessions.

Key reasons it matters:

- **Data persistence**: Save results so they're available next time the program runs
- **Data sharing**: Files let different programs (and even different machines) exchange information
- **Logging**: Track what a program did, when, and what errors occurred
- **Configuration**: Store settings that users can change without modifying the source code
- **Automation**: Process large volumes of data stored in files

### Real-World Use Cases of Files

- A school management system storing student grades in a CSV file
- A web server logging each request to a log file
- A desktop application reading its settings from a JSON or INI file
- A data pipeline reading thousands of records from a text file and writing results to another
- A photo editor reading image data from a binary file
- A bank application writing transaction records to a file for auditing

### Types of Files

#### Text Files

Text files store data as **human-readable characters**. Each character is encoded (usually in UTF-8 or ASCII) as a sequence of bytes. You can open text files in any text editor and read them.

Examples: `.txt`, `.csv`, `.json`, `.xml`, `.html`, `.py`

```python
# A simple text file might look like this internally:
# Hello, World!\n
# This is line two.\n
```

#### Binary Files

Binary files store data in **raw bytes** that are not necessarily human-readable. They are designed to be interpreted by specific software.

Examples: `.jpg`, `.png`, `.mp3`, `.pdf`, `.exe`, `.docx`

```python
# A binary file's raw bytes might look like:
# b'\xff\xd8\xff\xe0\x00\x10JFIF...'  (a JPEG image)
```

---

## 2. Understanding Files and Paths

### What Is a File

A **file** is a named collection of data stored on a storage medium (hard drive, SSD, etc.). Every file has:

- A **name** (e.g., `report.txt`)
- An **extension** that hints at its type (e.g., `.txt`)
- **Content** — the actual data
- **Metadata** — creation date, size, permissions, etc.

### File Extensions

A file extension is the suffix after the last dot in a filename. It is a convention that indicates the file format.

| Extension | Meaning |
|-----------|---------|
| `.txt` | Plain text |
| `.py` | Python source code |
| `.csv` | Comma-Separated Values |
| `.json` | JavaScript Object Notation |
| `.jpg` / `.png` | Image files |
| `.pdf` | Portable Document Format |
| `.mp4` | Video file |

> Note: Extensions are not enforced by most operating systems — a file named `photo.txt` could actually contain binary image data. Python cares about how you open the file (text vs binary mode), not the extension.

### Absolute vs Relative Paths

#### Absolute Path

An **absolute path** is the full path from the root of the file system to the file. It is the same regardless of where your Python script is located.

```
Windows:  C:\Users\John\Documents\notes.txt
Linux:    /home/john/documents/notes.txt
macOS:    /Users/john/Documents/notes.txt
```

#### Relative Path

A **relative path** is defined relative to the **current working directory** (CWD) — the folder your script is running from.

If your CWD is `/home/john/` and the file is at `/home/john/documents/notes.txt`, the relative path is:

```
documents/notes.txt
```

Or if the file is in the same folder:

```
notes.txt
```

```python
# Absolute path
file = open("/home/john/documents/notes.txt", "r")

# Relative path (assumes CWD contains 'documents' folder)
file = open("documents/notes.txt", "r")
```

### Working Directory

The **working directory** is the folder Python treats as the starting point for relative paths. You can check and change it with the `os` module.

```python
import os

# Check current working directory
print(os.getcwd())  # e.g., /home/john/projects

# Change working directory
os.chdir("/home/john/documents")
print(os.getcwd())  # /home/john/documents
```

### File Locations in Different Operating Systems

| OS | Root | Path Separator | Home |
|----|------|---------------|------|
| Windows | `C:\` | `\` (backslash) | `C:\Users\username` |
| Linux | `/` | `/` (forward slash) | `/home/username` |
| macOS | `/` | `/` (forward slash) | `/Users/username` |

In Python, always use forward slashes `/` or raw strings `r"C:\path"` for Windows paths, or use the `pathlib` module which handles all OS differences automatically.

```python
# Safe cross-platform path handling
import os
path = os.path.join("folder", "subfolder", "file.txt")
# Windows: folder\subfolder\file.txt
# Linux:   folder/subfolder/file.txt
```

---

## 3. Opening and Closing Files

### The `open()` Function

The `open()` function is Python's built-in gateway to the file system. It opens a file and returns a **file object** (also called a file handle) that you use to read from or write to the file.

```python
file_object = open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
```

### File Syntax and Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `file` | Path to the file (string or path-like object) | Required |
| `mode` | How to open the file | `'r'` |
| `buffering` | Buffering policy | `-1` (system default) |
| `encoding` | Character encoding (text mode only) | Platform default |
| `errors` | How to handle encoding errors | `'strict'` |
| `newline` | How to handle newlines | `None` |

```python
# Basic usage
f = open("hello.txt", "r")
content = f.read()
f.close()
```

### File Modes

#### `r` — Read (default)

Opens the file for **reading only**. The file must already exist. The cursor starts at the beginning.

```python
f = open("data.txt", "r")
print(f.read())
f.close()
```

#### `w` — Write

Opens the file for **writing**. If the file exists, it is **completely overwritten**. If it doesn't exist, Python creates it.

```python
f = open("data.txt", "w")
f.write("Hello!")  # Overwrites everything that was in data.txt
f.close()
```

#### `a` — Append

Opens the file for **appending**. New data is written at the **end** of the file. If the file doesn't exist, Python creates it.

```python
f = open("log.txt", "a")
f.write("New log entry\n")  # Does NOT erase existing content
f.close()
```

#### `x` — Exclusive Creation

Creates a **new file** for writing. Raises a `FileExistsError` if the file already exists. This is a safety mode.

```python
try:
    f = open("newfile.txt", "x")
    f.write("Created fresh!")
    f.close()
except FileExistsError:
    print("File already exists!")
```

#### `b` — Binary Mode

Used in combination with other modes. Tells Python to handle the file as raw bytes instead of text.

```python
f = open("image.jpg", "rb")  # Read binary
data = f.read()
f.close()

f = open("copy.jpg", "wb")  # Write binary
f.write(data)
f.close()
```

#### `t` — Text Mode (default)

The default mode. Python decodes bytes to strings using the specified (or default) encoding.

```python
f = open("notes.txt", "rt")  # Same as "r"
```

#### `+` — Read and Write

Combines reading and writing. Must be combined with another mode.

| Mode | Meaning |
|------|---------|
| `r+` | Read and write; file must exist; cursor at start |
| `w+` | Write and read; overwrites file; creates if missing |
| `a+` | Append and read; cursor at end for writes |

```python
# r+ example: read then modify
f = open("data.txt", "r+")
content = f.read()
f.seek(0)         # Go back to beginning
f.write("NEW")    # Overwrite the first 3 chars
f.close()
```

### Closing Files with `close()`

After you're done with a file, you **must** close it. Closing releases the OS resources (file descriptor) and ensures all buffered data is **flushed** (written) to disk.

```python
f = open("data.txt", "r")
content = f.read()
f.close()  # Always close!

# Check if file is closed
print(f.closed)  # True
```

**Why closing matters:**

- Prevents memory leaks
- Prevents data corruption (unflushed buffers)
- Prevents "too many open files" errors
- Allows other programs to access the file

---

## 4. Using Context Managers (`with` Statement)

### What Context Managers Are

A **context manager** is an object that manages the setup and teardown of a resource. For files, it means: automatically opening the file when you enter the `with` block, and **automatically closing it** when you exit — even if an error occurs.

### Why `with open()` Is Preferred

The traditional approach of `open()` + `close()` has a critical flaw: if an exception occurs between `open()` and `close()`, the file never gets closed.

```python
# RISKY: What if an error happens on this line?
f = open("data.txt", "r")
content = f.read()  # <-- If this crashes, f.close() is never called!
f.close()
```

With `with`, the file is **always closed**, no matter what:

```python
# SAFE: File is always closed
with open("data.txt", "r") as f:
    content = f.read()
# f is automatically closed here, even if an error occurred above
```

### Automatic Resource Management

The `with` statement uses two special methods internally:
- `__enter__()` — called when entering the block (opens the file)
- `__exit__()` — called when leaving the block (closes the file)

```python
# You can open multiple files at once in one with statement
with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    data = infile.read()
    outfile.write(data.upper())
# Both files are closed here automatically
```

### Preventing Memory Leaks

Every open file holds an OS-level **file descriptor** — a numbered slot. Most systems have a limit (e.g., 1024 open files per process). Forgetting to close files causes **file descriptor leaks**, which can crash long-running programs.

```python
# BAD: In a loop, this can exhaust file descriptors
for i in range(10000):
    f = open(f"file_{i}.txt", "w")
    f.write("data")
    # Never closed!

# GOOD: Context manager ensures each is closed immediately
for i in range(10000):
    with open(f"file_{i}.txt", "w") as f:
        f.write("data")
```

---

## 5. Reading Files

### `read()`

Reads the **entire file** as a single string. Optionally accepts a `size` argument to read a specific number of characters.

```python
with open("story.txt", "r") as f:
    content = f.read()       # Read entire file
    print(content)

with open("story.txt", "r") as f:
    chunk = f.read(100)      # Read first 100 characters
    print(chunk)
```

> **Warning:** Avoid `read()` on very large files — it loads everything into RAM at once.

### `readline()`

Reads **one line at a time**, including the newline character `\n`. Returns an empty string `""` when the end of file is reached.

```python
with open("poem.txt", "r") as f:
    first_line = f.readline()   # "Roses are red\n"
    second_line = f.readline()  # "Violets are blue\n"
    print(first_line.strip())   # Strip removes the \n
    print(second_line.strip())
```

Looping with `readline()`:

```python
with open("data.txt", "r") as f:
    line = f.readline()
    while line:
        print(line.strip())
        line = f.readline()
```

### `readlines()`

Reads **all lines** and returns them as a **list of strings**. Each string includes the `\n` at the end.

```python
with open("students.txt", "r") as f:
    lines = f.readlines()
    # lines = ["Alice\n", "Bob\n", "Charlie\n"]
    for name in lines:
        print(name.strip())
```

### Reading Specific Characters

```python
with open("alphabet.txt", "r") as f:
    f.seek(5)          # Jump to position 5
    chars = f.read(3)  # Read 3 characters from position 5
    print(chars)       # e.g., "fgh"
```

### Looping Through File Contents

The most **Pythonic** and memory-efficient way to read a file line by line is to loop directly over the file object:

```python
with open("large_file.txt", "r") as f:
    for line in f:           # Iterates one line at a time
        print(line.strip())  # No need to call readline()
```

Python's file object is an **iterator** — it reads one line at a time from disk, keeping only that line in memory.

### Reading Large Files Efficiently

For very large files (gigabytes), reading everything at once will crash your program. Use chunked reading:

```python
# Method 1: Line-by-line iteration (best for text files)
with open("huge_log.txt", "r") as f:
    for line in f:
        process(line)

# Method 2: Read in chunks (good for binary or text)
CHUNK_SIZE = 1024 * 1024  # 1 MB chunks

with open("massive_file.txt", "r") as f:
    while True:
        chunk = f.read(CHUNK_SIZE)
        if not chunk:
            break
        process(chunk)

# Method 3: islice — read only first N lines
from itertools import islice

with open("bigfile.txt", "r") as f:
    for line in islice(f, 100):  # Read only first 100 lines
        print(line.strip())
```

---

## 6. Writing to Files

### `write()`

Writes a **single string** to the file. Returns the number of characters written. Does **not** automatically add a newline.

```python
with open("output.txt", "w") as f:
    f.write("Hello, World!")    # 13 characters written
    f.write("\nSecond line.")   # Must add \n manually
```

### `writelines()`

Writes a **list of strings** to the file. Like `write()`, it does NOT add newlines between items — you must include them in the strings.

```python
lines = ["Alice\n", "Bob\n", "Charlie\n"]

with open("names.txt", "w") as f:
    f.writelines(lines)
```

Or using a list comprehension:

```python
names = ["Alice", "Bob", "Charlie"]

with open("names.txt", "w") as f:
    f.writelines(name + "\n" for name in names)
```

### Overwriting File Contents

Opening a file in `"w"` mode always **erases existing content** before writing:

```python
# First run: file gets "Hello"
with open("data.txt", "w") as f:
    f.write("Hello")

# Second run: "Hello" is GONE, file now contains "World"
with open("data.txt", "w") as f:
    f.write("World")
```

### Creating New Files

`"w"` and `"a"` modes both create a file if it doesn't exist. Use `"x"` if you want to guarantee you're not overwriting an existing file.

```python
# Creates new file (or overwrites existing)
with open("new_file.txt", "w") as f:
    f.write("Brand new content")

# Safe creation - fails if file already exists
try:
    with open("important.txt", "x") as f:
        f.write("This will not overwrite anything")
except FileExistsError:
    print("important.txt already exists — not overwriting!")
```

### Formatting Written Content

```python
# Writing structured data
students = [
    {"name": "Alice", "grade": 92},
    {"name": "Bob", "grade": 85},
    {"name": "Charlie", "grade": 78},
]

with open("grades.txt", "w") as f:
    f.write("Student Report\n")
    f.write("=" * 30 + "\n")
    for s in students:
        line = f"{s['name']:<15} {s['grade']:>3}\n"
        f.write(line)
    f.write("=" * 30 + "\n")
```

Output in file:
```
Student Report
==============================
Alice            92
Bob              85
Charlie          78
==============================
```

---

## 7. Appending to Files

### Append Mode (`a`)

Append mode opens the file with the cursor positioned at the **end**, so all new writes are added after existing content. The file is created if it doesn't exist.

```python
# Day 1
with open("diary.txt", "a") as f:
    f.write("Day 1: Started the project.\n")

# Day 2 — Day 1's content is still there!
with open("diary.txt", "a") as f:
    f.write("Day 2: Made good progress.\n")

# diary.txt now contains both lines
```

### Difference Between Write and Append

| Feature | `"w"` Write Mode | `"a"` Append Mode |
|---------|-----------------|------------------|
| Existing content | **Erased** | **Preserved** |
| Cursor position | Beginning | End |
| File creation | Yes | Yes |
| Use case | Start fresh | Add to existing data |

```python
# WRITE — erases first
with open("test.txt", "w") as f:
    f.write("Line 1\n")
with open("test.txt", "w") as f:
    f.write("Line 2\n")
# File contains ONLY: "Line 2\n"

# APPEND — preserves all
with open("test.txt", "a") as f:
    f.write("Line 1\n")
with open("test.txt", "a") as f:
    f.write("Line 2\n")
# File contains: "Line 1\nLine 2\n"
```

### Logging Data into Files

Append mode is perfect for logging:

```python
import datetime

def log_event(message, log_file="app.log"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

log_event("Application started")
log_event("User logged in: alice@example.com")
log_event("Error: database connection failed")

# app.log:
# [2024-01-15 10:23:01] Application started
# [2024-01-15 10:23:15] User logged in: alice@example.com
# [2024-01-15 10:25:44] Error: database connection failed
```

---

## 8. Working with File Cursor and Position

### What the File Pointer/Cursor Is

When you open a file, Python keeps track of a **cursor** (also called a file pointer) — an integer representing your current position in the file, measured in bytes from the beginning. Every read/write operation moves this cursor forward.

Think of it like a read-head on a cassette tape: it moves as you play, and you can rewind it.

### `tell()`

Returns the **current position** of the cursor (in bytes from the start of the file).

```python
with open("data.txt", "r") as f:
    print(f.tell())         # 0 — at the beginning

    f.read(5)               # Read 5 characters
    print(f.tell())         # 5 — cursor moved 5 bytes

    f.readline()            # Read the rest of the line
    print(f.tell())         # Position after the newline
```

### `seek()`

Moves the cursor to a specific position.

```python
f.seek(offset, whence)
```

| `whence` | Meaning |
|----------|---------|
| `0` (default) | From the **beginning** of the file |
| `1` | From the **current** position |
| `2` | From the **end** of the file |

```python
with open("sample.txt", "r") as f:
    f.seek(10)         # Move to byte 10 from start
    print(f.read(5))   # Read 5 bytes from position 10

    f.seek(0)          # Back to the beginning
    print(f.read(3))   # Read first 3 bytes

    f.seek(-5, 2)      # 5 bytes before the end (binary mode required for whence=1,2)
```

> **Important:** `seek()` with `whence=1` or `whence=2` only works in **binary mode** (`"rb"`, etc.). In text mode, only `seek(0)` and values returned by `tell()` are guaranteed to work.

### Moving Around Inside Files

```python
# Practical example: read header, skip middle, read footer
with open("report.txt", "rb") as f:
    # Read first 50 bytes (header)
    header = f.read(50)
    print("Header:", header)

    # Jump to 100 bytes before end (footer)
    f.seek(-100, 2)
    footer = f.read()
    print("Footer:", footer)

# Reread a file from the beginning without reopening
with open("data.txt", "r") as f:
    first_read = f.read()
    f.seek(0)            # Rewind
    second_read = f.read()
    print(first_read == second_read)  # True
```

---

## 9. Handling File Errors and Exceptions

### Common File Errors

#### `FileNotFoundError`

Raised when you try to open a file in `"r"` mode but it doesn't exist.

```python
open("ghost.txt", "r")
# FileNotFoundError: [Errno 2] No such file or directory: 'ghost.txt'
```

#### `PermissionError`

Raised when you don't have the OS-level permission to read or write the file.

```python
open("/etc/shadow", "r")
# PermissionError: [Errno 13] Permission denied: '/etc/shadow'
```

#### `IsADirectoryError`

Raised when you try to open a directory as if it were a file.

```python
open("/home/user/", "r")
# IsADirectoryError: [Errno 21] Is a directory: '/home/user/'
```

#### Other Common Exceptions

| Exception | Cause |
|-----------|-------|
| `FileExistsError` | Using `"x"` mode on an existing file |
| `UnicodeDecodeError` | Reading a binary file in text mode with wrong encoding |
| `OSError` | General OS-level failure (disk full, etc.) |
| `IOError` | Alias for `OSError` |

### Using `try`, `except`, `finally`

```python
try:
    with open("data.txt", "r") as f:
        content = f.read()
        print(content)

except FileNotFoundError:
    print("Error: The file does not exist.")

except PermissionError:
    print("Error: You don't have permission to read this file.")

except IsADirectoryError:
    print("Error: The path points to a directory, not a file.")

except UnicodeDecodeError:
    print("Error: Could not decode the file. It may be binary.")

except OSError as e:
    print(f"OS Error: {e}")

finally:
    print("File operation attempted.")  # Always runs
```

### Writing Safe File Operations

```python
import os

def safe_read(filepath):
    """Safely read a file with full error handling."""
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return None

    if not os.path.isfile(filepath):
        print(f"Not a file: {filepath}")
        return None

    if not os.access(filepath, os.R_OK):
        print(f"No read permission: {filepath}")
        return None

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except UnicodeDecodeError:
        print("Encoding error — trying latin-1")
        try:
            with open(filepath, "r", encoding="latin-1") as f:
                return f.read()
        except Exception as e:
            print(f"Failed: {e}")
            return None

content = safe_read("notes.txt")
if content:
    print(content)
```

---

## 10. Working with Binary Files

### Binary vs Text Files

| Feature | Text Mode | Binary Mode |
|---------|-----------|-------------|
| Encoding | Yes (UTF-8, etc.) | No |
| Newline translation | Yes (`\n` ↔ `\r\n` on Windows) | No |
| Data type returned | `str` | `bytes` |
| Use for | Text documents | Images, audio, video, etc. |

### Reading Binary Files

```python
with open("photo.jpg", "rb") as f:
    data = f.read()
    print(type(data))       # <class 'bytes'>
    print(data[:4])         # b'\xff\xd8\xff\xe0' — JPEG magic bytes
```

Identifying file types by "magic bytes":

```python
def get_file_type(filepath):
    """Detect file type from magic bytes."""
    with open(filepath, "rb") as f:
        header = f.read(8)

    if header[:4] == b'\xff\xd8\xff\xe0':
        return "JPEG Image"
    elif header[:8] == b'\x89PNG\r\n\x1a\n':
        return "PNG Image"
    elif header[:4] == b'%PDF':
        return "PDF Document"
    elif header[:2] == b'PK':
        return "ZIP Archive (or DOCX/XLSX)"
    else:
        return "Unknown"

print(get_file_type("image.jpg"))   # JPEG Image
```

### Writing Binary Files

```python
# Copy a binary file manually
with open("original.jpg", "rb") as src:
    with open("copy.jpg", "wb") as dst:
        data = src.read()
        dst.write(data)

# Efficient chunked copy for large files
def copy_binary(source, destination, chunk_size=65536):
    with open(source, "rb") as src, open(destination, "wb") as dst:
        while True:
            chunk = src.read(chunk_size)
            if not chunk:
                break
            dst.write(chunk)

copy_binary("video.mp4", "video_backup.mp4")
```

### Examples with Images/PDFs

```python
# Write raw bytes to create a minimal valid PNG (1x1 white pixel)
import struct, zlib

def create_minimal_png(filename):
    """Create a 1x1 white PNG file from scratch."""
    signature = b'\x89PNG\r\n\x1a\n'

    def chunk(name, data):
        c = name + data
        return struct.pack('>I', len(data)) + c + struct.pack('>I', zlib.crc32(c) & 0xffffffff)

    ihdr = chunk(b'IHDR', struct.pack('>IIBBBBB', 1, 1, 8, 2, 0, 0, 0))
    idat = chunk(b'IDAT', zlib.compress(b'\x00\xff\xff\xff'))
    iend = chunk(b'IEND', b'')

    with open(filename, 'wb') as f:
        f.write(signature + ihdr + idat + iend)

create_minimal_png("white_pixel.png")

# Read and print PDF metadata (first 1024 bytes)
with open("document.pdf", "rb") as f:
    header = f.read(1024).decode("latin-1", errors="replace")
    print(header[:200])
```

---

## 11. File and Directory Management with `os`

### Introduction to the `os` Module

The `os` module provides a **portable interface to operating system features**: creating, deleting, renaming, and navigating files and directories.

```python
import os
```

### Checking If Files Exist

```python
import os

# Check if a path exists (file or directory)
print(os.path.exists("data.txt"))      # True or False

# Check if it's a file specifically
print(os.path.isfile("data.txt"))      # True

# Check if it's a directory
print(os.path.isdir("my_folder"))      # True

# Check permissions
print(os.access("data.txt", os.R_OK))  # Readable?
print(os.access("data.txt", os.W_OK))  # Writable?
print(os.access("data.txt", os.X_OK))  # Executable?
```

### Creating Files and Folders

```python
import os

# Create a single directory
os.mkdir("new_folder")

# Create nested directories (like mkdir -p)
os.makedirs("parent/child/grandchild", exist_ok=True)
# exist_ok=True means no error if it already exists

# Create a file by opening it for writing
with open("new_folder/notes.txt", "w") as f:
    f.write("Hello!")
```

### Renaming Files

```python
import os

os.rename("old_name.txt", "new_name.txt")

# Move to a different folder (also uses rename)
os.rename("file.txt", "archive/file.txt")
```

### Deleting Files

```python
import os
import shutil

# Delete a single file
os.remove("unwanted.txt")

# Delete an empty directory
os.rmdir("empty_folder")

# Delete a directory and all its contents (DANGEROUS — irreversible!)
shutil.rmtree("folder_with_stuff")

# Safe delete with check
def safe_delete(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
        print(f"Deleted: {filepath}")
    else:
        print(f"Not found or not a file: {filepath}")

safe_delete("temp.txt")
```

### Navigating Directories

```python
import os

# List all items in a directory
items = os.listdir(".")           # Current directory
print(items)                      # ['file.txt', 'folder', ...]

# Walk through all files recursively
for root, dirs, files in os.walk("my_project"):
    print(f"Directory: {root}")
    for file in files:
        full_path = os.path.join(root, file)
        print(f"  File: {full_path}")

# Get file info
stat = os.stat("data.txt")
print(f"Size: {stat.st_size} bytes")
print(f"Last modified: {stat.st_mtime}")

# Path manipulation
filepath = "/home/user/documents/report.txt"
print(os.path.dirname(filepath))   # /home/user/documents
print(os.path.basename(filepath))  # report.txt
print(os.path.splitext(filepath))  # ('/home/user/documents/report', '.txt')
print(os.path.abspath("notes.txt")) # Absolute path from relative
```

---

## 12. Using the `pathlib` Module

### Why `pathlib` Is Modern and Preferred

Introduced in Python 3.4, `pathlib` offers an **object-oriented** approach to file paths. Instead of working with bare strings, you work with `Path` objects that have useful methods. It automatically handles OS differences.

```python
from pathlib import Path
```

### Creating Paths

```python
from pathlib import Path

# Create a Path object
p = Path("data.txt")
home = Path.home()           # Current user's home directory
cwd = Path.cwd()             # Current working directory

# Absolute path
absolute = Path("/home/user/documents/report.txt")
```

### Joining Paths

Use the `/` operator — much cleaner than `os.path.join()`:

```python
from pathlib import Path

base = Path("/home/user")
full = base / "documents" / "report.txt"
print(full)   # /home/user/documents/report.txt

# Also works with strings
folder = Path("data") / "csv" / "sales.csv"
```

### Checking File Existence

```python
from pathlib import Path

p = Path("data.txt")

print(p.exists())      # True if path exists (file or dir)
print(p.is_file())     # True if it's a file
print(p.is_dir())      # True if it's a directory
print(p.stat().st_size)    # File size in bytes
```

### Reading/Writing with `pathlib`

```python
from pathlib import Path

p = Path("notes.txt")

# Write text (creates or overwrites)
p.write_text("Hello from pathlib!\nSecond line.")

# Read text
content = p.read_text()
print(content)

# Write bytes
p_bin = Path("data.bin")
p_bin.write_bytes(b'\x00\x01\x02\x03')

# Read bytes
raw = p_bin.read_bytes()
print(raw)  # b'\x00\x01\x02\x03'
```

### More Useful `pathlib` Operations

```python
from pathlib import Path

p = Path("/home/user/documents/report.txt")

# Path parts
print(p.name)       # report.txt
print(p.stem)       # report
print(p.suffix)     # .txt
print(p.parent)     # /home/user/documents
print(p.parts)      # ('/', 'home', 'user', 'documents', 'report.txt')

# Rename and delete
p.rename(p.parent / "final_report.txt")
p.unlink()  # Delete file

# Create directories
Path("new/nested/dir").mkdir(parents=True, exist_ok=True)

# List files matching a pattern (glob)
for txt_file in Path(".").glob("*.txt"):
    print(txt_file)

# Recursive glob
for py_file in Path(".").rglob("*.py"):
    print(py_file)

# Iterate directory contents
for item in Path(".").iterdir():
    print(item, "is file" if item.is_file() else "is dir")
```

---

## 13. Working with CSV Files

### What CSV Files Are

**CSV (Comma-Separated Values)** is a plain-text format for tabular data. Each line is a row, and values in each row are separated by commas (or sometimes semicolons, tabs, or pipes).

```
name,age,city
Alice,30,Lagos
Bob,25,Abuja
Charlie,35,Kano
```

### Reading CSV Files

#### Basic reading without the `csv` module:

```python
with open("people.csv", "r") as f:
    for line in f:
        parts = line.strip().split(",")
        print(parts)
# ['name', 'age', 'city']
# ['Alice', '30', 'Lagos']
```

#### Problem: Commas inside quoted fields break naive splitting.
Use Python's `csv` module instead.

### Using Python's `csv` Module

#### `csv.reader`

```python
import csv

with open("people.csv", "r", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)  # Read the header row
    print("Headers:", header)

    for row in reader:
        name, age, city = row
        print(f"{name} is {age} years old and lives in {city}")
```

> **Always use `newline=""` when opening CSV files** — the `csv` module handles newlines internally.

#### Writing CSV Files

```python
import csv

data = [
    ["name", "age", "city"],
    ["Alice", 30, "Lagos"],
    ["Bob", 25, "Abuja"],
    ["Charlie", 35, "Kano"],
]

with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)   # Write all rows at once
```

Or row by row:

```python
import csv

with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age", "city"])  # Header
    writer.writerow(["Alice", 30, "Lagos"])
    writer.writerow(["Bob", 25, "Abuja"])
```

### CSV Dictionaries

`DictReader` and `DictWriter` let you work with rows as dictionaries — much more readable.

#### `csv.DictReader`

```python
import csv

with open("people.csv", "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        # row is an OrderedDict
        print(f"Name: {row['name']}, Age: {row['age']}, City: {row['city']}")
```

#### `csv.DictWriter`

```python
import csv

students = [
    {"name": "Alice", "grade": 92, "subject": "Math"},
    {"name": "Bob", "grade": 85, "subject": "Science"},
]

with open("students.csv", "w", newline="") as f:
    fieldnames = ["name", "grade", "subject"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()          # Writes the column names row
    writer.writerows(students)    # Writes all student dicts
```

### Custom Delimiters

```python
import csv

# Tab-separated values (TSV)
with open("data.tsv", "r", newline="") as f:
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        print(row)

# Pipe-separated values
with open("data.psv", "r", newline="") as f:
    reader = csv.reader(f, delimiter="|")
    for row in reader:
        print(row)
```

---

## 14. Working with JSON Files

### What JSON Is

**JSON (JavaScript Object Notation)** is a lightweight, human-readable data interchange format. It uses key-value pairs (like Python dictionaries), arrays (like Python lists), strings, numbers, booleans, and null.

```json
{
  "name": "Alice",
  "age": 30,
  "skills": ["Python", "SQL", "Excel"],
  "active": true,
  "address": {
    "city": "Lagos",
    "country": "Nigeria"
  }
}
```

Python's `json` module maps JSON types to Python types:

| JSON | Python |
|------|--------|
| object `{}` | `dict` |
| array `[]` | `list` |
| string `""` | `str` |
| number | `int` or `float` |
| `true`/`false` | `True`/`False` |
| `null` | `None` |

### Serializing Data (`dumps` / `dump`)

**Serialization** = converting Python objects → JSON string/file.

#### `json.dumps()` — Python object → JSON string

```python
import json

data = {
    "name": "Alice",
    "age": 30,
    "skills": ["Python", "SQL"]
}

json_string = json.dumps(data)
print(json_string)
# '{"name": "Alice", "age": 30, "skills": ["Python", "SQL"]}'

# Pretty printing
pretty = json.dumps(data, indent=4, sort_keys=True)
print(pretty)
```

#### `json.dump()` — Python object → JSON file

```python
import json

data = {"name": "Alice", "age": 30}

with open("user.json", "w") as f:
    json.dump(data, f, indent=4)
```

### Deserializing Data (`loads` / `load`)

**Deserialization** = converting JSON string/file → Python objects.

#### `json.loads()` — JSON string → Python object

```python
import json

json_string = '{"name": "Alice", "age": 30, "skills": ["Python", "SQL"]}'

data = json.loads(json_string)
print(type(data))          # <class 'dict'>
print(data["name"])        # Alice
print(data["skills"][0])   # Python
```

#### `json.load()` — JSON file → Python object

```python
import json

with open("user.json", "r") as f:
    data = json.load(f)

print(data["name"])   # Alice
```

### Real-World JSON Example

```python
import json

# Configuration file management
def load_config(path="config.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}  # Return empty config if file doesn't exist

def save_config(config, path="config.json"):
    with open(path, "w") as f:
        json.dump(config, f, indent=4)

# Usage
config = load_config()
config["theme"] = "dark"
config["font_size"] = 14
save_config(config)
```

### Handling Complex Objects

```python
import json
from datetime import datetime

# json.dumps() cannot serialize datetime by default
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

data = {"event": "meeting", "time": datetime.now()}
json_str = json.dumps(data, cls=DateTimeEncoder, indent=2)
print(json_str)
```

---

## 15. Working with User Input and Files

### Saving User Input into Files

```python
def collect_and_save():
    """Collect user input and save to a file."""
    entries = []
    print("Enter items (type 'done' to finish):")

    while True:
        item = input("> ").strip()
        if item.lower() == "done":
            break
        if item:
            entries.append(item)

    with open("user_data.txt", "a") as f:
        for entry in entries:
            f.write(entry + "\n")

    print(f"Saved {len(entries)} entries.")

collect_and_save()
```

### Reading Saved Data

```python
def display_saved():
    """Read and display previously saved data."""
    try:
        with open("user_data.txt", "r") as f:
            lines = f.readlines()
        if lines:
            print("Saved entries:")
            for i, line in enumerate(lines, 1):
                print(f"  {i}. {line.strip()}")
        else:
            print("No entries saved yet.")
    except FileNotFoundError:
        print("No data file found. Add some entries first.")

display_saved()
```

### Building Small Storage Systems

```python
import json

class SimpleStorage:
    """A simple key-value storage system using a JSON file."""

    def __init__(self, filepath="storage.json"):
        self.filepath = filepath
        self.data = self._load()

    def _load(self):
        try:
            with open(self.filepath, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def _save(self):
        with open(self.filepath, "w") as f:
            json.dump(self.data, f, indent=4)

    def set(self, key, value):
        self.data[key] = value
        self._save()

    def get(self, key, default=None):
        return self.data.get(key, default)

    def delete(self, key):
        if key in self.data:
            del self.data[key]
            self._save()

    def all(self):
        return dict(self.data)

# Usage
store = SimpleStorage()
store.set("username", "alice")
store.set("score", 100)
print(store.get("username"))    # alice
print(store.all())              # {'username': 'alice', 'score': 100}
store.delete("score")
```

---

## 16. File Compression Basics

### Introduction to ZIP Files

ZIP is a widely-used archive format that compresses multiple files into a single `.zip` file, reducing their total size and making them easier to distribute.

### Using `zipfile`

```python
import zipfile
```

### Compressing Files

```python
import zipfile
import os

# Create a ZIP archive
with zipfile.ZipFile("archive.zip", "w", compression=zipfile.ZIP_DEFLATED) as zf:
    zf.write("report.txt")                        # Add a file
    zf.write("data.csv", arcname="data/data.csv") # Add with a different path inside ZIP
    zf.write("image.png")

# ZIP an entire folder
def zip_folder(folder_path, output_zip):
    with zipfile.ZipFile(output_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zf.write(file_path, arcname)

zip_folder("my_project", "my_project.zip")
```

### Extracting Files

```python
import zipfile

# Extract all files
with zipfile.ZipFile("archive.zip", "r") as zf:
    zf.extractall("extracted_files/")

# Extract a specific file
with zipfile.ZipFile("archive.zip", "r") as zf:
    zf.extract("report.txt", "output/")

# List contents without extracting
with zipfile.ZipFile("archive.zip", "r") as zf:
    zf.printdir()
    names = zf.namelist()
    print(names)

# Read a file from ZIP without extracting to disk
with zipfile.ZipFile("archive.zip", "r") as zf:
    with zf.open("report.txt") as f:
        content = f.read().decode("utf-8")
        print(content)
```

### Password-Protected ZIPs

```python
# Extract with password
with zipfile.ZipFile("secure.zip", "r") as zf:
    zf.extractall("output/", pwd=b"secretpassword")
```

---

## 17. Temporary Files

### Why Temporary Files Are Useful

Temporary files are used when a program needs to:
- Store intermediate results that don't need to persist
- Process data too large to hold in memory
- Pass data between processes through the file system
- Create scratch space during file conversions

### Using the `tempfile` Module

```python
import tempfile
import os
```

#### `NamedTemporaryFile`

Creates a temporary file with a name visible on the file system. Deleted when closed (by default).

```python
import tempfile

# Auto-deleted when the with block exits
with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=True) as tmp:
    tmp.write("Temporary content\n")
    tmp.flush()                      # Ensure data is written to disk
    print(f"Temp file: {tmp.name}")  # Something like /tmp/tmpABCDEF.txt
    # Work with the file here
# File is deleted here

# Keep the file after closing (delete=False)
tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False)
tmp.write("name,age\nAlice,30\n")
tmp.close()
print(f"File kept at: {tmp.name}")
os.unlink(tmp.name)  # Delete manually when done
```

#### `TemporaryDirectory`

```python
import tempfile
import os

with tempfile.TemporaryDirectory() as tmpdir:
    print(f"Temp directory: {tmpdir}")
    # Create files inside
    filepath = os.path.join(tmpdir, "scratch.txt")
    with open(filepath, "w") as f:
        f.write("Scratch data")
    # Directory and all its contents are deleted when block exits
```

#### `SpooledTemporaryFile`

Starts in memory, spills to disk only if it exceeds a size limit. Good for unknown-size data.

```python
import tempfile

with tempfile.SpooledTemporaryFile(max_size=1024*1024, mode="w") as f:
    # Lives in RAM up to 1MB, then spills to disk
    f.write("Some data")
    f.seek(0)
    print(f.read())
```

---

## 18. Advanced File Handling Concepts

### Buffering

By default, Python **buffers** file I/O — instead of writing each byte immediately to disk (which is slow), it accumulates data in a buffer (in RAM) and writes it in larger, efficient chunks.

```python
# Default buffering
with open("data.txt", "w") as f:
    f.write("Hello")          # May not be on disk yet!
    f.flush()                 # Force-write buffer to disk now
# File is fully written when the with block exits (flush + close)

# Disable buffering (line-buffered for text files)
with open("live.log", "w", buffering=1) as f:
    f.write("Line 1\n")       # Written immediately (line-buffered)

# Fully unbuffered (binary mode only)
with open("raw.bin", "wb", buffering=0) as f:
    f.write(b'\x00\x01')     # Written immediately
```

### Encoding and Decoding

**Encoding** converts text (characters) to bytes. **Decoding** converts bytes back to text.

```python
# Specify encoding when opening
with open("arabic.txt", "r", encoding="utf-8") as f:
    text = f.read()

with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello, العالم!")  # Mix of English and Arabic

# Handle encoding errors
with open("messy.txt", "r", encoding="utf-8", errors="replace") as f:
    text = f.read()   # Replaces invalid bytes with ?

# or ignore bad characters
with open("messy.txt", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()   # Skips invalid bytes
```

### UTF-8 and Character Encoding

| Encoding | Description |
|----------|-------------|
| `ascii` | 128 characters; English only |
| `latin-1` / `iso-8859-1` | 256 characters; Western European |
| `utf-8` | Variable width; all Unicode characters; default for most modern systems |
| `utf-16` | Fixed 2-byte encoding; used internally by Windows/Java |
| `cp1252` | Windows Western European |

**Always use UTF-8 unless you have a specific reason not to.**

```python
# Detect encoding of an unknown file (requires chardet library)
# pip install chardet
import chardet

with open("unknown.txt", "rb") as f:
    raw = f.read()

result = chardet.detect(raw)
print(result)  # {'encoding': 'utf-8', 'confidence': 0.99}

with open("unknown.txt", "r", encoding=result["encoding"]) as f:
    text = f.read()
```

### Large File Processing

```python
# Processing a multi-gigabyte log file line by line
def count_errors(filepath):
    error_count = 0
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:              # Only one line in memory at a time
            if "ERROR" in line:
                error_count += 1
    return error_count

# Using generators for pipeline processing
def read_lines(filepath):
    with open(filepath, "r") as f:
        for line in f:
            yield line.strip()

def filter_errors(lines):
    for line in lines:
        if "ERROR" in line:
            yield line

def count(iterable):
    return sum(1 for _ in iterable)

pipeline = filter_errors(read_lines("app.log"))
print(f"Total errors: {count(pipeline)}")
```

### File Streaming

File streaming means processing data **as it flows**, without loading everything at once.

```python
# Stream-process a large CSV
import csv

def stream_process_csv(filepath):
    with open(filepath, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row    # One row at a time — never loads whole file

total_sales = sum(
    float(row["amount"])
    for row in stream_process_csv("transactions.csv")
)
print(f"Total: ${total_sales:,.2f}")
```

---

## 19. Best Practices in File Handling

### Proper File Closing

Always use `with` statements. They guarantee closure even if an exception occurs.

```python
# GOOD
with open("data.txt") as f:
    content = f.read()

# BAD — if read() fails, f.close() is never called
f = open("data.txt")
content = f.read()
f.close()
```

### Efficient Reading/Writing

```python
# For text files: iterate line by line, don't use read() on large files
with open("big.txt") as f:
    for line in f:
        process(line)

# For binary files: use fixed-size chunks
with open("big.bin", "rb") as f:
    while chunk := f.read(65536):   # Walrus operator (Python 3.8+)
        process(chunk)

# Write all at once rather than in a loop when possible
lines = generate_lines()  # Returns a list
with open("output.txt", "w") as f:
    f.writelines(lines)   # One system call, not thousands
```

### Error Handling Strategies

```python
import os

# Strategy 1: LBYL (Look Before You Leap)
if os.path.isfile("data.txt"):
    with open("data.txt") as f:
        content = f.read()

# Strategy 2: EAFP (Easier to Ask Forgiveness than Permission) — Pythonic
try:
    with open("data.txt") as f:
        content = f.read()
except FileNotFoundError:
    content = ""

# Strategy 3: Provide defaults
def read_with_default(filepath, default=""):
    try:
        with open(filepath, "r") as f:
            return f.read()
    except (FileNotFoundError, PermissionError):
        return default
```

### Security Considerations

```python
import os

# NEVER trust user-provided file paths without validation
def safe_open(filename, base_dir="allowed_files/"):
    """Prevent directory traversal attacks."""
    # Resolve to absolute paths
    base = os.path.realpath(base_dir)
    requested = os.path.realpath(os.path.join(base_dir, filename))

    # Ensure requested path is inside base directory
    if not requested.startswith(base + os.sep):
        raise ValueError(f"Access denied: {filename}")

    return open(requested, "r")

# BAD — user could pass "../../../etc/passwd"
# open(user_input)

# GOOD
try:
    f = safe_open(user_input)
except ValueError as e:
    print(e)
```

### Organizing Project Files

```
my_project/
│
├── data/               # Input data files
│   ├── raw/            # Unprocessed data
│   └── processed/      # Cleaned/transformed data
│
├── output/             # Generated output files
├── logs/               # Log files
├── config/             # Configuration files
├── src/                # Source code
│   └── main.py
├── tests/              # Tests
└── README.md
```

---

## 20. Practical Mini Projects

### 1. Note-Taking App

```python
import json
import datetime
import os

NOTES_FILE = "notes.json"

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as f:
            return json.load(f)
    return []

def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=4)

def add_note(title, content):
    notes = load_notes()
    notes.append({
        "id": len(notes) + 1,
        "title": title,
        "content": content,
        "created": datetime.datetime.now().isoformat()
    })
    save_notes(notes)
    print(f"Note '{title}' saved.")

def list_notes():
    notes = load_notes()
    if not notes:
        print("No notes yet.")
        return
    for note in notes:
        print(f"[{note['id']}] {note['title']} — {note['created'][:10]}")

def view_note(note_id):
    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            print(f"\nTitle: {note['title']}")
            print(f"Date: {note['created']}")
            print(f"\n{note['content']}")
            return
    print("Note not found.")

# Run the app
add_note("Meeting Notes", "Discussed project deadlines and milestones.")
add_note("Shopping List", "Eggs, Milk, Bread, Python book")
list_notes()
view_note(1)
```

### 2. Student Record System

```python
import csv
import os

RECORDS_FILE = "students.csv"

def initialize():
    if not os.path.exists(RECORDS_FILE):
        with open(RECORDS_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "name", "age", "grade"])
            writer.writeheader()

def add_student(name, age, grade):
    students = get_all_students()
    new_id = max((int(s["id"]) for s in students), default=0) + 1
    with open(RECORDS_FILE, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "age", "grade"])
        writer.writerow({"id": new_id, "name": name, "age": age, "grade": grade})
    print(f"Student {name} added with ID {new_id}")

def get_all_students():
    with open(RECORDS_FILE, "r", newline="") as f:
        return list(csv.DictReader(f))

def display_all():
    students = get_all_students()
    if not students:
        print("No students found.")
        return
    print(f"\n{'ID':<5} {'Name':<20} {'Age':<5} {'Grade'}")
    print("-" * 40)
    for s in students:
        print(f"{s['id']:<5} {s['name']:<20} {s['age']:<5} {s['grade']}")

initialize()
add_student("Alice Johnson", 17, "A")
add_student("Bob Smith", 16, "B+")
add_student("Charlie Brown", 18, "A-")
display_all()
```

### 3. Simple Logger

```python
import datetime
import os

class Logger:
    LEVELS = {"DEBUG": 0, "INFO": 1, "WARNING": 2, "ERROR": 3, "CRITICAL": 4}

    def __init__(self, filepath="app.log", min_level="INFO"):
        self.filepath = filepath
        self.min_level = min_level

    def _write(self, level, message):
        if self.LEVELS.get(level, 0) < self.LEVELS.get(self.min_level, 0):
            return
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] [{level:<8}] {message}\n"
        with open(self.filepath, "a") as f:
            f.write(entry)
        print(entry.strip())

    def debug(self, msg): self._write("DEBUG", msg)
    def info(self, msg): self._write("INFO", msg)
    def warning(self, msg): self._write("WARNING", msg)
    def error(self, msg): self._write("ERROR", msg)
    def critical(self, msg): self._write("CRITICAL", msg)

log = Logger("myapp.log", min_level="INFO")
log.info("Application started")
log.warning("Low disk space detected")
log.error("Failed to connect to database")
log.debug("This won't show (below min level)")
```

### 4. CSV Data Processor

```python
import csv
from collections import defaultdict

def analyze_sales(filepath):
    """Read a sales CSV and compute summary statistics."""
    totals = defaultdict(float)
    counts = defaultdict(int)

    with open(filepath, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            product = row["product"]
            amount = float(row["amount"])
            totals[product] += amount
            counts[product] += 1

    print(f"\n{'Product':<20} {'Sales Count':<15} {'Total Revenue'}")
    print("-" * 50)
    for product in sorted(totals, key=totals.get, reverse=True):
        print(f"{product:<20} {counts[product]:<15} ${totals[product]:,.2f}")

# Create sample data
with open("sales.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["product", "amount", "date"])
    writer.writerows([
        ["Laptop", 1200.00, "2024-01-01"],
        ["Phone", 800.00, "2024-01-02"],
        ["Laptop", 1100.00, "2024-01-03"],
        ["Tablet", 400.00, "2024-01-04"],
        ["Phone", 750.00, "2024-01-05"],
    ])

analyze_sales("sales.csv")
```

### 5. JSON Configuration Manager

```python
import json
import os

class ConfigManager:
    def __init__(self, config_file="config.json", defaults=None):
        self.config_file = config_file
        self.defaults = defaults or {}
        self.config = self._load()

    def _load(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, "r") as f:
                data = json.load(f)
            # Merge with defaults (defaults fill missing keys)
            return {**self.defaults, **data}
        return dict(self.defaults)

    def save(self):
        with open(self.config_file, "w") as f:
            json.dump(self.config, f, indent=4)

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value
        self.save()

    def reset(self):
        self.config = dict(self.defaults)
        self.save()

config = ConfigManager("app_config.json", defaults={
    "theme": "light",
    "font_size": 12,
    "language": "en",
    "autosave": True
})

print(config.get("theme"))      # light (from defaults)
config.set("theme", "dark")     # Changed and saved
print(config.get("theme"))      # dark
```

### 6. File Organizer

```python
import os
import shutil

def organize_folder(source_dir):
    """Sort files into subfolders by extension."""
    extension_map = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
        "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
        "Audio": [".mp3", ".wav", ".flac", ".aac"],
        "Archives": [".zip", ".tar", ".gz", ".rar"],
        "Code": [".py", ".js", ".html", ".css", ".java", ".cpp"],
    }

    moved = 0
    for filename in os.listdir(source_dir):
        filepath = os.path.join(source_dir, filename)
        if not os.path.isfile(filepath):
            continue

        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        destination_folder = "Others"
        for folder, extensions in extension_map.items():
            if ext in extensions:
                destination_folder = folder
                break

        dest_dir = os.path.join(source_dir, destination_folder)
        os.makedirs(dest_dir, exist_ok=True)
        shutil.move(filepath, os.path.join(dest_dir, filename))
        moved += 1

    print(f"Organized {moved} files in '{source_dir}'")

organize_folder("Downloads")
```

### 7. To-Do List Application

```python
import json
import os
from datetime import datetime

TODO_FILE = "todos.json"

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(TODO_FILE, "w") as f:
        json.dump(todos, f, indent=4)

def add_todo(task, priority="medium"):
    todos = load_todos()
    todos.append({
        "id": len(todos) + 1,
        "task": task,
        "priority": priority,
        "done": False,
        "created": datetime.now().isoformat()
    })
    save_todos(todos)
    print(f"Added: {task}")

def complete_todo(todo_id):
    todos = load_todos()
    for todo in todos:
        if todo["id"] == todo_id:
            todo["done"] = True
            save_todos(todos)
            print(f"Completed: {todo['task']}")
            return
    print("Task not found.")

def list_todos(show_done=False):
    todos = load_todos()
    filtered = [t for t in todos if show_done or not t["done"]]
    if not filtered:
        print("No tasks.")
        return
    for t in filtered:
        status = "✓" if t["done"] else "○"
        print(f"[{status}] ({t['priority']:<6}) {t['id']}. {t['task']}")

add_todo("Buy groceries", "high")
add_todo("Read Python book", "medium")
add_todo("Exercise", "low")
list_todos()
complete_todo(1)
list_todos()
```

---

## 21. Final Capstone Projects

### 1. Expense Tracker with File Storage

```python
import json
import os
from datetime import datetime
from collections import defaultdict

class ExpenseTracker:
    def __init__(self, file="expenses.json"):
        self.file = file
        self.expenses = self._load()

    def _load(self):
        if os.path.exists(self.file):
            with open(self.file, "r") as f:
                return json.load(f)
        return []

    def _save(self):
        with open(self.file, "w") as f:
            json.dump(self.expenses, f, indent=4)

    def add(self, amount, category, description=""):
        self.expenses.append({
            "id": len(self.expenses) + 1,
            "amount": float(amount),
            "category": category,
            "description": description,
            "date": datetime.now().strftime("%Y-%m-%d")
        })
        self._save()

    def summary(self):
        by_category = defaultdict(float)
        for exp in self.expenses:
            by_category[exp["category"]] += exp["amount"]
        total = sum(by_category.values())

        print(f"\n{'Category':<20} {'Total':>10}")
        print("-" * 32)
        for cat, amt in sorted(by_category.items(), key=lambda x: x[1], reverse=True):
            print(f"{cat:<20} ₦{amt:>9,.2f}")
        print("-" * 32)
        print(f"{'TOTAL':<20} ₦{total:>9,.2f}")

    def monthly_report(self, year, month):
        month_str = f"{year}-{month:02d}"
        filtered = [e for e in self.expenses if e["date"].startswith(month_str)]
        print(f"\nExpenses for {month_str}:")
        for e in filtered:
            print(f"  {e['date']}  {e['category']:<15} ₦{e['amount']:>8,.2f}  {e['description']}")

tracker = ExpenseTracker()
tracker.add(5000, "Food", "Groceries")
tracker.add(15000, "Transport", "Monthly bus pass")
tracker.add(2500, "Food", "Restaurant lunch")
tracker.add(30000, "Rent", "Monthly rent contribution")
tracker.summary()
tracker.monthly_report(2024, 1)
```

### 2. Contact Management System

```python
import json
import os

class ContactManager:
    def __init__(self, filepath="contacts.json"):
        self.filepath = filepath
        self.contacts = self._load()

    def _load(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, "r") as f:
                return json.load(f)
        return {}

    def _save(self):
        with open(self.filepath, "w") as f:
            json.dump(self.contacts, f, indent=4)

    def add(self, name, phone, email="", notes=""):
        self.contacts[name.lower()] = {
            "name": name, "phone": phone, "email": email, "notes": notes
        }
        self._save()
        print(f"Contact '{name}' saved.")

    def search(self, query):
        query = query.lower()
        results = [c for k, c in self.contacts.items() if query in k or query in c.get("phone", "")]
        if results:
            for c in results:
                print(f"\nName:  {c['name']}")
                print(f"Phone: {c['phone']}")
                print(f"Email: {c['email']}")
                if c["notes"]: print(f"Notes: {c['notes']}")
        else:
            print("No contacts found.")

    def delete(self, name):
        if name.lower() in self.contacts:
            del self.contacts[name.lower()]
            self._save()
            print(f"Deleted: {name}")
        else:
            print("Contact not found.")

    def list_all(self):
        if not self.contacts:
            print("No contacts.")
            return
        print(f"\n{'Name':<25} {'Phone':<15} {'Email'}")
        print("-" * 60)
        for c in sorted(self.contacts.values(), key=lambda x: x["name"]):
            print(f"{c['name']:<25} {c['phone']:<15} {c['email']}")

cm = ContactManager()
cm.add("Alice Johnson", "+234-801-234-5678", "alice@example.com")
cm.add("Bob Smith", "+234-802-345-6789", "bob@example.com", "Colleague")
cm.list_all()
cm.search("alice")
```

### 3. Log Analyzer

```python
import re
from collections import Counter, defaultdict
from datetime import datetime

def analyze_log(filepath):
    """Analyze an Apache/Nginx-style access log."""
    # Pattern: IP - - [Date] "METHOD /path HTTP/1.x" status size
    pattern = re.compile(
        r'(\d+\.\d+\.\d+\.\d+).*\[(.+?)\] "(\w+) (.+?) HTTP.*?" (\d+) (\d+)'
    )

    ip_counter = Counter()
    status_counter = Counter()
    path_counter = Counter()
    errors = []

    total = 0
    with open(filepath, "r") as f:
        for line in f:
            match = pattern.search(line)
            if not match:
                continue
            ip, date, method, path, status, size = match.groups()
            ip_counter[ip] += 1
            status_counter[status] += 1
            path_counter[path] += 1
            total += 1
            if status.startswith(("4", "5")):
                errors.append((date, status, path))

    print(f"\nLog Analysis Report")
    print("=" * 50)
    print(f"Total Requests: {total}")
    print(f"\nTop 5 IPs:")
    for ip, count in ip_counter.most_common(5):
        print(f"  {ip:<20} {count} requests")
    print(f"\nStatus Code Distribution:")
    for code, count in sorted(status_counter.items()):
        print(f"  HTTP {code}: {count}")
    print(f"\nTop 5 Paths:")
    for path, count in path_counter.most_common(5):
        print(f"  {path:<40} {count}")
    print(f"\nRecent Errors ({len(errors)} total):")
    for date, status, path in errors[-5:]:
        print(f"  [{date}] {status} {path}")

# analyze_log("access.log")  # Uncomment with a real log file
```

### 4. Simple Database-Like System Using Files

```python
import json
import os
from typing import Dict, List, Any, Optional
from datetime import datetime

class FileDatabase:
    """A simple key-value database backed by JSON files."""

    def __init__(self, db_dir="filedb"):
        self.db_dir = db_dir
        os.makedirs(db_dir, exist_ok=True)

    def _table_path(self, table):
        return os.path.join(self.db_dir, f"{table}.json")

    def _load_table(self, table) -> List[Dict]:
        path = self._table_path(table)
        if os.path.exists(path):
            with open(path, "r") as f:
                return json.load(f)
        return []

    def _save_table(self, table, data):
        with open(self._table_path(table), "w") as f:
            json.dump(data, f, indent=2)

    def insert(self, table, record: Dict) -> int:
        rows = self._load_table(table)
        new_id = max((r.get("_id", 0) for r in rows), default=0) + 1
        record["_id"] = new_id
        record["_created"] = datetime.now().isoformat()
        rows.append(record)
        self._save_table(table, rows)
        return new_id

    def find(self, table, query: Dict = None) -> List[Dict]:
        rows = self._load_table(table)
        if not query:
            return rows
        return [r for r in rows if all(r.get(k) == v for k, v in query.items())]

    def find_one(self, table, query: Dict) -> Optional[Dict]:
        results = self.find(table, query)
        return results[0] if results else None

    def update(self, table, query: Dict, updates: Dict) -> int:
        rows = self._load_table(table)
        count = 0
        for row in rows:
            if all(row.get(k) == v for k, v in query.items()):
                row.update(updates)
                row["_updated"] = datetime.now().isoformat()
                count += 1
        self._save_table(table, rows)
        return count

    def delete(self, table, query: Dict) -> int:
        rows = self._load_table(table)
        original_count = len(rows)
        rows = [r for r in rows if not all(r.get(k) == v for k, v in query.items())]
        self._save_table(table, rows)
        return original_count - len(rows)

    def count(self, table, query: Dict = None) -> int:
        return len(self.find(table, query))

# Usage
db = FileDatabase("my_database")

# Insert records
db.insert("users", {"name": "Alice", "email": "alice@example.com", "role": "admin"})
db.insert("users", {"name": "Bob", "email": "bob@example.com", "role": "user"})
db.insert("users", {"name": "Charlie", "email": "charlie@example.com", "role": "user"})

# Query
all_users = db.find("users")
print(f"All users: {len(all_users)}")

admins = db.find("users", {"role": "admin"})
print(f"Admins: {[u['name'] for u in admins]}")

# Update
updated = db.update("users", {"name": "Bob"}, {"role": "moderator"})
print(f"Updated {updated} record(s)")

# Delete
deleted = db.delete("users", {"name": "Charlie"})
print(f"Deleted {deleted} record(s)")

# Final count
print(f"Remaining users: {db.count('users')}")
```

---

## 22. Bonus: Additional Topics

*Topics not in the original outline but essential for complete mastery.*

### File Locking (Preventing Concurrent Access)

When multiple processes or threads access the same file simultaneously, data corruption can occur. File locking prevents this.

```python
import fcntl  # Unix/macOS only
import time

def write_with_lock(filepath, data):
    with open(filepath, "a") as f:
        try:
            fcntl.flock(f, fcntl.LOCK_EX)  # Exclusive lock
            f.write(data + "\n")
            time.sleep(0.1)  # Simulate work
        finally:
            fcntl.flock(f, fcntl.LOCK_UN)  # Release lock

# Cross-platform option: use portalocker library
# pip install portalocker
import portalocker

with open("shared.txt", "a") as f:
    portalocker.lock(f, portalocker.LOCK_EX)
    f.write("Safe write\n")
    portalocker.unlock(f)
```

### Working with `io` Module (In-Memory Files)

Sometimes you want to treat a string or bytes object as a file, without writing to disk.

```python
import io

# StringIO — in-memory text file
buffer = io.StringIO()
buffer.write("Hello ")
buffer.write("World")
buffer.seek(0)
print(buffer.read())   # Hello World
buffer.close()

# BytesIO — in-memory binary file
img_buffer = io.BytesIO()
img_buffer.write(b'\xff\xd8\xff')   # Fake JPEG header
img_buffer.seek(0)
data = img_buffer.read()
print(data)   # b'\xff\xd8\xff'

# Useful for: sending data to functions that expect file objects without writing to disk
import csv, io

output = io.StringIO()
writer = csv.writer(output)
writer.writerows([["Alice", 30], ["Bob", 25]])
csv_string = output.getvalue()
print(csv_string)
```

### File Hashing and Integrity Checking

```python
import hashlib

def compute_hash(filepath, algorithm="sha256"):
    """Compute cryptographic hash of a file."""
    h = hashlib.new(algorithm)
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def verify_integrity(filepath, expected_hash, algorithm="sha256"):
    actual = compute_hash(filepath, algorithm)
    return actual == expected_hash

hash_val = compute_hash("data.txt")
print(f"SHA-256: {hash_val}")

print(verify_integrity("data.txt", hash_val))  # True
```

### Watching Files for Changes

```python
# Using watchdog library: pip install watchdog
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class ChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            print(f"Modified: {event.src_path}")

    def on_created(self, event):
        print(f"Created: {event.src_path}")

    def on_deleted(self, event):
        print(f"Deleted: {event.src_path}")

observer = Observer()
observer.schedule(ChangeHandler(), path=".", recursive=False)
observer.start()

try:
    time.sleep(10)   # Watch for 10 seconds
finally:
    observer.stop()
    observer.join()
```

### Reading `.ini` Configuration Files

```python
import configparser

# Create a config file
config = configparser.ConfigParser()
config["DEFAULT"] = {"timeout": "30", "retries": "3"}
config["database"] = {
    "host": "localhost",
    "port": "5432",
    "name": "mydb"
}
config["app"] = {
    "debug": "false",
    "theme": "dark"
}

with open("settings.ini", "w") as f:
    config.write(f)

# Read a config file
config2 = configparser.ConfigParser()
config2.read("settings.ini")

print(config2["database"]["host"])        # localhost
print(config2["app"].getboolean("debug")) # False (as bool)
print(config2["database"].getint("port")) # 5432 (as int)
print(config2.get("DEFAULT", "timeout"))  # 30
```

### `shutil` — High-Level File Operations

```python
import shutil

# Copy a file (copies content + permissions)
shutil.copy("source.txt", "destination.txt")

# Copy file with metadata (timestamps, etc.)
shutil.copy2("source.txt", "destination.txt")

# Copy entire directory tree
shutil.copytree("my_project", "my_project_backup")

# Move a file or directory
shutil.move("file.txt", "archive/file.txt")

# Delete entire directory tree
shutil.rmtree("temp_folder")

# Get disk usage statistics
usage = shutil.disk_usage("/")
print(f"Total: {usage.total // (1024**3)} GB")
print(f"Used: {usage.used // (1024**3)} GB")
print(f"Free: {usage.free // (1024**3)} GB")

# Find a command on the PATH
python_path = shutil.which("python3")
print(f"Python is at: {python_path}")
```

### Working with Excel Files (`openpyxl`)

```python
# pip install openpyxl
import openpyxl

# Write to Excel
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Sales"

ws.append(["Name", "Sales", "Month"])
ws.append(["Alice", 5000, "January"])
ws.append(["Bob", 4200, "January"])

wb.save("sales.xlsx")

# Read from Excel
wb2 = openpyxl.load_workbook("sales.xlsx")
ws2 = wb2["Sales"]

for row in ws2.iter_rows(values_only=True):
    print(row)
# ('Name', 'Sales', 'Month')
# ('Alice', 5000, 'January')
# ('Bob', 4200, 'January')
```

### Glob Pattern Matching

```python
import glob

# Find all .txt files in current directory
txt_files = glob.glob("*.txt")
print(txt_files)

# Recursive search for all Python files
py_files = glob.glob("**/*.py", recursive=True)
print(py_files)

# Multiple patterns
import fnmatch
import os

all_files = os.listdir(".")
images = fnmatch.filter(all_files, "*.jpg") + fnmatch.filter(all_files, "*.png")
print(images)
```

### Summary: Choosing the Right Tool

| Task | Best Tool |
|------|-----------|
| Simple text read/write | `open()` with `with` |
| Cross-platform paths | `pathlib.Path` |
| CSV data | `csv` module |
| JSON config/data | `json` module |
| ZIP archives | `zipfile` module |
| Directory ops | `os` + `shutil` |
| In-memory files | `io.StringIO` / `io.BytesIO` |
| Temp files | `tempfile` module |
| Binary files | `open()` in `"rb"`/`"wb"` mode |
| Excel files | `openpyxl` |
| INI configs | `configparser` |
| File integrity | `hashlib` |
| File watching | `watchdog` |

---

*End of Python File Handling — Complete Study Notes*

> **Keep practising.** File handling is one of those skills where reading the notes gets you 20% of the way — the other 80% comes from building real projects and making real mistakes. Every project in Section 20 and 21 is worth building from scratch.