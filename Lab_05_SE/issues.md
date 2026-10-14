# Static Code Analysis — Issues and Fixes

## Project Details

- **Student Name:** SANGADALA YEASASWANI
- **SRN:** PES2UG24CS441
- **Project:** Campus Shuttle System
- **File Analysed:** `shuttle_system.py`

## Issue Table

| Sl. No. | Tool | Issue Identified | Fix Applied |
|---:|---|---|---|
| 1 | Pylint | Missing module and function docstrings | Added descriptive docstrings |
| 2 | Pylint | Mutable default argument `logs=[]` | Changed to `logs=None` and initialized inside the function |
| 3 | Pylint | Function name `assignDriver` did not follow snake_case | Renamed it to `assign_driver` |
| 4 | Pylint | File handling lacked explicit encoding and context managers | Used `with open()` and UTF-8 encoding |
| 5 | Bandit | B110: Broad exception handling with `pass` | Removed the bare `except` and handled route data explicitly |
| 6 | Bandit | B311: Standard pseudo-random generator used for driver selection | Replaced `random.choice()` with `secrets.choice()` |
| 7 | Flake8 | E302/E305: Incorrect blank-line spacing | Corrected function spacing |
| 8 | Flake8 | E501: Line exceeded the maximum line length | Wrapped the long line |
| 9 | Flake8 | E722: Bare `except` statement | Removed the bare exception handler |

## Final Results

- **Pylint:** Before — 6.25/10; After — 10.00/10.
- **Bandit:** Before — 2 low-severity findings; After — 0 findings.
- **Flake8:** Before — formatting violations; After — 0 violations.