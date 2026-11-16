# Password Checker

Command-line Python program that rates a password's strength.

**Status:** work in progress.

## What it does today
- Asks the user for a password with `input()`
- Rates it by length: Weak (under 8), Medium (8 to 11), Strong (12+)
- Includes a `specialchecker()` function that detects special characters

## Planned
- Check for digits, uppercase, and lowercase letters
- Mark passwords with no digit or special character as Weak
- Print which checks failed
- Loop until the user types `quit`
- Compare against a list of common passwords

## Run it
```
python password_checker.py
```

The program never stores or sends the password.
