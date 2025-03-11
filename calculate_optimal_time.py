# calculate optimal time file, created 11/12/24

import datetime

import mysql.connector

mydb = mysql.connector.connect(
    host="10.0.2.214",
    user="standardUser",
    password="StandardPassword123!",
    database="ComputerScienceNEA"
)

class userEvent:
    '''
    This class contains all information about a user event.
    '''
    def __init__(self, id, start, end, is_tentative):
        self.id = id
        self.start = start
        self.end = end
        self.is_tentative = is_tentative

class User:
    '''
    This class contains information about a user's account.
    '''
    def __init__(self, username):
        self.username = username

    def set_preferred_times(self, preferred_start, preferred_end):
        self.preferred_start = preferred_start
        self.preferred_end = preferred_end

class timeSlot: # each hour timeslot that the event could possibly be in
    '''
    This class contains information about each invididual hour-long timeslot.
    '''
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.score = 0
    
    def increase_score_by_3(self): # when event isn't tentative
        self.score += 3

    def increase_score_by_2(self): # when event is tentative
        self.score += 2
    
    def decrease_score(self): # when preferred time
        self.score -= 2
    


def get_users_in_event(eventID, mydb): # collects all the users who are part of an event from EVENT_MEMBERS TABLE
    mycursor = mydb.cursor()
    find_users_sql = "SELECT username FROM EVENT_MEMBERS WHERE eventID = %s"
    values = (eventID, )
    mycursor.execute(find_users_sql, values)
    users_in_event = mycursor.fetchall() 
    list_of_users_in_event = []   
    for user in users_in_event: # making a list of the users
        userObject = User(user[0])
        list_of_users_in_event.append(userObject)
    list_of_event_objects = find_events_from_user_in_database(list_of_users_in_event, mydb) # finds each user's events
    list_of_timeslots = find_timeslots_range(eventID, mydb) # creates a list of timeslots in host event date range
    calculate_timeslot_score_from_events(list_of_timeslots, list_of_event_objects) # calculates each timeslot's event score
    find_preferred_times(list_of_users_in_event, mydb) # finds each user's preferred time
    calculate_timeslot_score_from_preferred_times(list_of_users_in_event, list_of_timeslots) # adjusts score based on preferred times
    list_of_best_timeslots = find_best_timeslots(list_of_timeslots) # finds 9 events with lowest scores
    return list_of_best_timeslots

def find_events_from_user_in_database(list_of_users_in_event, mydb): # finds all events in USER_EVENTS table for each user
    mycursor = mydb.cursor()
    list_of_events_found = []
    for user in list_of_users_in_event: # iterates over every user
        find_event_sql = "SELECT userEventID, event_start, event_end, is_tentative FROM USER_EVENTS WHERE username = %s"
        values = (user.username, )
        mycursor.execute(find_event_sql, values)
        event_found = mycursor.fetchall()
        list(event_found) # list of that user's events
        list_of_events_found.append(event_found)
    list_of_event_objects = convert_events_into_objects(list_of_events_found) # converts events into objects of class userEvent
    return list_of_event_objects

def convert_events_into_objects(list_of_events_found): # converts the items in the list into a list of objects of class userEvents
    list_of_event_objects = []
    for users_events in list_of_events_found: # iterating over ever user's list of events
        for event in users_events: # iterating over every user's event in their list of events
            event_id = event[0]
            start = event[1]
            end = event[2]
            is_tentative = event[3]
            list_of_event_objects.append(userEvent(event_id, start, end, is_tentative)) # making an individual object for each event
    return list_of_event_objects

def find_timeslots_range(eventID, mydb): # finds start date & end date of host event from database-
    mycursor = mydb.cursor()
    find_timeslot_sql = "SELECT start_date, end_date FROM HOST_EVENTS WHERE eventID = %s"
    values = (eventID,)
    mycursor.execute(find_timeslot_sql, values)
    myresult = mycursor.fetchone()
    start_date = myresult[0]
    end_date = myresult[1]
    list_of_timeslots = create_timeslots(start_date, end_date) # creates list of timeslots from date range
    return list_of_timeslots
    
def create_timeslots(start_date, end_date): # creates timeslot objects for each timeslot in the range
    list_of_timeslots = []
    current_date = start_date
    while current_date <= end_date: # iterating over all dates in timeframe
        hour = 8 # starts at 8am every day
        current_time = datetime.time(hour, 0, 0) # setting new time
        while hour <= 22: # while before 10pm, iterating over every hour in the day
            timeslot_start = datetime.datetime.combine(current_date, current_time) # sets start of timeslot
            hour += 1 # adding 1 to the hour
            current_time = datetime.time(hour, 0, 0) # sets current time
            timeslot_end = datetime.datetime.combine(current_date, current_time)
            list_of_timeslots.append(timeSlot(timeslot_start, timeslot_end)) # adding new timeslot object to list of timeslots
        current_date += datetime.timedelta(days=1) # adding 1 to the date
    return list_of_timeslots

def calculate_timeslot_score_from_events(list_of_timeslots, list_of_event_objects): 
    # calculates timeslot score based on if an event is during it
    for timeslot in list_of_timeslots:
        for event in list_of_event_objects:
            if (event.end >= timeslot.end and event.start <= timeslot.start) or (event.end <= timeslot.end and event.start >= timeslot.start):
                # checks if end of event & start of event are outside of timeslot range (aka across entire timeslot)
                # checks if start of event and end of event are within timeslot range (entirely within timeslot)
                if event.is_tentative == "Yes":
                    timeslot.increase_score_by_2()
                else:
                    timeslot.increase_score_by_3()

def find_preferred_times(list_of_users_in_event, mydb): # finds preferred times of all the users in the event
    mycursor = mydb.cursor()
    find_preferred_times_sql = "SELECT preferred_time_start, preferred_time_end FROM USERS WHERE username=%s"
    for user in list_of_users_in_event:
        values = (user.username, )
        mycursor.execute(find_preferred_times_sql, values)
        preferred_times = mycursor.fetchone()
        user.set_preferred_times(preferred_times[0], preferred_times[1])


def calculate_timeslot_score_from_preferred_times(list_of_users_in_event, list_of_timeslots): 
    # adjusts timeslot score if someone's preferred time is during the timeslot
    for timeslot in list_of_timeslots:
        for user in list_of_users_in_event:
            if (user.preferred_end or user.preferred_start) is None: # if user doesn't have a preferred time
                continue
            elif (user.preferred_end >= timeslot.end and user.preferred_start <= timeslot.start) or (user.preferred_end <= timeslot.end and user.preferred_start >= timeslot.start):
                # if user's preferred time start is before timeslot and end is after timeslot (aka spans entire timeslot)
                # or if user's preferred time start/end are inside timeslot (aka within entire timeslot)
                timeslot.decrease_score()

def find_best_timeslots(list_of_timeslots): # finds best 1 hour timeslots
    best_timeslots = []
    dictionary_of_timeslot_scores = {}
    for timeslot in list_of_timeslots:
        dictionary_of_timeslot_scores[timeslot] = timeslot.score
    list_of_timeslot_scores_as_tuple = list(zip(dictionary_of_timeslot_scores.items())) # converting dictionary to list of tuples
    for i in range(9): # finding 9 best scores
        lowest_score = list_of_timeslot_scores_as_tuple[0] # setting first score as lowest
        for timeslot in list_of_timeslot_scores_as_tuple:
            if lowest_score[0][1] >= timeslot[0][1]: # checking every item in list to see if score is lower than lowest
                lowest_score = timeslot
        best_timeslots.append(lowest_score[0][0])
        list_of_timeslot_scores_as_tuple.remove(lowest_score)
    return best_timeslots


