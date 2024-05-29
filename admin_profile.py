import classs
import admin_page


def settings(username, password):
    print(classs.User.full_info(username, password))
    services = input("""
         1.First name
         2.Last name
         3.Password
         4.Ful info
         0. Back
               >>>""")

    if services == "1":
        new_first_name = input("Enter your New first name: ")
        print(classs.User.set_first_name(new_first_name, username, password, "first_name"))

    elif services == "2":
        new_last_name = input("Enter your New last name: ")
        print(classs.User.set_first_name(new_last_name, username, password, "last_name"))

    elif services == "3":
        new_password = input("Enter your New password: ")
        print(classs.User.set_first_name(new_password, username, password, "password"))

    elif services == "4":
        new_first_name = input("Enter your New  furst name information: ")
        new_last_name = input("Enter your New last name information: ")
        new_username = input("Enter your New  username information: ")
        new_password = input("Enter your New password information: ")
        print(classs.User.update_full_data(new_first_name, new_last_name, new_username, new_password, old_username=username))
        return profile(new_username, new_password)


def profile(username, password):
    menu = input("""
    1. Sittings
    0. Back
       >>>""")
    if menu == "1":
        return settings(username, password)

    elif menu == "0":
        return admin_page.landing_page(username, password)
