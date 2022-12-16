SPECIAL = "!@#$%^&*()-+."
UPPER = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
LOWER = ("abcdefghijklmnopqrstuvwxyz")

def main():
    ...

def check_length(pswd):
    l = len(pswd)
    if l >= 8:
        return True

    return False
        





def check_upper(pswd):
    for char in pswd:
        if char in UPPER:
            return True

    return False
    



def check_lower(pswd):
    for char in pswd:
        if char in LOWER:
            return True

    return False


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