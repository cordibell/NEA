# set preferred times menu, made 10/12/24
import tkinter as tk
from tktooltip import ToolTip
from tkinter import messagebox

class setPreferredTime:
    def __init__(self, set_preferred_time_window, start_date, end_date, start_time, end_time):
        self.set_preferred_time_window = set_preferred_time_window
        self.start_date = start_date
        self.end_date = end_date
        self.start_time = start_time
        self.end_time = end_time

    def get_start_date(self):
        return self.start_date.get()
    
    def get_end_date(self):
        return self.end_date.get()
    
    def get_start_time(self):
        return self.start_time.get()
    
    def get_end_time(self):
        return self.end_time.get()

    def invalid_date_format(self):
        messagebox.showerror("Invalid date", "Date format must be DD/MM/YY")

    def invalid_date_logic(self):
        messagebox.showerror("Invalid date", "Start date after end date")
    
    def invalid_time_format(self):
        messagebox.showerror("Invalid time", "Time format must be HH:MM")
    
    def invalid_time_logic(self):
        messagebox.showerror("Invalid time", "Start time after end time")
    
    def error(self):
        messagebox.showerror("Error", "Error")

def set_preferred_times_menu(root, set_preferred_time_command, back_command): 
    
    set_preferred_time_window = tk.Toplevel(root)
    set_preferred_time_window.title("Set preferred time")
    set_preferred_time_window.geometry("1050x800")
    
    # setting up frames

    set_preferred_time_frame = tk.Frame(set_preferred_time_window)
    
    border_colour_page_title = tk.Frame(set_preferred_time_frame, highlightbackground="red", highlightthickness=2)

    date_frame = tk.Frame(set_preferred_time_frame)

    border_colour_start_date = tk.Frame(date_frame, highlightbackground="red", highlightthickness=2)
    border_colour_end_date = tk.Frame(date_frame, highlightbackground="red", highlightthickness=2)

    time_frame = tk.Frame(set_preferred_time_frame)

    border_colour_start_time = tk.Frame(time_frame, highlightbackground="red", highlightthickness=2)
    border_colour_end_time = tk.Frame(time_frame, highlightbackground="red", highlightthickness=2)

    # creating page title

    set_preferred_time_page_title = tk.Label(
        border_colour_page_title,
        text="SET PREFERRED TIME",
        font=("Arial", 25, "bold"),
        width=25,
        anchor="n",
        wraplength=350
    )

    # packing title & border colours
    set_preferred_time_frame.pack(padx=3, pady=3)
    set_preferred_time_page_title.pack(padx=3, pady=3)
    border_colour_page_title.pack(padx=3, pady=3)

    # creating start date entries

    start_date_entry = tk.Entry(border_colour_start_date,
                            borderwidth=2,
                            font=("Arial", 12)
                            )
    start_date_entry_label = tk.Label(border_colour_start_date, 
                                      text="Start date:",
                                      font=("Arial", 14, "italic")
                                      )
    
    end_date_entry = tk.Entry(border_colour_end_date,
                              borderwidth=2,
                              font=("Arial", 12)
                              )
    end_date_entry_label = tk.Label(border_colour_end_date,
                                    text="End date:",
                                    font=("Arial", 14, "italic")
                                    )
    
    # packing start date entries

    date_frame.pack(padx=3, pady=3)

    start_date_entry_label.pack(padx=3, pady=3)
    start_date_entry.pack(padx=3, pady=3)
    border_colour_start_date.pack(padx=15, pady=15, side=tk.LEFT)

    end_date_entry_label.pack(padx=3, pady=3)
    end_date_entry.pack(padx=3, pady=3)
    border_colour_end_date.pack(padx=15, pady=15, side=tk.LEFT)

    # entries and labels for times

    start_time_entry = tk.Entry(border_colour_start_time,
                            borderwidth=2,
                            font=("Arial", 12)
                            )
    start_time_entry_label = tk.Label(border_colour_start_time,
                                      text="Start time:",
                                      font=("Arial", 14, "italic")
                                      )
    
    end_time_entry = tk.Entry(border_colour_end_time,
                              borderwidth=2,
                              font=("Arial", 12)
                              )
    end_time_entry_label = tk.Label(border_colour_end_time,
                                    text="End time:",
                                    font=("Arial", 14, "italic")
                                    )
    
    # packing time labels

    time_frame.pack(padx=3, pady=3)

    start_time_entry_label.pack(padx=3, pady=3)
    start_time_entry.pack(padx=3, pady=3)
    border_colour_start_time.pack(padx=15, pady=15, side=tk.LEFT)

    end_time_entry_label.pack(padx=3, pady=3)
    end_time_entry.pack(padx=3, pady=3)
    border_colour_end_time.pack(padx=15, pady=15, side=tk.LEFT)

    # confirmation button & back button

    confirm_create_event_button = tk.Button(set_preferred_time_frame,
                                activebackground="green",
                                bg="red",
                                text="Set preferred times",
                                font=("Arial", 14, "bold"),
                                command=set_preferred_time_command
    )
    confirm_create_event_button.pack(padx=3, pady=3)

    back_arrow_button = tk.Button(set_preferred_time_frame,
                                  activebackground="yellow",
                                  bg="orange",
                                  text="←",
                                  font=("Arial", 26, "bold"),
                                  command=back_command
                                  )
    back_arrow_button.pack(padx=3, pady=3)

    # tooltips

    ToolTip(start_date_entry_label, msg="Start date in format DD/MM/YY")
    ToolTip(end_date_entry_label, msg="End date in format DD/MM/YY")
    ToolTip(start_time_entry_label, msg="Start time in format HH:MM")
    ToolTip(end_time_entry_label, msg="End time in format HH:MM")


    return setPreferredTime(set_preferred_time_window, start_date_entry, end_date_entry, start_time_entry, end_time_entry)

    

    