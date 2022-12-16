SPECIAL = "!@#$%^&*()-+."
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER = "abcdefghijklmnopqrstuvwxyz"


def main():
    password = input("Password: ")
    print(check_common(password))


def check_length():
    ...


def check_upper():
    ...


def check_lower():
    ...


def check_digit():
    ...


def check_special():
    ...


# TO-DO
def check_unique():
    ...


def check_common(pswd):
    # Load list of common passwords in memory
    common = []
    with open("common.txt") as file:
        for line in file:
            common.append(line.rstrip())
    
    # Compare password with common passwords
    for password in common:
        if pswd == password:
            return False
    
    return True





if __name__ == "__main__":
    main()