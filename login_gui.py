# Login GUI module, created 17/07/24
import tkinter as tk
import login_code

def collect_new_account():
    username = new_username_entry.get()
    password = new_password_entry.get()
    new_account = login_code.createAccount(username, password)
    new_account.save()

login_window = tk.Tk()
login_window.geometry("1050x800")

# Constructing the two frames for this component
existing_account_frame = tk.Frame(login_window)
create_account_frame = tk.Frame(login_window)

# Constructing the border frames for the titles & text fields

border_colour_existing_account = tk.Frame(existing_account_frame, bg="red")
border_colour_create_account = tk.Frame(create_account_frame, bg="red")

border_colour_existing_username = tk.Frame(existing_account_frame, highlightbackground="red", highlightthickness=2)
border_colour_existing_password = tk.Frame(existing_account_frame, highlightbackground="red", highlightthickness=2)

border_colour_new_username = tk.Frame(create_account_frame, highlightbackground="red", highlightthickness=2)
border_colour_new_password = tk.Frame(create_account_frame, highlightbackground="red", highlightthickness=2)

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
                            font=("Arial", 14, "bold")
)
confirm_create_account_button = tk.Button(create_account_frame,
                                          activebackground="green",
                                          bg="red",
                                          text="Create account",
                                          font=("Arial", 14, "bold"),
                                        command=collect_new_account
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

# Assigning results of button to create account to account object



login_window.mainloop()