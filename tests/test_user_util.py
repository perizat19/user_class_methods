import unittest
from user_util import UserUtil
from user import User


class TestUserUtil(unittest.TestCase):

    def test_generate_email(self):
        user1 = User(230121004, 'Perizat', 'Kunduzbekova',
                     'perizat.kunduzbekova@alatoo.edu.com', '12jnPerizat',
                     '2005-06-12')
        self.assertEqual(user1.email, UserUtil.generate_email('Perizat', 'Kunduzbekova',
                                                           'alatoo.edu'))

    def test_validate_email(self):
        user1 = User(230121004, 'Perizat', 'Kunduzbekova',
                     'perizat.kunduzbekova@alatoo.edu.com', '12jnPerizat',
                     '2005-06-12')
        self.assertTrue(UserUtil.validate_email('perizat.kunduzbekova@alatoo.edu.com'))

    def test_is_strong_password(self):
        password = UserUtil.generate_password()
        self.assertTrue(UserUtil.is_strong_password(password))