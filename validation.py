SPECIAL = "!@#$%^&*()-+."
UPPER = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
LOWER = ("abcdefghijklmnopqrstuvwxyz")

def main():
    ...


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
def check_unique():
    ...


def check_common():
    # Load list of common passwords in memory
    ...


if __name__ == "__main__":
    main()