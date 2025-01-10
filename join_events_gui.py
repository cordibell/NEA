# join/create events menu, created 27/08/24

import tkinter as tk
from tktooltip import ToolTip
import mysql.connector
from datetime import datetime
from tkinter import messagebox

mydb = mysql.connector.connect(
    host="10.0.2.214",
    user="standardUser",
    password="StandardPassword123!",
    database="ComputerScienceNEA"
)

class joinEvents: # encapsulates data from joining & hosting events
    def __init__(self, join_events_window, join_event_code, timeframe_var, start_date, end_date, event_title):
        self.join_events_window = join_events_window
        self.join_event_code = join_event_code
        self.timeframe_var = timeframe_var
        self.start_date = start_date
        self.end_date = end_date
        self.event_title = event_title
    
    def get_join_event_code(self):
        return self.join_event_code.get()
    
    def get_timeframe_var(self):
        return self.timeframe_var.get()
    
    def get_start_date(self):
        return self.start_date.get()
    
    def get_end_date(self):
        return self.end_date.get()
    
    def get_event_title(self):
        return self.event_title.get()
    
    def display_unique_code(self, generated_code):
        messagebox.showinfo("Event code", f"Your event code is {generated_code}.")
    
    def invalid_date_format(self):
        messagebox.showerror("Invalid date", "Date format must be DD/MM/YY")
    
    def invalid_date_logic(self):
        messagebox.showerror("Invalid date", "Start date after end date")
    
    def invalid_date_timeframe(self):
        messagebox.showerror("Invalid date", "Dates outside chosen timeframe length")
    
    def invalid_title_length(self):
        messagebox.showerror("Invalid title", "Title must be between 1-128 characters")
    
    def invalid_code(self):
        messagebox.showerror("Invalid code", "Cannot find that code")

# tkinter window

def join_events_menu(root, collect_join_event, collect_host_event): # displays join events window

    join_events_window = tk.Toplevel(root)
    join_events_window.title("Join or Host an Event Menu")
    join_events_window.geometry("1050x800")

    # Collecting information

    timeframe_var = tk.IntVar()
        
    # Constructing the two frames for this component
    join_event_frame = tk.Frame(join_events_window)
    host_event_frame = tk.Frame(join_events_window)

    # Constructing the border frames for the titles & text fields

    border_colour_join_event = tk.Frame(join_event_frame, bg="red")
    border_colour_host_event = tk.Frame(host_event_frame, bg="red")

    border_colour_join_event_entry = tk.Frame(join_event_frame, highlightbackground="red", highlightthickness=2)

    border_colour_select_timeframe = tk.Frame(host_event_frame, highlightbackground="red", highlightthickness=2)

    select_dates_frame = tk.Frame(host_event_frame)

    border_colour_start_date = tk.Frame(select_dates_frame, highlightbackground="red", highlightthickness=2)
    border_colour_end_date = tk.Frame(select_dates_frame, highlightbackground="red", highlightthickness=2)

    border_colour_event_title = tk.Frame(host_event_frame, highlightbackground="red", highlightthickness=2)

    # Constructing the label widgets for the titles
    join_event_title = tk.Label(
        border_colour_join_event,
        text="JOIN AN EVENT",
        font=("Arial", 26, "bold"),
        width=25,
        anchor="n",
        wraplength=350
    )
    host_event_title = tk.Label(
        border_colour_host_event,
        text="HOST AN EVENT",
        font=("Arial", 26, "bold"),
        width=25,
        anchor="n",
        wraplength=350
        )
    # Using the grid manager to display the two frames
    join_event_frame.grid(row=0, column=0, sticky="n")
    host_event_frame.grid(row=0,column=1)

    # Packing the two titles alongside their border colours onto the window
    join_event_title.pack(side=tk.TOP, anchor="n", padx=3,pady=3)
    host_event_title.pack(padx=3,pady=3)
    border_colour_join_event.pack(side=tk.TOP, anchor="n", padx=20,pady=20)
    border_colour_host_event.pack(padx=20,pady=20)

    # Joining an existing event entry
    join_event_code_entry = tk.Entry(border_colour_join_event_entry,
                                borderwidth=2,
                                font=("Arial", 12)
                                )

    join_event_code_entry_label = tk.Label(border_colour_join_event_entry,
                                            text="Enter code here:",
                                            font=("Arial", 14, "italic"),
                                            anchor="w"
                                    )

    # Select a timeframe buttons
    one_day_button = tk.Radiobutton(border_colour_select_timeframe,
                            bg="white",
                            activebackground="yellow",
                            text="1 day",
                            font=("Arial", 12),
                            indicatoron=0,
                            selectcolor="green",
                            variable=timeframe_var,
                            value=1
                            )

    one_week_button = tk.Radiobutton(border_colour_select_timeframe,
                            bg="white",
                            activebackground="yellow",
                            text="1 week",
                            font=("Arial", 12),
                            indicatoron=0,
                            selectcolor="green",
                            variable=timeframe_var,
                            value=2
                            )

    one_month_button = tk.Radiobutton(border_colour_select_timeframe,
                            bg="white",
                            activebackground="yellow",
                            text="1 month",
                            font=("Arial", 12),
                            indicatoron=0,
                            selectcolor="green",
                            variable=timeframe_var,
                            value=3
                            )

    three_months_button = tk.Radiobutton(border_colour_select_timeframe,
                            bg="white",
                            activebackground="yellow",
                            text="3 months",
                            font=("Arial", 12),
                            indicatoron=0,
                            selectcolor="green",
                            variable=timeframe_var,
                            value=4
                            )

    select_timeframe_label = tk.Label(border_colour_select_timeframe,
                                            text="Select a timeframe",
                                            font=("Arial", 14, "italic"),
                                            anchor="w"
                                    )

    # Enter start dates & end dates

    start_date_entry = tk.Entry(border_colour_start_date,
                                borderwidth=2,
                                font=("Arial", 12)
                                )

    start_date_entry_label = tk.Label(border_colour_start_date,
                                    text="Start date:",
                                    font=("Arial", 14, "italic"),
                                    anchor="w"
                                    )

    end_date_entry = tk.Entry(border_colour_end_date,
                                borderwidth=2,
                                font=("Arial", 12)
                                )

    end_date_entry_label = tk.Label(border_colour_end_date,
                                    text="End date:",
                                    font=("Arial", 14, "italic"),
                                    anchor="w"
                                    )

    # Enter title of event

    event_title_entry = tk.Entry(border_colour_event_title,
                                borderwidth=2,
                                font=("Arial", 12)
                            )

    event_title_entry_label = tk.Label(border_colour_event_title,
                                            text="Title:",
                                            font=("Arial", 14, "italic"),
                                            anchor="w"
                                    )

    # Confirmation buttons
    confirm_join_event_button = tk.Button(join_event_frame,
                                activebackground="green",
                                bg="red",
                                text="Join event",
                                font=("Arial", 14, "bold"),
                                command=collect_join_event
    )

    confirm_host_event_button = tk.Button(host_event_frame,
                                            activebackground="green",
                                            bg="red",
                                            text="Host event",
                                            font=("Arial", 14, "bold"),
                                            command=collect_host_event
    )

    # Packing join existing event entry
    join_event_code_entry_label.pack(side=tk.TOP, anchor="n", padx=1, pady=1)
    join_event_code_entry.pack(side=tk.TOP, anchor="n", padx=20,ipady=3, pady=10)
    border_colour_join_event_entry.pack(side=tk.TOP, anchor="n", padx=15, pady=5)


    # Packing select timeframes
    select_timeframe_label.pack(padx=1, pady=1)
    one_day_button.pack(side=tk.LEFT, padx=10, ipady=3, pady=10)
    one_week_button.pack(side=tk.LEFT, padx=5, ipady=3, pady=10)
    one_month_button.pack(side=tk.LEFT, padx=5, ipady=3, pady=10)
    three_months_button.pack(side=tk.LEFT, padx=10, ipady=3,pady=10)
    border_colour_select_timeframe.pack(padx=15, pady=5)

    # Packing start & end dates

    # Start date
    start_date_entry_label.pack(padx=1, pady=1)
    start_date_entry.pack(padx=10, ipady=3, pady=5)
    border_colour_start_date.pack(side=tk.LEFT, padx=15, pady=5)

    # End date
    end_date_entry_label.pack(padx=1, pady=1)
    end_date_entry.pack(padx=10, ipady=3, pady=5)
    border_colour_end_date.pack(side=tk.LEFT, padx=15, pady=5)

    select_dates_frame.pack(padx=1, pady=1)

    event_title_entry_label.pack(padx=1, pady=1)
    event_title_entry.pack(padx=20, ipady=3, pady=10)
    border_colour_event_title.pack(padx=15, pady=5)

    # Packing confirmation buttons
    confirm_join_event_button.pack(padx=20, pady=10)
    confirm_host_event_button.pack(padx=20, pady=10)

    # Tooltips

    ToolTip(start_date_entry_label, msg="Start date in format DD/MM/YY")
    ToolTip(end_date_entry_label, msg="End date in format DD/MM/YY")

    ToolTip(select_timeframe_label, msg="Choose a timeframe")

    ToolTip(event_title_entry_label, msg="Choose a title between 1-128 characters")

    ToolTip(join_event_code_entry_label, msg="Enter your 8 digit long code e.g. A123B456")

    return joinEvents(join_events_window, join_event_code_entry, timeframe_var, start_date_entry, end_date_entry, event_title_entry)

mydb.close()
