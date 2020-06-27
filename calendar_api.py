from __future__ import print_function
from stringcolor import *
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import datetime
from datetime import timedelta
from datetime import date
from rfc3339 import rfc3339



# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
PATH = '/home/kevin/code/projects/google-calendar-command-line/credentials.json'
HOME_WORK_CALENDAR_COLOR = "#12cad6"
HOME_CALENDAR_COLOR = "#fa163f"
DATE_COLOR = "#ffcd3c"
BOARD_COLOR = "#404040"

def response_from_api(calID, service, max_time, now, color):
    events_result = service.events().list(calendarId=calID, timeMax=max_time, timeMin=now,
                                        maxResults=200, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])


    val = []
    if not events:
        pass
        # print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        val.append(start + " " + event['summary'])
    return val



def get_api_response():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('/home/kevin/code/projects/google-calendar-command-line/token.pickle'):
        with open('/home/kevin/code/projects/google-calendar-command-line/token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('/home/kevin/code/projects/google-calendar-command-line/token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)


    # Call the Calendar API
    now = rfc3339(date.today() - timedelta(days=0))

    delta = datetime.timedelta(days=7)
    max_time = date.today() + timedelta(days=7)
    max_time = rfc3339(max_time)
    api_test_cal = response_from_api ("4tikr714t89qsjprpeijog83po@group.calendar.google.com", service, max_time, now, color="#FF6347")
    home_cal = response_from_api ("d47.org_l77q084fo5hdumaucnoqmu7ifs@group.calendar.google.com", service, max_time, now, color="#FF6347")
    birthdays_cal = response_from_api ("93ree9e9e3piqpimt1uiu596tg@group.calendar.google.com", service, max_time, now, color="#FF6347")

    list_of_cals = [api_test_cal, birthdays_cal, home_cal]
    return list_of_cals
list_of_events = []


ffffff = 1
print(type(ffffff))

def parse_response(response):
    color = "#FFFFFF"
    i = 0
    for _ in response:
        for event in _:
            event_name = event[26:]
            event_day = event[8:10]
            try:
                 if int(event[11]):
                    print("type is on int", event[11])
                    event_time = event[11:13] + ":" + event[14:16]
                    x = int(event_time[0:2])
                    if int(x) > 12:
                        event_time = int(event_time[0:2]) - 12
                        event_time = "0" + str(event_time) + ":" +event[14:16] + "PM"
                    else:
                     event_time = str(event_time) + "AM"
            except:
                event_time = "ALL DAY"
                event_name = event[11:]

            if i == 0:
                color = HOME_WORK_CALENDAR_COLOR
            elif i == 1:
                color = HOME_CALENDAR_COLOR
            list_of_events.append([event_day, event_time, event_name, color])
        i = i+1

    return (list_of_events)


def main():
    response = get_api_response()
    parsed_response =parse_response(response)


main()


space = " "

day_1_time1 = " "
day_1_time2 = " "
day_1_color1 = "#FFFFFF"
day_1_event1 = " "
day_1_event2 = " "
day_1_color2 = "#FFFFFF"
day_1_time3 = " "
day_1_event3 = " "
day_1_color3 = "#FFFFFF"
day_1_time4 = " "
day_1_event4 = " "
day_1_color4 = "#FFFFFF"
day_1_time5 = " "
day_1_event5 = " "
day_1_color5 = "#FFFFFF"

day_2_time1 = " "
day_2_event1 = " "
day_2_color1 = "#FFFFFF"
day_2_time2 = " "
day_2_event2 = " "
day_2_color2 = "#FFFFFF"
day_2_time3 = " "
day_2_event3 = " "
day_2_color3 = "#FFFFFF"
day_2_time4 = " "
day_2_event4 = " "
day_2_color4 = "#FFFFFF"
day_2_time5 = " "
day_2_event5 = " "
day_2_color5 = "#FFFFFF"

day_3_time1 = " "
day_3_event1 = " "
day_3_color1 = "#FFFFFF"
day_3_time2 = " "
day_3_event2 = " "
day_3_color2 = "#FFFFFF"
day_3_time3 = " "
day_3_event3 = " "
day_3_color3 = "#FFFFFF"
day_3_time4 = " "
day_3_event4 = " "
day_3_color4 = "#FFFFFF"
day_3_time5 = " "
day_3_event5 = " "
day_3_color5 = "#FFFFFF"

day_4_time1 = " "
day_4_event1 = " "
day_4_color1 = "#FFFFFF"
day_4_time2 = " "
day_4_event2 = " "
day_4_color2 = "#FFFFFF"
day_4_time3 = " "
day_4_event3 = " "
day_4_color3 = "#FFFFFF"
day_4_time4 = " "
day_4_event4 = " "
day_4_color4 = "#FFFFFF"
day_4_time5 = " "
day_4_event5 = " "
day_4_color5 = "#FFFFFF"

day_5_time1 = " "
day_5_event1 = " "
day_5_color1 = "#FFFFFF"
day_5_time2 = " "
day_5_event2 = " "
day_5_color2 = "#FFFFFF"
day_5_time3 = " "
day_5_event3 = " "
day_5_color3 = "#FFFFFF"
day_5_time4 = " "
day_5_event4 = " "
day_5_color4 = "#FFFFFF"
day_5_time5 = " "
day_5_event5 = " "
day_5_color5 = "#FFFFFF"

day_6_time1 = " "
day_6_event1 = " "
day_6_color1 = "#FFFFFF"
day_6_time2 = " "
day_6_event2 = " "
day_6_color2 = "#FFFFFF"
day_6_time3 = " "
day_6_event3 = " "
day_6_color3 = "#FFFFFF"
day_6_time4 = " "
day_6_event4 = " "
day_6_color4 = "#FFFFFF"
day_6_time5 = " "
day_6_event5 = " "
day_6_color5 = "#FFFFFF"

day_7_time1 = " "
day_7_event1 = " "
day_7_color1 = "#FFFFFF"
day_7_time2 = " "
day_7_event2 = " "
day_7_color2 = "#FFFFFF"
day_7_time3 = " "
day_7_event3 = " "
day_7_color3 = "#FFFFFF"
day_7_time4 = " "
day_7_event4 = " "
day_7_color4 = "#FFFFFF"
day_7_time5 = " "
day_7_event5 = " "
day_7_color5 = "#FFFFFF"


day_1 = (date.today()).__format__("%b-%a-%d")
day_2 = (date.today() + timedelta(days=1)).__format__("%b-%a-%d")
day_3 = (date.today() + timedelta(days=2)).__format__("%b-%a-%d")
day_4 = (date.today() + timedelta(days=3)).__format__("%b-%a-%d")
day_5 = (date.today() + timedelta(days=4)).__format__("%b-%a-%d")
day_6 = (date.today() + timedelta(days=5)).__format__("%b-%a-%d")
day_7 = (date.today() + timedelta(days=6)).__format__("%b-%a-%d")

day_1_num  = (date.today()).__format__("%d")
day_2_num = (date.today() + timedelta(days=1)).__format__("%d")
day_3_num = (date.today() + timedelta(days=2)).__format__("%d")
day_4_num = (date.today() + timedelta(days=3)).__format__("%d")
day_5_num = (date.today() + timedelta(days=4)).__format__("%d")
day_6_num = (date.today() + timedelta(days=5)).__format__("%d")
day_7_num = (date.today() + timedelta(days=6)).__format__("%d")

i = 0
day_1_count = 1
day_2_count = 1
day_3_count = 1
day_4_count = 1
day_5_count = 1
day_6_count = 1
day_7_count = 1
for each in list_of_events:
    if day_1_num == list_of_events[i][0]:
        if day_1_count == 1:
            day_1_time1 = list_of_events[i][1]
            day_1_event1 = list_of_events[i][2]
            day_1_color1 = list_of_events[i][3]
        elif day_1_count == 2:
            day_1_time2 = list_of_events[i][1]
            day_1_event2 = list_of_events[i][2]
            day_1_color2 = list_of_events[i][3]
        elif day_1_count == 3:
            day_1_time3 = list_of_events[i][1]
            day_1_event3 = list_of_events[i][2]
            day_1_color3 = list_of_events[i][3]
        elif day_1_count == 4:
            day_1_time4 = list_of_events[i][1]
            day_1_event4 = list_of_events[i][2]
            day_1_color4 = list_of_events[i][3]
        elif day_1_count == 5:
            day_1_time5 = list_of_events[i][1]
            day_1_event5 = list_of_events[i][2]
            day_1_color5 = list_of_events[i][3]
        day_1_count = day_1_count+1
    if day_2_num == list_of_events[i][0]:
        if day_2_count == 1:
            day_2_time1 = list_of_events[i][1]
            day_2_event1 = list_of_events[i][2]
            day_2_time1 = list_of_events[i][1]
            day_2_event1 = list_of_events[i][2]
            day_2_color1 = list_of_events[i][3]
        elif day_2_count == 2:
            day_2_time2 = list_of_events[i][1]
            day_2_event2 = list_of_events[i][2]
            day_2_color2 = list_of_events[i][3]
        elif day_2_count == 3:
            day_2_time3 = list_of_events[i][1]
            day_2_event3 = list_of_events[i][2]
            day_2_color3 = list_of_events[i][3]
        elif day_2_count == 4:
            day_2_time4 = list_of_events[i][1]
            day_2_event4 = list_of_events[i][2]
            day_2_color4 = list_of_events[i][3]
        elif day_2_count == 5:
            day_2_time5 = list_of_events[i][1]
            day_2_event5 = list_of_events[i][2]
            day_2_color5 = list_of_events[i][3]
        day_2_count = day_2_count+1
    if day_3_num == list_of_events[i][0]:
        if day_3_count == 1:
            day_3_time1 = list_of_events[i][1]
            day_3_event1 = list_of_events[i][2]
            day_3_color1 = list_of_events[i][3]
        elif day_3_count == 2:
            day_3_time2 = list_of_events[i][1]
            day_3_event2 = list_of_events[i][2]
            day_3_color2 = list_of_events[i][3]
        elif day_3_count == 3:
            day_3_time3 = list_of_events[i][1]
            day_3_event3 = list_of_events[i][2]
            day_3_color3 = list_of_events[i][3]
        elif day_3_count == 4:
            day_3_time4 = list_of_events[i][1]
            day_3_event4 = list_of_events[i][2]
            day_3_color4 = list_of_events[i][3]
        elif day_3_count == 5:
            day_3_time5 = list_of_events[i][1]
            day_3_event5 = list_of_events[i][2]
            day_3_color5 = list_of_events[i][3]
        day_3_count = day_3_count+1
    if day_4_num == list_of_events[i][0]:
        if day_4_count == 1:
            day_4_time1 = list_of_events[i][1]
            day_4_event1 = list_of_events[i][2]
            day_4_color1 = list_of_events[i][3]
        elif day_4_count == 2:
            day_4_time2 = list_of_events[i][1]
            day_4_event2 = list_of_events[i][2]
            day_4_color2 = list_of_events[i][3]
        elif day_4_count == 3:
            day_4_time3 = list_of_events[i][1]
            day_4_event3 = list_of_events[i][2]
            day_4_color3 = list_of_events[i][3]
        elif day_4_count == 4:
            day_4_time4 = list_of_events[i][1]
            day_4_event4 = list_of_events[i][2]
            day_4_color4 = list_of_events[i][3]
        elif day_4_count == 5:
            day_4_time5 = list_of_events[i][1]
            day_4_event5 = list_of_events[i][2]
            day_4_color5 = list_of_events[i][3]
        day_4_count = day_4_count+1
    if day_5_num == list_of_events[i][0]:
        if day_1_count == 1:
            day_5_time1 = list_of_events[i][1]
            day_5_event1 = list_of_events[i][2]
            day_5_color1 = list_of_events[i][3]
        elif day_5_count == 2:
            day_5_time2 = list_of_events[i][1]
            day_5_event2 = list_of_events[i][2]
            day_5_color2 = list_of_events[i][3]
        elif day_5_count == 3:
            day_5_time3 = list_of_events[i][1]
            day_5_event3 = list_of_events[i][2]
            day_5_color3 = list_of_events[i][3]
        elif day_5_count == 4:
            day_5_time4 = list_of_events[i][1]
            day_5_event4 = list_of_events[i][2]
            day_5_color4 = list_of_events[i][3]
        elif day_5_count == 5:
            day_5_time5 = list_of_events[i][1]
            day_5_event5 = list_of_events[i][2]
            day_5_color5 = list_of_events[i][3]
        day_5_count = day_5_count+1
    if day_6_num == list_of_events[i][0]:
        if day_6_count == 1:
            day_6_time1 = list_of_events[i][1]
            day_6_event1 = list_of_events[i][2]
            day_6_color1 = list_of_events[i][3]
        elif day_6_count == 2:
            day_6_time2 = list_of_events[i][1]
            day_6_event2 = list_of_events[i][2]
            day_6_color2 = list_of_events[i][3]
        elif day_6_count == 3:
            day_6_time3 = list_of_events[i][1]
            day_6_event3 = list_of_events[i][2]
            day_6_color3 = list_of_events[i][3]
        elif day_6_count == 4:
            day_6_time4 = list_of_events[i][1]
            day_6_event4 = list_of_events[i][2]
            day_6_color4 = list_of_events[i][3]
        elif day_6_count == 5:
            day_6_time5 = list_of_events[i][1]
            day_6_event5 = list_of_events[i][2]
            day_6_color5 = list_of_events[i][3]
        day_6_count = day_6_count+1
    if day_7_num == list_of_events[i][0]:
        if day_7_count == 1:
            day_7_time1 = list_of_events[i][1]
            day_7_event1 = list_of_events[i][2]
            day_7_color1 = list_of_events[i][3]
        elif day_7_count == 2:
            day_7_time2 = list_of_events[i][1]
            day_7_event2 = list_of_events[i][2]
            day_7_color2 = list_of_events[i][3]
        elif day_7_count == 3:
            day_7_time3 = list_of_events[i][1]
            day_7_event3 = list_of_events[i][2]
            day_7_color3 = list_of_events[i][3]
        elif day_7_count == 4:
            day_7_time4 = list_of_events[i][1]
            day_7_event4 = list_of_events[i][2]
            day_7_color4 = list_of_events[i][3]
        elif day_7_count == 5:
            day_7_time5 = list_of_events[i][1]
            day_7_event5 = list_of_events[i][2]
            day_7_color5 = list_of_events[i][3]
        day_7_count = day_7_count+1
    i= i+1

# day_1_time1.ljust(18)[0:18]

print(f"  /--------------------------------------------------------------------------------------------------------------------------------------------------------\  ")
print(f"  |                     |                     |                     |                     |                     |                     |                    |  ")
print(f"  |    {cs(day_1, DATE_COLOR).bold().underline()}       |     {cs(day_2, DATE_COLOR).bold().underline()}      |     {cs(day_3, DATE_COLOR).bold().underline()}      |     {cs(day_4, DATE_COLOR).bold().underline()}      |     {cs(day_5, DATE_COLOR).bold().underline()}      |     {cs(day_6, DATE_COLOR).bold().underline()}      |     {cs(day_7, DATE_COLOR).bold().underline()}     |  ")
print(f"  |                     |                     |                     |                     |                     |                     |                    |  ")
print(f"  |---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|--------------------|  ")
print(f"  |                     |                     |                     |                     |                     |                     |                    |  ")
print(f"  |   {cs(day_1_time1.ljust(18)[0:18], day_1_color1).bold()}|   {cs(day_2_time1.ljust(18)[0:18], day_2_color1).bold()}|   {cs(day_3_time1.ljust(18)[0:18], day_3_color1).bold()}|   {cs(day_4_time1.ljust(18)[0:18], day_4_color1).bold()}|   {cs(day_5_time1.ljust(18)[0:18], day_5_color1).bold()}|   {cs(day_6_time1.ljust(18)[0:18], day_6_color1).bold()}|   {cs(day_7_time1.ljust(18)[0:17], day_7_color1).bold()}|")
print(f"  |   {cs(day_1_event1.ljust(18)[0:18], day_1_color1).bold()}|   {cs(day_2_event1.ljust(18)[0:18], day_2_color1).bold()}|   {cs(day_3_event1.ljust(18)[0:18], day_3_color1).bold()}|   {cs(day_4_event1.ljust(18)[0:18], day_4_color1).bold()}|   {cs(day_5_event1.ljust(18)[0:18], day_5_color1).bold()}|   {cs(day_6_event1.ljust(18)[0:18], day_6_color1).bold()}|   {cs(day_7_event1.ljust(18)[0:17], day_7_color1).bold()}|")
print(f"  |                     |                     |                     |                     |                     |                     |                    |  ")
print(f"  |                     |                     |                     |                     |                     |                     |                    |  ")
print(f"  |                     |                     |                     |                     |                     |                     |                    |  ")
print(f"  |                     |                     |                     |                     |                     |                     |                    |  ")
print(f"  |   {cs(day_1_time2.ljust(18)[0:18], day_1_color2).bold()}|   {cs(day_2_time2.ljust(18)[0:18], day_2_color2).bold()}|   {cs(day_3_time2.ljust(18)[0:18], day_3_color2).bold()}|   {cs(day_4_time2.ljust(18)[0:18], day_4_color2).bold()}|   {cs(day_5_time2.ljust(18)[0:18], day_5_color2).bold()}|   {cs(day_6_time2.ljust(18)[0:18], day_6_color2).bold()}|   {cs(day_7_time2.ljust(18)[0:17], day_7_color2).bold()}|")
print(f"  |   {cs(day_1_event2.ljust(18)[0:18], day_1_color2).bold()}|   {cs(day_2_event2.ljust(18)[0:18], day_2_color2).bold()}|   {cs(day_3_event2.ljust(18)[0:18], day_3_color2).bold()}|   {cs(day_4_event2.ljust(18)[0:18], day_4_color2).bold()}|   {cs(day_5_event2.ljust(18)[0:18], day_5_color2).bold()}|   {cs(day_6_event2.ljust(18)[0:18], day_6_color2).bold()}|   {cs(day_7_event2.ljust(18)[0:17], day_7_color2).bold()}|")
print(f"  |                     |                     |                     |                     |                     |                     |                    |  ")
print(f"  |                     |                     |                     |                     |                     |                     |                    |  ")
print(f"  |                     |                     |                     |                     |                     |                     |                    |  ")
print(f"  |                     |                     |                     |                     |                     |                     |                    |  ")
print(f"  |   {cs(day_1_time3.ljust(18)[0:18], day_1_color3).bold()}|   {cs(day_2_time3.ljust(18)[0:18], day_2_color3).bold()}|   {cs(day_3_time3.ljust(18)[0:18], day_3_color3).bold()}|   {cs(day_4_time3.ljust(18)[0:18], day_4_color3).bold()}|   {cs(day_5_time3.ljust(18)[0:18], day_5_color3).bold()}|   {cs(day_6_time3.ljust(18)[0:18], day_6_color3).bold()}|   {cs(day_7_time3.ljust(18)[0:17], day_7_color3).bold()}|")
print(f"  |   {cs(day_1_event3.ljust(18)[0:18], day_1_color3).bold()}|   {cs(day_2_event3.ljust(18)[0:18], day_2_color3).bold()}|   {cs(day_3_event3.ljust(18)[0:18], day_3_color3).bold()}|   {cs(day_4_event3.ljust(18)[0:18], day_4_color3).bold()}|   {cs(day_5_event3.ljust(18)[0:18], day_5_color3).bold()}|   {cs(day_6_event3.ljust(18)[0:18], day_6_color3).bold()}|   {cs(day_7_event3.ljust(18)[0:17], day_7_color3).bold()}|")
print(f"  |                     |                     |                     |                     |                     |                     |                    |  ")
print(f"  |                     |                     |                     |                     |                     |                     |                    |  ")
print(f"  |                     |                     |                     |                     |                     |                     |                    |  ")
print(f"  |                     |                     |                     |                     |                     |                     |                    |  ")
print(f"  |   {cs(day_1_time4.ljust(18)[0:18], day_1_color4).bold()}|   {cs(day_2_time4.ljust(18)[0:18], day_2_color4).bold()}|   {cs(day_3_time4.ljust(18)[0:18], day_3_color4).bold()}|   {cs(day_4_time4.ljust(18)[0:18], day_4_color4).bold()}|   {cs(day_5_time4.ljust(18)[0:18], day_5_color4).bold()}|   {cs(day_6_time4.ljust(18)[0:18], day_6_color4).bold()}|   {cs(day_7_time4.ljust(18)[0:17], day_7_color4).bold()}|")
print(f"  |   {cs(day_1_event4.ljust(18)[0:18], day_1_color4).bold()}|   {cs(day_2_event4.ljust(18)[0:18], day_2_color4).bold()}|   {cs(day_3_event4.ljust(18)[0:18], day_3_color4).bold()}|   {cs(day_4_event4.ljust(18)[0:18], day_4_color4).bold()}|   {cs(day_5_event4.ljust(18)[0:18], day_5_color4).bold()}|   {cs(day_6_event4.ljust(18)[0:18], day_6_color4).bold()}|   {cs(day_7_event4.ljust(18)[0:17], day_7_color4).bold()}|")
print(f"  |                     |                     |                     |                     |                     |                     |                    |  ")
print(f"  |                     |                     |                     |                     |                     |                     |                    |  ")
print(f"  |                     |                     |                     |                     |                     |                     |                    |  ")
print(f"  |                     |                     |                     |                     |                     |                     |                    |  ")
print(f"  |   {cs(day_1_time5.ljust(18)[0:18], day_1_color5).bold()}|   {cs(day_2_time5.ljust(18)[0:18], day_2_color5).bold()}|   {cs(day_3_time5.ljust(18)[0:18], day_3_color5).bold()}|   {cs(day_4_time5.ljust(18)[0:18], day_4_color5).bold()}|   {cs(day_5_time5.ljust(18)[0:18], day_5_color5).bold()}|   {cs(day_6_time5.ljust(18)[0:18], day_6_color5).bold()}|   {cs(day_7_time5.ljust(18)[0:17], day_7_color5).bold()}|")
print(f"  |   {cs(day_1_event5.ljust(18)[0:18], day_1_color5).bold()}|   {cs(day_2_event5.ljust(18)[0:18], day_2_color5).bold()}|   {cs(day_3_event5.ljust(18)[0:18], day_3_color5).bold()}|   {cs(day_4_event5.ljust(18)[0:18], day_4_color5).bold()}|   {cs(day_5_event5.ljust(18)[0:18], day_5_color5).bold()}|   {cs(day_6_event5.ljust(18)[0:18], day_6_color5).bold()}|   {cs(day_7_event5.ljust(18)[0:17], day_7_color5).bold()}|")
print(f"  |                     |                     |                     |                     |                     |                     |                    |  ")
print(f"  |                     |                     |                     |                     |                     |                     |                    |  ")
print(f"  |                     |                     |                     |                     |                     |                     |                    |  ")
print(f"  \--------------------------------------------------------------------------------------------------------------------------------------------------------/  ")

print(f"\t\t\t\t\t\t COLOR CODES:\t{cs('HOME CALENDAR', HOME_CALENDAR_COLOR).bold().underline()} {cs('SCHOOL CALENDAR', HOME_WORK_CALENDAR_COLOR).bold().underline()}")
