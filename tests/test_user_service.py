import unittest
from user_service import UserService
from user import User


class TestUserService(unittest.TestCase):

    def test_find_user(self):
        user1 = User(230121004, 'Perizat', 'Kunduzbekova',
                     'perizat.kunudzbekova@alatoo.edu.com', '12jnPerizat',
                     '2005-06-12')
        UserService.add_user(user1)
        self.assertIn(user1.user_id, UserService.users)

    def test_get_number(self):
        user2 = User(230946712, 'Ali', 'Kanatbekov',
                     'ali.kanatbekov@alatoo.edu.com', '12jlAli', '2006-12-22')
        UserService.add_user(user2)

        user3 = User(230245013, 'Kanykey', 'Asanova',
                     'kanykey.asanova@alatoo.edu.com', '34fKany', '2005-04-23')
        UserService.add_user(user3)

        self.assertNotEqual(UserService.get_number(), 3)

    def test_delete_user(self):
        user2 = User(230946712, 'Ali', 'Kanatbekov',
                     'ali.kanatbekov@alatoo.edu.kg', '12jlAli', '2006-12-22')
        UserService.add_user(user2)
        UserService.delete_user(230946712)

        self.assertTrue(user2 not in UserService.users)
