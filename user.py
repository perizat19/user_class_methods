from datetime import datetime

class User:

    def __init__(self, user_id, name, surname, email, password, birthday=datetime):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.email = email
        self.__password = password
        self.birthday = birthday

    def get_details(self):
        return f"User id: {self.user_id}\n"\
               f"User name: {self.name}\n"\
               f"Surname: {self.surname}\n"\
               f"Email: {self.email}\n"\
               f"Password: {self.__password}\n"\
               f"Birthday: {self.birthday}"

    def get_age(self):
        age = datetime.today().year - datetime.strptime(self.birthday, '%Y-%m-%d').year
        return age



    
