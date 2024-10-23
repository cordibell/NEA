# calendar gui, made 8/9/24

import tkinter as tk

# tkinter window

class visualCalendar: # encapsulates all data from visual calendar menu
    def __init__(self, calendar_window):
        self.calendar_window = calendar_window
    
    def set_event_ID(self, eventID):
        self.eventID = eventID


def calendar_menu(root, load_create_event_menu): # displays calendar window

    calendar_window = tk.Toplevel(root)
    calendar_window.title("Visual Calendar")
    calendar_window.geometry("1400x1000")

    # setting up frames for header buttons/labels
    
    header_frame = tk.Frame(calendar_window)
    border_colour_calendar_title = tk.Frame(header_frame, highlightbackground="red", highlightthickness=2)

    add_edit_event_frame = tk.Frame(header_frame)

    # buttons & labels for top menu

    optimal_time_button = tk.Button(header_frame,
                                  activebackground="yellow",
                                  bg="orange",
                                  text="View optimal times",
                                  font=("Arial", 14, "bold")
                                  )
    
    add_event_button = tk.Button(add_edit_event_frame,
                                 activebackground="yellow",
                                 bg="orange",
                                 text="Add event",
                                 font=("Arial", 14, "bold"),
                                 command=load_create_event_menu
                                 )

    edit_event_button = tk.Button(add_edit_event_frame,
                                  activebackground="yellow",
                                  bg="orange",
                                  text="Edit event",
                                  font=("Arial", 14, "bold")
                                  )
    
    calendar_title = tk.Label(
                            border_colour_calendar_title,
                            text="Group Calendar",
                            font=("Arial", 26, "bold"),
                            width=25,
                            anchor="n",
                            wraplength=350,
                            justify="center"
                            )

    # Packing header buttons/label

    header_frame.pack(padx=3, pady=3)

    optimal_time_button.pack(side=tk.LEFT, padx=3, pady=3)
    calendar_title.pack(side=tk.LEFT,padx=3, pady=3)
    border_colour_calendar_title.pack(side=tk.LEFT, padx=20, pady=20)
    
    add_edit_event_frame.pack(side=tk.LEFT, padx=3, pady=3)

    add_event_button.pack(padx=3, pady=3)
    edit_event_button.pack(padx=3, pady=3)

    # creating the grid outline

    visual_calendar_frame = tk.Frame(calendar_window)

    visual_calendar_frame.pack(padx=3, pady=3)

    days = ["","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for day in range(8):
        day_border = tk.Frame(visual_calendar_frame, highlightbackground="black", highlightthickness=1)
        day_label = tk.Label(day_border, text=days[day], font=("Arial", 22, "bold"), width=10, bg="white")
        day_border.grid(row=0, column=day, sticky="n")
        day_label.pack(padx=1, pady=1)

    times = ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00"]
    for time in range(1,17):
        time_border = tk.Frame(visual_calendar_frame, highlightbackground="black", highlightthickness=1)
        time_label = tk.Label(time_border, text=times[time-1], font=("Arial", 22, "bold"), width=10, bg="white", height=1)
        time_border.grid(row=time, column=0, sticky="n")
        time_label.pack(padx=1, pady=1)

    for day in range(1,8):
        for time in range(1, 17):
            cell_border = tk.Frame(visual_calendar_frame, highlightbackground="black", highlightthickness=1)
            cell_label = tk.Label(cell_border, text="", bg="white", anchor="center", height=2)
            cell_border.grid(row=time, column=day, sticky="nesw")
            cell_label.pack(fill='both')

    # footer - arrow keys & preferred time button

    footer_frame = tk.Frame(calendar_window)

    back_arrow_button = tk.Button(footer_frame,
                                  activebackground="yellow",
                                  bg="orange",
                                  text="←",
                                  font=("Arial", 26, "bold")
                                  )
    
    preferred_time_button = tk.Button(footer_frame,
                                      activebackground="yellow",
                                      bg="orange",
                                      text="Preferred time",
                                      font=("Arial", 26, "bold")
                                      )
    
    forward_arrow_button = tk.Button(footer_frame,
                                  activebackground="yellow",
                                  bg="orange",
                                  text="→",
                                  font=("Arial", 26, "bold")
                                  )
    
    footer_frame.pack(padx=3, pady=3)
    
    back_arrow_button.pack(padx=3, pady=3, side=tk.LEFT)
    preferred_time_button.pack(padx=3, pady=3, side=tk.LEFT)
    forward_arrow_button.pack(padx=3, pady=3, side=tk.LEFT)

    return visualCalendar(calendar_window)
