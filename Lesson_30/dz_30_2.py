import hashlib


def passwords():
    passwords = {}
    with open("passwords.txt", "r") as f:
        for line in f:
            line = line.strip().split(":")
            passwords[line[0]] = line[1]
    return passwords


def encoding(password):
    encoded = hashlib.md5(password.encode()).hexdigest()
    return encoded


def registration(login, password, passwords):
    passwords[login] = password
    with open("passwords.txt", "w") as f:
        for i in passwords:
            f.write(i + ":" + passwords[i] + "\n")


def verification_login(login, passwords):
    if login in passwords:
        return True
    else:
        return False


def verification_password(login, encoded, passwords):
    if encoded == passwords[login]:
        return True
    else:
        return False


def start():
    while True:
        greeting = input("Hello and welcome to the database. Are you registered user? (Y/N)")
        if greeting == "N":
            login = input("Please, enter your login:")
            if not verification_login(login, passwords):
                password = input("Please, enter your password:")
                password = encoding(password)
                registration(login, password, passwords)
                print(f"User {login} has been added to database.")
                break
            else:
                print("User with this login already exists. Please, choose another one.")
                start()
        elif greeting == "Y":
            login = input("Please, enter your login:")
            password = input('Please, enter your password:')
            encoded = encoding(password)
            if verification_login(login, passwords) and verification_password(login, encoded, passwords):
                print(f"Welcome, {login}. Access granted.")
                break
            else:
                incorrect = input("Login or password are incorrect. Try again? (Y/N)")
                if incorrect == "Y":
                    start()
                else:
                    print("Access denied.")
                    break
        else:
            start()


if __name__ == "__main__":
    passwords = passwords()
    start()
