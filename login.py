from classs import User


def login():
    print("Login page")
    username = input("Enter your Usename =>>")
    password = input("Enter your Password =>>")
    if User.check_user(username, password) is False:
        return login()

