from user import User
import datetime
from user_service import UserService
from user_util import UserUtil

if __name__ == '__main__':
    print('Hello')

user1 = User(230121004, 'Perizat', 'Kunduzbekova', 'perizat.kunudzbekova@alatoo.edu.kg', '12jnPerizat', '2005-06-12')
user1.get_age()

UserService.add_user(user1)