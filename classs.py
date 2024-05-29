from datetime import datetime
import json
import admin_page
import user_page


class User:
    """Bu yirga foydalanuvchi haqida malumot kirtiladi"""
    def __init__(self, first_name: str, last_name: str, username: str, password: str):
        """
        Bu yirda biz foydalanuvchi haqida malumotlar elon qildik
        :param first_name:
        :param last_name:
        :param username:
        :param password:
        """
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.__password = password
        self.status = "user"
        self.courses = []
        self.create_date = f"{datetime.now()}"

    @staticmethod
    def see():
        """Bu metod orqali biz saytdagi kurslar haqida malumot olamiz"""
        with open("data/curses.json", encoding="utf-8") as file:
            data = json.load(file)
            for i in data["curses"]:
                print(f"""
                  Name:{i["name"]}
                  Modul: {i["modul"]}
                  Teacher: {i["teacher"]}
                  Price: {i["price"]}
                  Time: {i["time"]}
                  Location: {i["location"]}
                """)

    def regester(self):
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        username = input("Usename: ")
        password1 = input("Password1: ")
        password2 = input("Password2: ")

    @property
    def get_password(self):
        """Bu metod orqali biz passwordni himoyalangan holatga keltirdik"""
        return self.__password

    @staticmethod
    def full_info(username, password):
        """Bu metod orqali biz foydalanuvchi haqida to'liq malumot olamiz"""
        with open("data/users.json", encoding="utf-8") as file:
            data = json.load(file)
            for user in data["users"]:
                if user["username"] == username and user["password"] == password:
                    return f"""
                    First name: {user["first_name"]} 
                    Last name: {user["last_name"]}
                    Username: {user["username"]}
                    Password: {user["password"]}
                    """

    @staticmethod
    def all_users():
        """Bu  etod orqali biz saytdagi barcha foydalanuvhcular ro'yxatini ko'rishimiz mumkun"""
        with open("data/users.json", encoding="utf-8") as file:
            data = json.load(file)
            for user in data["users"]:
                print(user)

    @staticmethod
    def active_course(username, password):
        with open("data/users.json", encoding="utf-8") as file:
            data = json.load(file)
            for user in data["users"]:
                if user["username"] == username and user["password"] == password:
                    courses = user["courses"]
                    return courses
    @staticmethod
    def update_full_data(new_first_name, new_last_name, new_username, new_password, old_username):
        # new_user = {
        #     "first_name": self.first_name,
        #     "last_name": self.last_name,
        #     "username": self.username,
        #     "password": self.get_password,
        #     "status": self.status,
        #     "courses": [],
        #     "create_date": self.create_date
        # }

        with open("data/users.json", encoding="utf-8") as file:
            data = json.load(file)
            users = data["users"]
            for user in users:
                if user["username"] == old_username:
                    check_user = user

            users.remove(check_user)
            check_user["first_name"] = new_first_name
            check_user["last_name"] = new_last_name
            check_user["username"] = new_username
            check_user["password"] = new_password
            check_user["last_update"] = f"{datetime.now()}"
            users.append(check_user)
            data["users"] = users

            with open("data/users.json", "w") as f:
                json.dump(data, f, indent=4)

        return "Successfully"


    def save(self):
        """Bu metod orqali biz yangi foydalanuvchi qo'shamiz"""
        with open("data/users.json", encoding="utf-8") as file:
            data = json.load(file)

        with open("data/users.json", "w") as f:
            new_user = {
                  "first_name": self.first_name,
                  "last_name": self.last_name,
                  "username": self.username,
                  "password": self.get_password,
                  "status": self.status,
                  "courses": [],
                  "create_date": self.create_date
              }
            data["users"].append(new_user)
            json.dump(data, f, indent=6)
            print("Successfully Regester")

    @staticmethod
    def check_user(username, password):
          """Bu metod foydalanuchini password va usernameni tekshirib beradi"""
          with open("data/users.json", encoding="utf-8") as file:
            data = json.load(file)
            for user in data["users"]:
                if user["username"] == username and user["password"] == password:
                    if user["status"] == "admin":
                        return admin_page.landing_page(username, password)
                    else:
                        return user_page.landing_page(username, password)
            return False

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @staticmethod
    def set_first_name(new_first_name, username, password, atribut):
        with open("data/users.json", encoding="utf-8") as file:
            data = json.load(file)
            users = data["users"]
            for user in users:
                if user["username"] == username and user["password"] == password:
                    check_user = user
            users.remove(check_user)
            check_user[atribut] = new_first_name
            users.append(check_user)
            data["users"] = users

        with open("data/users.json", "w") as f:
            json.dump(data, f, indent=6)

        return "Saccessfully change"




class Course:
    def __init__(self, title: str, description: str, price: str, modules: int, mintor: str):
        self.title = title
        self.description = description
        self.price = price
        self.modules = modules
        self.mintor = mintor
        self.create_date = f"{datetime.now()}"

    @staticmethod
    def get_all_courses():
        with open("data/curses.json", encoding="utf-8") as file:
            data = json.load(file)
            for course in data["courses"]:
                print(f"""
                   Title: {course["title"]}
                   Description: {course["description"]}
                   Price: {course["price"]}
                   Modules: {course["modules"]}
                   Mintor: {course["mintor"]}                   
                """)



