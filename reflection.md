# Reflection — Static Code Analysis

## 1. What did you learn from static code analysis?

Static code analysis helped identify coding problems without executing the program. Pylint improved code quality and readability, Bandit identified potential security issues, and Flake8 detected formatting violations.

## 2. Which tool was the most useful and why?

Pylint was useful because it identified several code quality issues, including missing docstrings, a mutable default argument, and naming convention violations. It also provided a numerical score to measure code quality.

## 3. What challenges did you face while fixing the issues?

The main challenges were correcting the mutable default argument, removing broad exception handling, improving file handling, and fixing the crash caused by accessing a route after it had been removed. These changes required checking the program's behavior after editing.

## 4. How did static code analysis improve your program?

Static code analysis improved code readability, maintainability, and error handling. The final Pylint score increased from 6.25/10 to 10.00/10, Bandit reported zero issues, and Flake8 reported no formatting violations.