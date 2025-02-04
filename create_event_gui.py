# create event page created 21/10/24

import tkinter as tk
from tktooltip import ToolTip
from tkinter import messagebox

class createEvents:
    def __init__(self, create_event_window, start_date, end_date, start_time, end_time, event_title, is_repetitive, repetitive_timeframe_var, is_tentative_var):
        self.create_event_window = create_event_window
        self.start_date = start_date
        self.end_date = end_date
        self.start_time = start_time
        self.end_time = end_time
        self.event_title = event_title
        self.is_repetitive_var = is_repetitive
        self.repetitive_timeframe_var = repetitive_timeframe_var
        self.is_tentative_var = is_tentative_var
    
    def get_start_date(self):
        return self.start_date.get()
    
    def get_end_date(self):
        return self.end_date.get()
    
    def get_start_time(self):
        return self.start_time.get()
    
    def get_end_time(self):
        return self.end_time.get()
    
    def get_event_title(self):
        return self.event_title.get()
    
    def get_is_repetitive(self):
        return self.is_repetitive_var.get()
    
    def get_repetitive_timeframe(self):
        return self.repetitive_timeframe_var.get()
    
    def get_is_tentative(self):
        return self.is_tentative_var.get()
    
    def invalid_date_logic(self):
        messagebox.showerror("Invalid date", "Start date after end date")
    
    def invalid_date_format(self):
        messagebox.showerror("Invalid date", "Date format should be DD/MM/YY")

    def invalid_date_timeframe(self):
        messagebox.showerror("Invalid date", "One of the dates outside host's dates")
    
    def invalid_time_logic(self):
        messagebox.showerror("Invalid time", "Start time after end time")
    
    def invalid_time_format(self):
        messagebox.showerror("Invalid time", "Time format should be HH:MM")
    
    def invalid_title_length(self):
        messagebox.showerror("Invalid title", "Title should be between 1-128 characters")
    
    def invalid_repetition(self):
        messagebox.showerror("Invalid repetition", "Double check your repetition boxes")
    
    def invalid_tentability(self):
        messagebox.showerror("Invalid tentability", "Please select if tentative or not")


def create_event_menu(root, create_event_command, back_command):

    create_event_window = tk.Toplevel(root)
    create_event_window.title("Create an event")
    create_event_window.geometry("1050x800")

    # variables for collecting information from radiobuttons

    is_repetitive = tk.IntVar()
    repetitive_timeframe = tk.IntVar()
    is_tentative = tk.IntVar()

    # setting up frames for border colours & title
    create_event_frame = tk.Frame(create_event_window)
    
    border_colour_page_title = tk.Frame(create_event_frame, highlightbackground="red", highlightthickness=2)

    date_time_frame = tk.Frame(create_event_frame)

    border_colour_start_date = tk.Frame(date_time_frame, highlightbackground="orange", highlightthickness=2)
    border_colour_end_date = tk.Frame(date_time_frame, highlightbackground="orange", highlightthickness=2)
    border_colour_start_time = tk.Frame(date_time_frame, highlightbackground="orange", highlightthickness=2)
    border_colour_end_time = tk.Frame(date_time_frame, highlightbackground="orange", highlightthickness=2)

    border_colour_event_title = tk.Frame(create_event_frame, highlightbackground="red", highlightthickness=2)

    repetitive_frame = tk.Frame(create_event_frame)

    border_colour_is_repetitive = tk.Frame(repetitive_frame, highlightbackground="orange", highlightthickness=2)
    border_colour_repeat_timeframe = tk.Frame(repetitive_frame, highlightbackground="orange", highlightthickness=2)

    border_colour_is_tentative = tk.Frame(create_event_frame, highlightbackground="orange", highlightthickness=2)

    # adding in title

    create_event_page_title = tk.Label(
        border_colour_page_title,
        text="CREATE AN EVENT",
        font=("Arial", 25, "bold"),
        width=25,
        anchor="n",
        wraplength=350)
    
    # packing title + border colour

    create_event_frame.pack(padx=3, pady=3)
    create_event_page_title.pack(side=tk.TOP, anchor="n", padx=3, pady=3)
    border_colour_page_title.pack(padx=20, pady=20)

    # creating start/end date entries + labels

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
    
    # packing date/time frames/entries/labels

    date_time_frame.pack(padx=3, pady=3, side=tk.TOP)

    start_date_entry_label.pack(padx=3, pady=3)
    start_date_entry.pack(padx=3, pady=3)
    border_colour_start_date.pack(padx=15, pady=15, side=tk.LEFT)

    end_date_entry_label.pack(padx=3, pady=3)
    end_date_entry.pack(padx=3, pady=3)
    border_colour_end_date.pack(padx=15, pady=15, side=tk.LEFT)

    start_time_entry_label.pack(padx=3, pady=3)
    start_time_entry.pack(padx=3, pady=3)
    border_colour_start_time.pack(padx=15, pady=15, side=tk.LEFT)

    end_time_entry_label.pack(padx=3, pady=3)
    end_time_entry.pack(padx=3, pady=3)
    border_colour_end_time.pack(padx=15, pady=15, side=tk.LEFT)

    # create event title entry & packing

    create_event_title_entry = tk.Entry(border_colour_event_title,
                                        borderwidth=2,
                                        font=("Arial", 12),
                                        width=100
                                        )
    create_event_title_entry_label = tk.Label(border_colour_event_title,
                                              text="Event title:",
                                              font=("Arial", 14, "italic")
                                              )
    
    create_event_title_entry_label.pack(padx=3, pady=3)
    create_event_title_entry.pack(padx=3, pady=3)
    border_colour_event_title.pack(padx=3, pady=3)

    # repetitive buttons

    is_repetitive_button = tk.Radiobutton(border_colour_is_repetitive,
                                          bg="white",
                                          activebackground="yellow",
                                          text="Yes",
                                          font=("Arial", 12),
                                          indicatoron=0,
                                          selectcolor="green",
                                          variable=is_repetitive,
                                          value=1)
    is_not_repetitive_button = tk.Radiobutton(border_colour_is_repetitive,
                                          bg="white",
                                          activebackground="yellow",
                                          text="No",
                                          font=("Arial", 12),
                                          indicatoron=0,
                                          selectcolor="green",
                                          variable=is_repetitive,
                                          value=2)
    
    is_repetitive_label = tk.Label(border_colour_is_repetitive,
                                   text="Is repetitive?",
                                   font=("Arial", 14, "italic")
                                   )
    
    repeats_daily_button = tk.Radiobutton(border_colour_repeat_timeframe,
                            bg="white",
                            activebackground="yellow",
                            text="Daily",
                            font=("Arial", 12),
                            indicatoron=0,
                            selectcolor="green",
                            variable=repetitive_timeframe,
                            value=1
                            )
    repeats_weekly_button = tk.Radiobutton(border_colour_repeat_timeframe,
                            bg="white",
                            activebackground="yellow",
                            text="Weekly",
                            font=("Arial", 12),
                            indicatoron=0,
                            selectcolor="green",
                            variable=repetitive_timeframe,
                            value=2
                            )
    repeats_monthly_button = tk.Radiobutton(border_colour_repeat_timeframe,
                            bg="white",
                            activebackground="yellow",
                            text="Monthly",
                            font=("Arial", 12),
                            indicatoron=0,
                            selectcolor="green",
                            variable=repetitive_timeframe,
                            value=3
                            )
    repeats_custom_button = tk.Radiobutton(border_colour_repeat_timeframe,
                            bg="white",
                            activebackground="yellow",
                            text="Custom",
                            font=("Arial", 12),
                            indicatoron=0,
                            selectcolor="green",
                            variable=repetitive_timeframe,
                            value=4
                            )
    repeat_timeframe_label = tk.Label(border_colour_repeat_timeframe,
                                    text="How often does it repeat?",
                                    font=("Arial", 14, "italic")
                                    )

    # packing repetitive buttons

    repetitive_frame.pack(padx=3, pady=3)
    
    is_repetitive_label.pack(padx=3, pady=3)
    is_repetitive_button.pack(padx=3, pady=3, side=tk.LEFT)
    is_not_repetitive_button.pack(padx=3, pady=3, side=tk.RIGHT)
    border_colour_is_repetitive.pack(padx=3, pady=3, side=tk.LEFT)

    repeat_timeframe_label.pack(padx=3, pady=3)
    repeats_daily_button.pack(padx=3, pady=3, side=tk.LEFT)
    repeats_weekly_button.pack(padx=3, pady=3, side=tk.LEFT)
    repeats_monthly_button.pack(padx=3, pady=3, side=tk.LEFT)
    repeats_custom_button.pack(padx=3, pady=3, side=tk.LEFT)
    border_colour_repeat_timeframe.pack(padx=3, pady=3, side=tk.LEFT)

    # tentative buttons

    is_tentative_button = tk.Radiobutton(border_colour_is_tentative,
                            bg="white",
                            activebackground="yellow",
                            text="Yes",
                            font=("Arial", 12),
                            indicatoron=0,
                            selectcolor="green",
                            variable=is_tentative,
                            value=1
                            )
    is_not_tentative_button = tk.Radiobutton(border_colour_is_tentative,
                            bg="white",
                            activebackground="yellow",
                            text="No",
                            font=("Arial", 12),
                            indicatoron=0,
                            selectcolor="green",
                            variable=is_tentative,
                            value=2
                            )
    is_tentative_label = tk.Label(border_colour_is_tentative,
                                text="Tentative?",
                                font=("Arial", 14, "italic")
                                )
    
    # packing tentative buttons 

    is_tentative_label.pack(padx=3, pady=3)
    is_tentative_button.pack(padx=3, pady=3, side=tk.LEFT)
    is_not_tentative_button.pack(padx=3, pady=3, side=tk.RIGHT)
    border_colour_is_tentative.pack(padx=3, pady=3)

    # Confirmation/back button

    confirm_create_event_button = tk.Button(create_event_frame,
                                activebackground="green",
                                bg="red",
                                text="Create event",
                                font=("Arial", 14, "bold"),
                                command=create_event_command
    )
    confirm_create_event_button.pack(padx=3, pady=3)

    back_arrow_button = tk.Button(create_event_frame,
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

    ToolTip(create_event_title_entry_label, msg="Title between 1-128 characters")

    ToolTip(is_repetitive_label, msg="Select Yes/No")
    ToolTip(repeat_timeframe_label, msg="If selected Yes, choose one")

    ToolTip(is_tentative_label, msg="Select Yes/No")

    return createEvents(create_event_window, start_date_entry, end_date_entry, start_time_entry, end_time_entry, create_event_title_entry, is_repetitive, repetitive_timeframe, is_tentative)



