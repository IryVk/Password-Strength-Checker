SPECIAL = "!@#$%^&*()-+."
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER = "abcdefghijklmnopqrstuvwxyz"



def main():
    
  ...  


def check_length():
    ...


def check_upper():
    ...


def check_lower():
    ...


def check_digit(password):
    
    for char in password:
        if char.isdigit():
            return True
    return False



def check_special(password):
    
    for sp in password:
        if sp in SPECIAL:
            return True
    return False

    


# TO-DO
def check_unique():
    ...


def check_common():
    # Load list of common passwords in memory
    ...


if __name__ == "__main__":
    main()