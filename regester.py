import login
from classs import User
def regester():
    print("Regester page")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    username = input("Usename: ")
    password = input("Password: ")
    user = User(first_name, last_name, username, password)
    user.save()
    return login.login()
