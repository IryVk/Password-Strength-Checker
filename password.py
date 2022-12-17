from validation import calc_strength


def main():
    # Gets username and password from user
    username = input("Username: ")
    while True:
        try:
            password = input("Password: ")
            # If user inputs a user that is shorter than 3 characters, raise an error and re-prompt
            if len(password) < 3:
                print("Password is too short, please enter at least 3 characters.")
                raise ValueError
            break
        except ValueError:
            pass

    # Get errors and strength index
    errors, strength = calc_strength(username, password)

    # Print any errors to guide the user
    for error in errors:
        print(error)

    print(f"Password is {strength}.")


if __name__ == "__main__":
    main()
