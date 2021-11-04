from bot import Bot
from getpass import getpass
import time

def main():
    username = input('Username: ')
    password = getpass('Password: ')
    bot = Bot()
    if not bot.is_logged_in():
        bot.login(username, password)
    bot.find_studies()


if __name__ == '__main__':
    main()