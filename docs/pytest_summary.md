Good — this is something you’ll use constantly.

If you have:

```
tests/
├── test_top_k.py
└── test_train_test_split.py
```

and you only want to run **one file**, here’s how.

---

# ✅ Run One Specific Test File

From the project root:

```bash
pytest tests/test_top_k.py
```

or

```bash
python -m pytest tests/test_top_k.py
```

That will only run tests inside that file.

---

# ✅ Run One Specific Test Function

Inside the file:

```python
def test_reproducibility():
```

Run it like this:

```bash
pytest tests/test_train_test_split.py::test_reproducibility
```

Very useful when debugging one failing test.

---

# ✅ Run One Specific Test Class

If you had:

```python
class TestSplit:
    def test_shapes(self):
    def test_ratio(self):
```

Run:

```bash
pytest tests/test_train_test_split.py::TestSplit
```

---

# ✅ Run Tests Matching a Name Pattern

Example:

```bash
pytest -k reproducibility
```

Runs any test with “reproducibility” in its name across all files.

Extremely useful in larger projects.

---

# 🧠 Pro Tip for ML Engineers

When debugging:

```bash
pytest tests/test_top_k.py -v
```

* `-v` = verbose
* Shows each test clearly

For even better debugging:

```bash
pytest tests/test_top_k.py -vv
```

---

# 🚀 Professional Workflow Tip

When working on a function:

Run only that file repeatedly:

```bash
pytest tests/test_top_k.py
```

When finished:

Run everything:

```bash
pytest
```

This is how real engineers work — fast feedback loops.

---

If you'd like, I can also show you:

* How to stop on first failure (`-x`)
* How to run tests with coverage
* Or how to auto-run tests on file save (very powerful workflow)

