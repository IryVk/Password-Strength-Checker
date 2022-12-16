SPECIAL = "!@#$%^&*()-+."
UPPER = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
LOWER = ("abcdefghijklmnopqrstuvwxyz")

def main():
    password = input("Password: ")
    print(check_common(password))

def check_length(pss):

    L = len(pss)
    if L >= 8:
        print("good len ")
        return True
    else:
        return False
        





def check_upper(pss):
    for ad in (pss):
        L = UPPER
        if ad in L:
            print("it has upper")
            return True
    return False
    



def check_lower(pss):
    for ad in (pss):
        L = LOWER
        if ad in L:
            print("it has lower ") 
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