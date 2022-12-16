from validation import *


def main():
    username = input("Username: ")
    password = input("Password: ")

    errors, index = calc_strength(username, password)

    for error in errors:
        print(error)
    
    if 0 <= index <= 5:
        strength = "Very Weak"

    elif 6 <= index <= 9:
        strength = "Weak"

    elif 10 <= index <= 12:
        strength = "Moderate"

    elif 13 <= index <= 14:
        strength = "Strong"

    else:
        strength = "Very Strong"

    print(f"Password is {strength}.")




# Checks strength of password
def calc_strength(usr, pswd):
    errors = []  # Errors to guide users
    str_index = 0  # Strength index to judge password
    
    # Length
    if not check_length(pswd):
        errors.append("Password is less than 8 characters.")
        str_index += 0
    else:
        str_index += 3

    # Uppercase
    if not check_upper(pswd):
        errors.append("Password does not contain any uppercase letters.")
        str_index += 0
    else:
        str_index += 1

    # Lowercase
    if not check_lower(pswd):
        errors.append("Password does not contain any lowercase letters.")
        str_index += 0
    else:
        str_index += 1

    # Numbers
    if not check_digit(pswd):
        errors.append("Password does not contain any numbers.")
        str_index += 0
    else:
        str_index += 2

    # Special Chars
    if not check_special(pswd):
        errors.append("Password does not contain any special characters from the following: !@#$%^&*()-+.")
        str_index += 0
    else:
        str_index += 2

    # Similar to username
    if not check_unique(usr, pswd):
        errors.append("Password should not contain sequences from your username.")
        str_index += 0
    else:
        str_index += 2

    # Common Password
    if not check_common(pswd):
        errors.append("Password contains commonly used phrases.")
        str_index += 0
    else:
        str_index += 4

    return errors, str_index
    

if __name__ == "__main__":
    main()