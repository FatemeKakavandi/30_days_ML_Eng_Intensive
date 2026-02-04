# Python `pathlib` Module -- Clear Summary with Examples

## What is `pathlib`?

`pathlib` is a built-in Python module that provides an **object-oriented
way to work with filesystem paths**.\
Instead of handling file paths as plain strings (like with `os.path`),
`pathlib` treats them as objects with useful methods and properties.

------------------------------------------------------------------------

## Why Use `pathlib` Instead of `os.path`?

Old way:

``` python
import os
os.path.join("folder", "file.txt")
```

With `pathlib`:

``` python
from pathlib import Path
Path("folder") / "file.txt"
```

It is cleaner, more readable, and cross-platform.

------------------------------------------------------------------------

## Core Concepts

### 1. Pure Paths (No filesystem access)

Used only for manipulating path strings safely.

``` python
from pathlib import PurePath

p = PurePath("/usr/bin/python3")
print(p.parts)   # ('/', 'usr', 'bin', 'python3')
print(p.name)    # 'python3'
print(p.suffix)  # ''
```

They DO NOT check if files exist.

------------------------------------------------------------------------

### 2. Concrete Paths (Actual filesystem access)

Used for real file operations.

``` python
from pathlib import Path

p = Path("example.txt")
print(p.exists())
print(p.is_file())
print(p.is_dir())
```

`Path` automatically becomes: - `PosixPath` on Linux/macOS -
`WindowsPath` on Windows

------------------------------------------------------------------------

## Common Operations

### Inspecting a Path

``` python
p = Path("/etc/passwd")
print(p.name)     # 'passwd'
print(p.suffix)   # ''
print(p.stem)     # 'passwd'
```

------------------------------------------------------------------------

### Creating Paths

``` python
p = Path("/etc") / "init.d" / "reboot"
print(p)
```

------------------------------------------------------------------------

### Reading and Writing Files

``` python
file = Path("example.txt")
file.write_text("Hello World!")
print(file.read_text())
```

------------------------------------------------------------------------

### Listing Directory Contents

``` python
for item in Path(".").iterdir():
    print(item)
```

------------------------------------------------------------------------

### Searching with Glob

``` python
for py_file in Path(".").glob("**/*.py"):
    print(py_file)
```

------------------------------------------------------------------------

### Creating and Deleting

``` python
Path("my_folder").mkdir(exist_ok=True)
Path("old.txt").unlink()
```

------------------------------------------------------------------------

## Useful Methods Cheat Sheet

| Task \| `pathlib` \|

\|------\|-----------\| Join paths \| `Path("a") / "b"` \| \| Check
exists \| `path.exists()` \| \| Check file \| `path.is_file()` \| \|
Check dir \| `path.is_dir()` \| \| Read text \| `path.read_text()` \| \|
Write text \| `path.write_text()` \| \| Make dir \| `path.mkdir()` \| \|
Delete file \| `path.unlink()` \|

------------------------------------------------------------------------

## Full Example Script

``` python
from pathlib import Path

root = Path("project")

(root / "data").mkdir(parents=True, exist_ok=True)
(root / "data/file1.txt").write_text("Hello")

for txt in root.rglob("*.txt"):
    print(txt.read_text())
```

------------------------------------------------------------------------

## Summary

-   `pathlib` provides an object-oriented interface for paths.
-   It replaces most uses of `os.path`.
-   Cleaner, safer, and cross-platform.
-   Supports file reading, writing, searching, and directory
    manipulation.
