# login code
import mysql.connector 

# Setting up database
mydb = mysql.connector.connect(
    host="localhost",
    user="standardUser",
    password="StandardPassword123!",
    database="ComputerScienceNEA"
)

def validate_new_password(password): # checks if the password is 8+ characters & contains a special character
    if (len(password) < 8) or (len(password) > 128):
        return "Length" # invalid password length
    else:
        for character in password:
            if not (character.isalpha() or character.isdigit()):
                return True # password contains special character
        return "Character" # password doesn't contain special character

def validate_new_username(username, mydb): # checks if username is between 1-128 characters & is unique
    mycursor = mydb.cursor()
    if (len(username) == 0 or len(username) > 128):
        return False # invalid username length
    else:
        username_exists_sql = "SELECT * FROM USERS WHERE username=%s"
        value = (username, )
        mycursor.execute(username_exists_sql, value)
        myresult = mycursor.fetchone()
        if myresult is None:
            return True # username doesn't exist
        else:
            return "Exists" # username already exists

def get_password(username, mydb): # collects the stored password for the given username in the database
    mycursor = mydb.cursor()
    check_password_sql = "SELECT password FROM USERS WHERE username=%s"
    value = (username, )
    mycursor.execute(check_password_sql, value)
    password = mycursor.fetchone()
    if password is None:
        return "" # when no password or username doesn't exist
    else:
        return password # found password
    
def validate_login(username, input_password, mydb): # checks if stored password matches inputted one for given account name
    account_password = get_password(username, mydb)
    account_password = "".join(account_password)
    if account_password == "" or username == "":
        return False
    elif account_password == input_password:
        return True # right password, logging in
    else:
        return False # incorrect password

def saving_new_account(username, password, mydb): # validates & saves new account data from text fields
    is_valid_password = validate_new_password(password)
    is_valid_username = validate_new_username(username, mydb)
    if (is_valid_password != ("Character") and is_valid_password != "Length") and is_valid_username == True:
        new_account = Account(username, password)
        new_account.save_user_password(mydb)
        return True
    elif is_valid_password == "Length":
        return "Length" # password wrong length
    elif is_valid_password == "Character":
        return "Character" # password doesn't have a special character
    elif is_valid_username == "Exists":
        return "Exists" # username isn't unique
    elif not is_valid_username:
        return "Username" # username is wrong length


class Account:
    '''
    This class encapsulates all information to do with a user's account.
    '''
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_user_password(self, mydb): # saves username & password into database
        mycursor = mydb.cursor()
        save_sql = "INSERT INTO USERS (username, password) VALUES (%s, %s)"
        values = (self.username, self.password)
        mycursor.execute(save_sql, values)
        mydb.commit()

mydb.close()