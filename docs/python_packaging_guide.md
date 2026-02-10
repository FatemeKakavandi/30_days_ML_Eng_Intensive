# Python Packaging -- Beginner-Friendly Guide

## 📦 What Does "Packaging" Mean?

Packaging a Python project means preparing your code so it can be:

-   Installed with `pip`
-   Shared with others
-   Uploaded to PyPI (Python Package Index)
-   Reused across different machines or projects

Instead of copying `.py` files manually, users can install your project
like this:

``` bash
pip install my-package-name
```

------------------------------------------------------------------------

# 🧱 Basic Project Structure

A modern Python package usually follows this structure:

    my_project/
    │
    ├── pyproject.toml
    ├── README.md
    ├── LICENSE
    └── src/
        └── my_package/
            ├── __init__.py
            └── example.py

### Why use the `src/` layout?

It prevents accidental imports from the local directory during
development and ensures your installed package works correctly.

------------------------------------------------------------------------

# 🧠 Example Python Code

Inside `example.py`:

``` python
def add_one(number):
    return number + 1
```

This is the code we want others to install and use.

------------------------------------------------------------------------

# 📄 Important Files Explained

## 1️⃣ `pyproject.toml` (The Most Important File)

This file contains metadata and build configuration.

Example:

``` toml
[build-system]
requires = ["hatchling >= 1.26"]
build-backend = "hatchling.build"

[project]
name = "my-example-package"
version = "0.0.1"
description = "A small example package"
readme = "README.md"
requires-python = ">=3.9"

authors = [
  { name="Your Name", email="you@example.com" }
]
```

### What This Means:

-   **name** → The package name on PyPI
-   **version** → The release version
-   **description** → Short summary
-   **requires-python** → Minimum Python version
-   **build-system** → Tool used to build the package

------------------------------------------------------------------------

## 2️⃣ README.md

This explains your project.\
It appears on your PyPI page.

Example:

``` markdown
# My Example Package

This package adds one to a number.
```

------------------------------------------------------------------------

## 3️⃣ LICENSE

Tells others how they are allowed to use your code\
(Common choice: MIT License)

------------------------------------------------------------------------

# 🔨 Building Your Package

First install build tools:

``` bash
python -m pip install --upgrade build
```

Then run:

``` bash
python -m build
```

This creates a `dist/` folder containing:

-   `.tar.gz` → Source distribution (sdist)
-   `.whl` → Wheel (built distribution)

Wheels are what `pip` prefers installing.

------------------------------------------------------------------------

# ☁️ Uploading to PyPI

First install Twine:

``` bash
python -m pip install --upgrade twine
```

Upload to TestPyPI (recommended first):

``` bash
twine upload --repository testpypi dist/*
```

After testing, upload to real PyPI:

``` bash
twine upload dist/*
```

You will need a PyPI account and an API token.

------------------------------------------------------------------------

# 📥 Installing Your Package

Once uploaded, anyone can install it:

``` bash
pip install my-example-package
```

Then use it in Python:

``` python
from my_package.example import add_one

print(add_one(2))  # Output: 3
```

------------------------------------------------------------------------

# 🚀 What You Achieve by Packaging

By packaging your project, you:

-   Make your code reusable
-   Enable easy installation with pip
-   Make it publishable on PyPI
-   Follow modern Python standards
-   Separate development from distribution

------------------------------------------------------------------------

# 🧩 Key Concepts Recap

  Concept         Meaning
  --------------- -------------------------------------
  Package         A directory containing Python code
  Distribution    Installable version of your project
  Wheel           Built package format (`.whl`)
  sdist           Source distribution (`.tar.gz`)
  PyPI            Official Python package repository
  Build Backend   Tool that builds your package

------------------------------------------------------------------------

# ✅ Best Practices

-   Always use virtual environments
-   Test on TestPyPI before real PyPI
-   Use semantic versioning (0.1.0 → 0.1.1 → 1.0.0)
-   Keep your README clear and helpful
-   Use the `src/` layout

------------------------------------------------------------------------

# 🎯 Final Understanding

Think of packaging like turning your Python project into a proper
product.

Instead of sharing:

    "Here’s my .py file, copy it into your project"

You share:

    pip install my-package

That is the power of Python packaging.
