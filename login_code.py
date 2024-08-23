# login code
import tkinter as Tk

class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save(self):
        print("Saving object to database")

def createAccount(username, password):
    print(username, password)
    return Account(username, password)