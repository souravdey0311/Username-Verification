# Username-Verification
Command-line login simulator that checks a username and locks the user out after three failed attempts.
# Login Attempt Lockout

A command-line program that asks for a username and locks the user out after three incorrect attempts.

## Features

- Accepts a username in any letter case and ignores extra spaces
- Tracks failed attempts and shows how many remain
- Locks the session after three incorrect tries

## Requirements

- Python 3.x

## Usage

Run the program:

```bash
python "Username Verification.py"
```

Enter a username when prompted. The correct username is `SKD`.

Enter a username when prompted. The correct username is `SKD`.

Example:

```
Enter username: abc
INCORRECT USERNAME. Attempt 1 of 3
You have 2 attempts remaining out of 3
Enter username: skd
Welcome SKD
```

## What I Learned

- Using `while True` loops with `break` to control program flow
- Cleaning user input with `strip()` and `upper()`
- Tracking state with a counter variable
- Using conditional statements to display different messages based on progress
