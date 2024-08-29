# join_events code, made 29/09/24

import mysql.connector
import datetime

# Connecting to database
mydb = mysql.connector.connect(
    host="localhost",
    user="standardUser",
    password="StandardPassword123!",
    database="ComputerScienceNEA"
)

def find_timeframe(selected_timeframe):
    if selected_timeframe == 1:
        timeframe = "1 day"
    elif selected_timeframe == 2:
        timeframe = "1 week"
    elif selected_timeframe == 3:
        timeframe = "1 month"
    elif selected_timeframe == 4:
        timeframe = "3 months"
    else:
        timeframe="Error"
    return timeframe


class Host_event: # event hosted by a user, where they are trying to find out availability for it
    def __init__(self, event_name, timeframe, start_date, end_date):
        self.event_name = event_name
        self.timeframe = timeframe
        self.start_date = start_date
        self.end_date = end_date

    def save_event_info(self, mydb):
        print("Saved event info to database")
