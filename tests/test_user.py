import unittest
from user import User


class TestUser(unittest.TestCase):

    def test_get_age(self):
        user1 = User(230121004, 'Perizat', 'Kunduzbekova',
                     'perizat.kunudzbekova@alatoo.edu.kg', '12jnPerizat',
                     '2005-06-12')
        self.assertEqual(user1.get_age(), 20)


