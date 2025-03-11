# Optimal time GUI, created 18/12/24
import tkinter as tk

class optimalTimes:
    '''
    This class contains all information to do with the optimal time window.
    '''
    def __init__(self, optimal_time_window):
        self.optimal_time_window = optimal_time_window

def optimal_time_menu(root, confirm_time, list_of_best_timeslots):
    '''
    This function contains all the Tkinter widgets for the optimal time window.
    '''
    optimal_time_window = tk.Toplevel(root)
    optimal_time_window.title("View optimal times")
    optimal_time_window.geometry("1050x800")

    # creating frames

    border_colour_title = tk.Frame(optimal_time_window, bg="red")

    border_colour_optimal_times = tk.Frame(optimal_time_window, bg="red")

    # title

    optimal_event_title = tk.Label(
        border_colour_title,
        text="OPTIMAL TIMES",
        font=("Arial", 25, "bold"),
        width=25,
        anchor="n",
        wraplength=350
    )

    optimal_event_title.pack(padx=3, pady=3, side=tk.TOP)
    border_colour_title.pack(padx=3, pady=3)

    # setting up optimal times information grid

    count = 0
    for i in range(3): # iterating over rows
        for j in range(3): # iterating over columns
            if count<=2: # colour coding based on recommendation
                backgroundcolour = "green"
            elif count <= 5:
                backgroundcolour = "yellow"
            else:
                backgroundcolour = "red"
            border_colour_time_cell = tk.Frame(border_colour_optimal_times, bg="black")
            optimal_time_cell = tk.Frame(border_colour_time_cell, bg=backgroundcolour)
            timeslot_time = tk.Label(border_colour_time_cell,
                                text=f"{list_of_best_timeslots[count].start.strftime('%Y-%m-%d %H:%M')}-{list_of_best_timeslots[count].end.strftime('%Y-%m-%d %H:%M')}",
                                font=("Arial", 10, "bold"),
                                bg=backgroundcolour
            )
            timeslot_score = tk.Label(border_colour_time_cell,
                                    text=f"Score: {list_of_best_timeslots[count].score}",
                                    font=("Arial", 9, "italic"),
                                    bg=backgroundcolour
            )

            timeslot_time.pack(padx=1, fill="both", expand=True)
            timeslot_score.pack(padx=1, fill="both", expand=True)
            optimal_time_cell.pack(padx=1, pady=1, fill="both", expand=True)
            border_colour_time_cell.grid(row=i, column=j, sticky="n")
            count+=1
    
    border_colour_optimal_times.pack(padx=3, pady=3)
    
    # confirmation button that takes you back to visual calendar menu

    confirm_button = tk.Button(optimal_time_window,
                            activebackground="green",
                            bg="red",
                            text="Confirm Choice",
                            font=("Arial", 14, "bold"),
                            command=confirm_time
    )

    confirm_button.pack(padx=3, pady=3)

    return optimalTimes(optimal_time_window)
