Grafical User Interface using PYTHON and MySQL.
# LOGIN-PAGE-PYTHON
GUI (Login page) using PYTHON conneted to MYSQL database.

SIGNUP:

User name and Password must fulfil certain conditions while signup.
CONDITIONS FOR ELIGIBLE USERNAME:
  1.Username must only contain CAPITAL ALPHABETS.
  2.Username must not be EMPTY.
CONDITIONS FOR ELIGIBLE PASSWORD:
  1.Password must contain atleast one charater of the following categories.
      1.Capital letter
      2.Small letter
      3.Number
      4.Special charater
  2.Password must not be empty.
  3.Password must contain 8 to 12 charaters.
User's every suessful signup data will be stored in the Database hih as created in MYSQL.

LOGIN:
If the user enter the appropriate USERNAME AND PASSWORD which was already exist in a database,user an suessfully login their account.
If any of this conditions are not met,the appropriate MESSAGEBOX will POPUP.

# Detailed Summary
A secure user authentication system with login and registration functionality, built with Python, Tkinter for the GUI, and MySQL for database storage.

## Features

- **User Authentication**
  - Secure login with database verification
  - New user registration with validation
- **Password Security**
  - 8-12 character requirement
  - Requires uppercase, lowercase, numbers, and special characters
- **Username Requirements**
  - All uppercase letters enforced
- **User-Friendly Interface**
  - Clear error messages and guidance
  - Form validation with instant feedback
- **Database Integration**
  - MySQL backend for user storage
  - Prevents duplicate usernames

## Prerequisites

- Python 3.x
- MySQL Server
- Required Python packages:
  ```bash
  pip install mysql-connector-python pillow

Usage
Login:

Enter your existing username (all uppercase)

Enter your password

Click "Login" button

Signup:

Choose a new username (all uppercase)

Create a strong password meeting requirements

Click "Signup" button

Screenshots
https://screenshots/login.png
Login interface with form validation

https://screenshots/signup-success.png
Successful registration message

Code Structure
login(): Handles user authentication

signup(): Manages new user registration

clearfun(): Clears form fields

GUI elements: Labels, entry fields, and buttons


![image alt](https://github.com/Ranjid1087/LOGIN-PAGE-PYTHON/blob/bd6324d900fe0882975fafeabb5726ffe681b59d/User%20Interface%20SS.png)


Contributing
Contributions are welcome! Please fork the repository and create a pull request.
