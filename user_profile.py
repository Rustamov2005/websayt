import classs


def settings(username, password):
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
        new_full_info = input("Enter your New full information: ")
        print(classs.User.set_first_name(new_full_info, username, password, "last_name"))


def profile(username, password):
    menu = input("""
           1. My Course
           2. Settings
           0. Back
               >>>""")

    if menu == "1":
        for course in classs.User.active_course(username, password):
            print(course)

    elif menu == "2":
        return settings(username, password)
