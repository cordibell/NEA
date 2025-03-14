# Login GUI module, created 17/07/24
import tkinter as tk
from tktooltip import ToolTip
from tkinter import messagebox
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="standardUser",
    password="StandardPassword123!",
    database="ComputerScienceNEA"
)

class Login: # encapsulates data from entry & window into a class to easily move it to main.py
    '''
    This class encapsulates data from the entry boxes as well as error messages for the window.
    '''
    def __init__(self, login_window, new_username, new_password, existing_username, existing_password):
        self.login_window = login_window
        self.new_username = new_username
        self.new_password = new_password
        self.existing_username = existing_username
        self.existing_password = existing_password

    def get_new_username(self):
        return self.new_username.get()
    
    def get_new_password(self):
        return self.new_password.get()
    
    def get_existing_username(self):
        return self.existing_username.get()
    
    def get_existing_password(self):
        return self.existing_password.get()
    
    # Error message methods

    def invalid_password_length(self):
        messagebox.showerror("Invalid password", "Password must be between 8-128 characters")
    
    def invalid_password_character(self):
        messagebox.showerror("Invalid password", "Password must contain a special character")
    
    def invalid_username_length(self):
        messagebox.showerror("Invalid username", "Username must be between 1-128 characters")
    
    def invalid_username_exists(self):
        messagebox.showerror("Invalid username", "Username already exists")
    
    def incorrect_password(self):
        messagebox.showerror("Incorrect password", "Incorrect password. Try again")
    
    def made_new_account(self):
        messagebox.showinfo("Made new account", "Successfully created a new account")
    

def login_menu(login_command, new_account_command): # contains all the widgets for the login GUI
    '''
    This function contains all of the widgets for the login menu.
    '''
    # tkinter windows

    login_window = tk.Tk()
    login_window.title("Login Menu")
    login_window.geometry("1050x800")

    # Constructing the two frames for this component
    existing_account_frame = tk.Frame(login_window)
    create_account_frame = tk.Frame(login_window)

    # Constructing the border frames for the titles & text fields

    border_colour_existing_account = tk.Frame(existing_account_frame, bg="red")
    border_colour_create_account = tk.Frame(create_account_frame, bg="red")

    border_colour_existing_username = tk.Frame(existing_account_frame, highlightbackground="orange", highlightthickness=2)
    border_colour_existing_password = tk.Frame(existing_account_frame, highlightbackground="orange", highlightthickness=2)

    border_colour_new_username = tk.Frame(create_account_frame, highlightbackground="orange", highlightthickness=2)
    border_colour_new_password = tk.Frame(create_account_frame, highlightbackground="orange", highlightthickness=2)


    # Constructing the label widgets for the titles
    existing_account_title = tk.Label(
        border_colour_existing_account,
        text="SIGN INTO AN EXISTING ACCOUNT",
        font=("Arial", 26, "bold"),
        width=25,
        anchor="n",
        wraplength=350,
        justify="center"
    )
    create_account_title = tk.Label(
        border_colour_create_account,
        text="CREATE AN ACCOUNT",
        font=("Arial", 26, "bold"),
        width=25,
        anchor="n",
        wraplength=350,
        justify="center"
    )
    # Using the grid manager to display the two frames
    existing_account_frame.grid(row=0, column=0)
    create_account_frame.grid(row=0,column=1)

    # Packing the two titles alongside their border colours onto the window
    existing_account_title.pack(padx=3,pady=3)
    create_account_title.pack(padx=3,pady=3)
    border_colour_existing_account.pack(padx=20,pady=20)
    border_colour_create_account.pack(padx=20,pady=20)

    # Creating an enter username and password box for each option
    # Signing into an existing account
    existing_username_entry = tk.Entry(border_colour_existing_username,
                                borderwidth=2,
                                font=("Arial", 12)
                                )

    existing_username_entry_label = tk.Label(border_colour_existing_username,
                                            text="Username",
                                            font=("Arial", 14, "italic"),
                                            anchor="w"
                                    )

    existing_password_entry = tk.Entry(border_colour_existing_password,
                                borderwidth=2,
                                font=("Arial", 12),
                                show="•"
                            )

    existing_password_entry_label = tk.Label(border_colour_existing_password,
                                            text="Password",
                                            font=("Arial", 14, "italic"),
                                            anchor="w"
                                    )
    # Create new account
    new_username_entry = tk.Entry(border_colour_new_username,
                                borderwidth=2,
                                font=("Arial", 12)
                                )

    new_username_entry_label = tk.Label(border_colour_new_username,
                                            text="Enter a username",
                                            font=("Arial", 14, "italic"),
                                            anchor="w"
                                    )

    new_password_entry = tk.Entry(border_colour_new_password,
                                borderwidth=2,
                                font=("Arial", 12),
                                show="•"
                            )

    new_password_entry_label = tk.Label(border_colour_new_password,
                                            text="Enter a password",
                                            font=("Arial", 14, "italic"),
                                            anchor="w"
                                    )

    # Confirmation buttons
    confirm_sign_in_button = tk.Button(existing_account_frame,
                                activebackground="green",
                                bg="red",
                                text="Confirm sign in",
                                font=("Arial", 14, "bold"),
                                command=login_command
    )
    confirm_create_account_button = tk.Button(create_account_frame,
                                            activebackground="green",
                                            bg="red",
                                            text="Create account",
                                            font=("Arial", 14, "bold"),
                                            command=new_account_command
    )

    # Packing existing usernames
    existing_username_entry_label.pack(padx=1, pady=1)
    existing_username_entry.pack(padx=20,ipady=3, pady=10)
    border_colour_existing_username.pack(padx=15, pady=5)

    # Packing existing passswords
    existing_password_entry_label.pack(padx=1, pady=1)
    existing_password_entry.pack(padx=20, ipady=3, pady=10)
    border_colour_existing_password.pack(padx=15, pady=5)

    # Packing new usernames
    new_username_entry_label.pack(padx=1, pady=1)
    new_username_entry.pack(padx=20,ipady=3, pady=10)
    border_colour_new_username.pack(padx=15, pady=5)

    # Packing new passwords
    new_password_entry_label.pack(padx=1, pady=1)
    new_password_entry.pack(padx=20, ipady=3, pady=10)
    border_colour_new_password.pack(padx=15, pady=5)

    # Packing confirmation buttons
    confirm_sign_in_button.pack(padx=20, pady=10)
    confirm_create_account_button.pack(padx=20, pady=10)

    # Tooltips to show the user the expected inputs
    ToolTip(existing_username_entry_label, msg="Enter your username")
    ToolTip(existing_password_entry_label, msg="Enter your password")

    ToolTip(new_username_entry_label, msg="Must be between 1-128 characters")
    ToolTip(new_password_entry_label, msg="Must be 8+ characters and contain a special character")

    # return login_window
    return Login(login_window, new_username_entry, new_password_entry, existing_username_entry, existing_password_entry)
