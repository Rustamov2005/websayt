import login
import regester


def main():
    web = input("""
     1. Login
     2. Register
           >>>>""")
    if web == "1":
        return login.login()
    elif web == "2":
        return regester.regester()
    else:
        print("Error")


if __name__ == "__main__":
    main()
