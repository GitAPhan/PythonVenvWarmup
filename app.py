from getpass import getpass
import dbinteractions as db

username = input('Please enter your username: ')
password = getpass('Please enter your password: ')

login_status, user_id = db.attempt_login(username, password)

if login_status:
    db.show_user_dogs(user_id)