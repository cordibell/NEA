# login code
import tkinter as Tk

class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def createAccount():
    username = new_username_entry.get("1.0", "end-1c") 
    password = new_password_entry.get("1.0", "end-1c")
    return username, password

accountDetails = list(createAccount())
account = Account(accountDetails[0], accountDetails[1])