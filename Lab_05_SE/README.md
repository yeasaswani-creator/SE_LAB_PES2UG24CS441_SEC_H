# Lab 5: Static Code Analysis — Campus Shuttle Timetable & Fleet Tracker

**Student Name:** SANGADALA YEASASWANI  
**SRN:** PES2UG24CS441  
**Project:** Campus Shuttle System  
**File Analysed:** `shuttle_system.py`

## 1. Project Overview

The Campus Shuttle System is a Python program that manages campus shuttle routes, records passenger counts, calculates average passenger loads, identifies underused routes, assigns drivers, and synchronizes fleet data using JSON.

Static code analysis was performed using **Pylint, Bandit, and Flake8** to improve code quality, readability, maintainability, and security.

## 2. Objectives

- Identify code quality and maintainability issues.
- Detect potential security concerns.
- Correct Python style and formatting violations.
- Fix at least four issues in the source code.
- Compare static analysis results before and after fixes.
- Document the issues and reflect on the improvements.

## 3. Tools Used

| Tool | Purpose |
|---|---|
| Pylint | Checks Python code quality, naming conventions, and documentation. |
| Bandit | Detects potential security issues in Python code. |
| Flake8 | Checks Python style and formatting violations. |

## 4. Files Included

### Source Code
- `shuttle_system.py` — Corrected Python source code.

### Pylint Reports
- `pylint_report_before.txt` — Analysis results before fixes.
- `pylint_report_after.txt` — Analysis results after fixes.

### Bandit Reports
- `bandit_report_before.txt` — Security analysis before fixes.
- `bandit_report_after.txt` — Security analysis after fixes.

### Flake8 Reports
- `flake8_report_before.txt` — Formatting analysis before fixes.
- `flake8_report_after.txt` — Formatting analysis after fixes.

### Documentation
- `issues.md` — Issues identified and fixes applied.
- `reflection.md` — Reflection answers for the lab.
- `known_issue_table_lab5.pdf` — PDF containing the known issue table.

## 5. Issues Identified and Fixes Applied

The following types of issues were addressed during static code analysis:

1. Missing module and function docstrings.
2. Mutable default argument in the trip logging function.
3. Function naming convention violations.
4. Broad exception handling and suppressed errors.
5. Potentially insecure random selection.
6. File handling and resource management improvements.
7. Incorrect or unsafe handling of route lookups and average-load calculations.
8. Blank-line and line-length violations.

The detailed issue descriptions and corresponding fixes are documented in `issues.md`.

## 6. Before-and-After Analysis

The three static analysis tools were executed before and after modifying the source code.

| Tool | Before Fixes | After Fixes |
|---|---|---|
| Pylint | 6.25/10 | 10.00/10 |
| Bandit | 2 low-severity findings | No issues identified |
| Flake8 | Multiple formatting violations | No formatting violations |

## 7. Commands Used

Install the tools:

```bash
python -m pip install pylint bandit flake8
```

Run Pylint:

```bash
python -m pylint shuttle_system.py
```

Run Bandit:

```bash
python -m bandit -r shuttle_system.py
```

Run Flake8:

```bash
python -m flake8 shuttle_system.py
```

Save reports to files:

```bash
python -m pylint shuttle_system.py > pylint_report_after.txt 2>&1
python -m bandit -r shuttle_system.py > bandit_report_after.txt 2>&1
python -m flake8 shuttle_system.py > flake8_report_after.txt 2>&1
```

## 8. Final Results

- **Pylint:** 10.00/10.
- **Bandit:** No issues identified.
- **Flake8:** No formatting violations.
- The corrected program was executed to verify its behaviour.
- Before-and-after reports were saved for comparison.

## 9. Conclusion

This lab demonstrated how static code analysis can improve Python software quality. Pylint helped improve documentation and coding conventions, Bandit helped identify security-related concerns, and Flake8 helped enforce consistent formatting.

Fixing the identified issues improved the readability and maintainability of the Campus Shuttle System and provided practical experience with static analysis tools.
