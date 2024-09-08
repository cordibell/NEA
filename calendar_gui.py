# calendar gui, made 8/9/24

import tkinter as tk

# tkinter window

class visualCalendar: # encapsulates all data from visual calendar menu
    def __init__(self, calendar_window):
        self.calendar_window = calendar_window


def calendar_menu(root): # displays calendar window

    calendar_window = tk.Toplevel(root)
    calendar_window.title("Visual Calendar")
    calendar_window.geometry("1050x800")
    
    placeholder_frame = tk.Frame(calendar_window)
    placeholder_text = tk.Label(placeholder_frame, text="This is a placeholder for the visual calendar")
    placeholder_frame.grid(row=0, column=0, sticky="n")
    placeholder_text.pack()

    return visualCalendar(calendar_window)

mydb.close()