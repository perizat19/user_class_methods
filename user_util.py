import string
from datetime import date
import random
import string
import re


class UserUtil:

    @staticmethod
    def generate_user_id():
        curr_date = date.today()
        curr_year = str(curr_date.year)
        id_start = curr_year[2:]
        random_num = str(random.randint(1000000, 9999999))
        new_id = id_start + random_num
        return new_id

    @staticmethod
    def generate_password():
        length = 8
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.whitespace, k=length))

        return password

    @staticmethod
    def is_strong_password(password):
        if (string.ascii_letters and string.digits and string.whitespace) not in password:
            return ("Your password must contain minimum 8 characters, at least 1 uppercase, 1 lowercase, 1 digit and 1 "
                    "special character")
        else:
            return "Your password is strong"

    @staticmethod
    def generate_email(name, surname, domain):
        email = f'{name.lower()}.{surname.lower()}@{domain}.com'

        return email

    def lower(self):
        pass

    @staticmethod
    def validate_email(email):
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(email_pattern, email):
            return True
        else:
            return False







