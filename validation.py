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


def check_digit():
    ...


def check_special():
    ...


# TO-DO
def check_unique(usr, pswd):
    for i in range(len(pswd)):
        try:
            if pswd[i:i+4] in usr:
                return False
        except IndexError:
            break

    return True


def check_common():
    # Load list of common passwords in memory
    ...


if __name__ == "__main__":
    main()