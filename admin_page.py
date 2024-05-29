import classs
import admin_profile




def landing_page(username, password):
    print("Welcome admin page")
    sesveses = input(f"""
       1. Users
       2. Curses
       3. Profile
            >>>""")
    if sesveses == "1":
        classs.User.all_users()
        return landing_page(username, password)

    elif sesveses == "2":
        classs.Course.get_all_courses()
        return landing_page(username, password)

    elif sesveses == "3":
        return admin_profile.profile(username, password)



