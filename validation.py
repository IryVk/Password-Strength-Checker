# Global variables to use in checks
SPECIAL = "!@#$%^&*()-+."
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER = "abcdefghijklmnopqrstuvwxyz"


# A temporary main function to test our checks
def main():
    ...


# Checks if password is at least 8 characters long
def check_length(pswd):
    l = len(pswd)
    if l >= 8:
        return True
    return False


# Checks if password contains a uppercase character
def check_upper(pswd):
    for char in pswd:
        if char in UPPER:
            return True
    return False


# Checks if password contains a lowercase character
def check_lower(pswd):
    for char in pswd:
        if char in LOWER:
            return True
    return False


# Checks if password contains number
def check_digit(pswd):
    for char in pswd:
        if char.isdigit():
            return True
    return False


# Checks if password contains special characters
def check_special(password):
    for char in password:
        if char in SPECIAL:
            return True
    return False


# Checks if password does not contain sequence in user-name
def check_unique(usr, pswd):
    for i in range(len(pswd) - 4):
        if pswd[i : i + 4].lower() in usr.lower():
            return False
    return True


# Checks if passowrd is not in list of common 100,000 passwords
def check_common(pswd):
    # Load list of common passwords in memory
    common = []
    with open("common_large.txt") as file:
        for line in file:
            common.append(line.rstrip())

    # Compare password with common passwords
    for password in common:
        if pswd.lower() == password:
            return False
    return True


# Check if there's a sequence or pattern in characters such as : 123 , 369, abc etc.
def check_seq(pswd):
    pswd = pswd.lower()
    for i in range(len(pswd) - 2):
        # Checks if no 3 characters are in a sequence/have a pattern
        if ord(pswd[i + 2]) - ord(pswd[i + 1]) == ord(pswd[i + 1]) - ord(pswd[i]):
            return False
    return True


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
        errors.append(
            "Password does not contain any special characters from the following: !@#$%^&*()-+."
        )
        str_index += 0
    else:
        str_index += 2

    # Similar to username
    if not check_unique(usr, pswd):
        errors.append("Password should not contain sequences from your username.")
        str_index += 0
    else:
        str_index += 2

    # Sequence or pattern
    if not check_seq(pswd):
        errors.append("Password contains a repeated pattern/characters in sequence.")
        str_index += 0
    else:
        str_index += 2

    # Common Password
    if not check_common(pswd):
        errors.append("Password is a commonly used password.")
        str_index += 0
    else:
        str_index += 4

    # Decides strength based on the strength index
    if 0 <= str_index <= 7:
        strength = "Very Weak"
    elif 8 <= str_index <= 11:
        strength = "Weak"
    elif 12 <= str_index <= 14:
        strength = "Moderate"
    elif 15 <= str_index <= 16:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return errors, strength


if __name__ == "__main__":
    main()
