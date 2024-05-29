import classs
import user_profile


def landing_page(username, password):
    print("Welcome user page")
    services = input(f"""
       1. Curses
       2. Profile
            >>>""")
    if services == "1":
        classs.Course.get_all_courses()
        back = input("0. Back\n\t>>>")
        if back == "0":
            return landing_page(username, password)

    elif services == "2":
        return user_profile.profile(username, password)








