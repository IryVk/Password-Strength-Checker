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
    for i in range(len(pswd)):
        try:
            if pswd[i : i + 4].lower() in usr.lower():
                return False
        except IndexError:  # Once it reaches end of password i.e. raises index error, return
            return True


# Checks if passowrd is not in list of common passwords
def check_common(pswd):
    # Load list of common passwords in memory
    common = []
    with open("common.txt") as file:
        for line in file:
            common.append(line.rstrip())

    # Compare password with common passwords
    for password in common:
        if pswd.lower() == password.lower():
            return False
    return True


if __name__ == "__main__":
    main()
