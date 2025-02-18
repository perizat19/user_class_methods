import self
from user import User
from collections import defaultdict


class UserService:

    users = {}

    @classmethod
    def add_user(cls, user):
        cls.users[user.user_id] = user

    @classmethod
    def find_user(cls, user_id):
        for i in cls.users.items():
            if user_id in cls.users:
                print(cls.users[i])

    @classmethod
    def delete_user(cls, user_id):
        if user_id in cls.users:
            del cls.users[user_id]

    @classmethod
    def update_user(cls, user_id, user_update):
        if user_id in cls.users:
            cls.users[user_id] = user_update
        else:
            return f"User with the user_id {user_id} is not found"

    @classmethod
    def get_number(cls):
        num = len(cls.users)

        return num
