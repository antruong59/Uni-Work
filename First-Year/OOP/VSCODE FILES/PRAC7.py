#
# COMP 1046 OOP
# Practical 7
#

import hashlib

# User class
class User:
    def __init__(self, username, password):
        #Create a new user object. The password will be encrypted before storing. 
        self.username = username
        self.password = self._encrypt_pw(password)
        self.is_logged_in = False

    def _encrypt_pw(self, password):
        #Encrypt the password with the username and return the sha digest. 
        hash_string = self.username + password
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self, password):
        #Return True if the password is valid for this user, false otherwise. 
        encrypted = self._encrypt_pw(password)
        return encrypted == self.password


# Exceptions
class AuthException(Exception):
    def __init__(self, username):
        super().__init__(username)
        self.username = username
    
class UsernameAlreadyExists(AuthException): 
    pass

class PasswordTooShort(AuthException):
    pass

class InvalidUsername(AuthException):
    pass

class InvalidPassword(AuthException):
    pass


class Authenticator:
    def __init__(self):
        self.users = {} #username, User

    def add_user(self, username, password):
        if len(password) < 6:
            raise PasswordTooShort(username)
        
        if username in self.users:
            raise UsernameAlreadyExists(username)
    
        self.users[username] = User(username,password)

    def login(self, username, password):
        if username not in self.users:
            raise InvalidUsername(username)
        
        if self.users[username].check_password(password) == False: 
            raise InvalidPassword(username)

        self.users[username].is_logged_in = True
        return User(username, password).is_logged_in    

    def is_logged_in(self, username):
        if username in self.users:
            return self.users[username].is_logged_in
        else:
            return False

auth = Authenticator()
try:
    auth.add_user("johnny", "johnnypassword")
    print(auth.is_logged_in("johnny"))
    auth.login("johnny", "joepassword")
except AuthException as e:
    print(type(e).__name__, e.username)
try:
    auth.login("johnny", "johnnypassword")
    print(auth.is_logged_in("johnny"))
    auth.add_user("johnny", "newpassword")
except AuthException as e:
    print(type(e).__name__, e.username)
try:
    auth.login("susi", "123")
except AuthException as e:
    print(type(e).__name__, e.username)
try:
    auth.add_user("susi", "123")
except AuthException as e:
    print(type(e).__name__, e.username)