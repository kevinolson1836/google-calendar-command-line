from __future__ import print_function
from stringcolor import *
import datetime
import pickle
import geocoder
import os.path
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import datetime
from datetime import timedelta
from datetime import date
from rfc3339 import rfc3339
import requests
import json
from stringcolor import *
import pdb
import draw_cal as dc


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
PATH = 'credentials.json'
HOME_WORK_CALENDAR_COLOR = "#FF0000"
CLASSES_CALENDAR_COLOR = "#FFFFFF"
BIRTHDAY_CALENDAR_COLOR = "#FFC0CB"
HOME_CALENDAR_COLOR = "#6B8E23"
HOLIDAY_CALENDAR_COLOR = "#00FF00" 
NORMAL_CALENDAR_COLOR = "#FFA500"
DATE_COLOR = "#ffcd3c"
BOARD_COLOR = "#404040"
CRYPTO_COLOR = "#ffcd3c"
WEATHER = "WEATHER"
SCC_PRICE = "test value"
CRYPTO = "CRYPTO"
BTC_PRICE = ""
BTC_COLOR = "#B2840C"
ETH_PRICE = ""
ETH_COLOR = "#B2840C"
SCC_PRICE = ""
SCC_COLOR = "#B2840C"
WEATHER_COLOR = '#B2840C'
list_of_events = []

class Calendar:
    def __init__(self, response, color):
        self.response = response
        self.color = color

    def get_response(self):
        return self.response

    def get_color(self):
        return self.color

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
    classes = Calendar (response_from_api ("4tikr714t89qsjprpeijog83po@group.calendar.google.com", service, max_time, now, color="#FF6347"), color=CLASSES_CALENDAR_COLOR)
    home_cal = Calendar (response_from_api ("d47.org_l77q084fo5hdumaucnoqmu7ifs@group.calendar.google.com", service, max_time, now, color="#FF6347"), color=HOME_CALENDAR_COLOR)
    birthdays_cal = Calendar (response_from_api ("93ree9e9e3piqpimt1uiu596tg@group.calendar.google.com", service, max_time, now, color="#FF6347"), color = BIRTHDAY_CALENDAR_COLOR)
    holiday_cal = Calendar (response_from_api ("en.usa#holiday@group.v.calendar.google.com", service, max_time, now, color="#FF6347"), color = HOLIDAY_CALENDAR_COLOR)
    normal_cal = Calendar (response_from_api ("n12ih9qm9q8tfae88lhdu8gg24@group.calendar.google.com", service, max_time, now, color="#FF6347"), color = NORMAL_CALENDAR_COLOR)
    list_of_cals = [birthdays_cal, classes, normal_cal, home_cal, holiday_cal]
    return(list_of_cals)

def get_homework_response():
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
    home_work_cal = Calendar (response_from_api ("jd68d64fb2t5jr453apkuvkkcs@group.calendar.google.com", service, max_time, now, color="#FF6347"), color = HOME_WORK_CALENDAR_COLOR)
    event = home_work_cal.get_response()
    return_list =[]
    i = 0
    for each in range(12):
        if i >= len(event):
            return_list.append("")
        else:
            return_list.append(event[i])
        i = i+1
    return(return_list)

def parse_response(response):
    color = "#aaaaaa"
    i = -1
    for _ in response:
        i = i + 1
        event = _.get_response()
        if not event:
            pass
        else:
            for event in event:
                event_name = event[26:]
                event_day = event[8:10]

                if event[10] != " ":
                    event_time = str(event[11:13]) + ":" + str(event[14:16])
                    # print(event_time)
                    x = int(event_time[0:2])
                    if x > 12:
                        event_time = int(event_time[0:2]) - 12
                        event_time = "0" + str(event_time) + ":" + str(event[14:16]) + "PM"
                    else:
                        event_time = str(event_time) + "AM"
                else:
                    event_time = "ALL DAY"
                    event_name = event[11:]
                color = _.get_color()
                list_of_events.append([event_day, event_time, event_name, color])
                # print(list_of_events)
    return (list_of_events)


def main():
    response = get_api_response()
    parsed_response = parse_response(response)



main()

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
day_1_time6 = " "
day_1_event6 = " "
day_1_color6 = "#FFFFFF"
day_1_time7 = " "
day_1_event7 = " "
day_1_color7 = "#FFFFFF"
day_1_time8 = " "
day_1_event8 = " "
day_1_color8 = "#FFFFFF"

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
day_2_time6 = " "
day_2_event6 = " "
day_2_color6 = "#FFFFFF"
day_2_time7 = " "
day_2_event7 = " "
day_2_color7 = "#FFFFFF"
day_2_time8 = " "
day_2_event8 = " "
day_2_color8 = "#FFFFFF"

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
day_3_time6 = " "
day_3_event6 = " "
day_3_color6 = "#FFFFFF"
day_3_time7 = " "
day_3_event7 = " "
day_3_color7 = "#FFFFFF"
day_3_time8 = " "
day_3_event8 = " "
day_3_color8 = "#FFFFFF"


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
day_4_time6 = " "
day_4_event6 = " "
day_4_color6 = "#FFFFFF"
day_4_time7 = " "
day_4_event7 = " "
day_4_color7 = "#FFFFFF"
day_4_time8 = " "
day_4_event8 = " "
day_4_color8 = "#FFFFFF"


day_5_time1 = "day_5_time1"
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
day_5_time6 = " "
day_5_event6 = " "
day_5_color6 = "#FFFFFF"
day_5_time7 = " "
day_5_event7 = " "
day_5_color7 = "#FFFFFF"
day_5_time8 = " "
day_5_event8 = " "
day_5_color8 = "#FFFFFF"


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
day_6_time6 = " "
day_6_event6 = " "
day_6_color6 = "#FFFFFF"
day_6_time7 = " "
day_6_event7 = " "
day_6_color7 = "#FFFFFF"
day_6_time8 = " "
day_6_event8 = " "
day_6_color8 = "#FFFFFF"

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
day_7_time6 = " "
day_7_event6 = " "
day_7_color6 = "#FFFFFF"
day_7_time7 = " "
day_7_event7 = " "
day_7_color7 = "#FFFFFF"
day_7_time8 = " "
day_7_event8 = " "
day_7_color8 = "#FFFFFF"


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

dates = [
    [day_1],
    [day_2],
    [day_3],
    [day_4],
    [day_5],
    [day_6],
    [day_7],
]

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
        elif day_1_count == 6:
            day_1_time6 = list_of_events[i][1]
            day_1_event6 = list_of_events[i][2]
            day_1_color6 = list_of_events[i][3]
        elif day_1_count == 7:
            day_1_time7 = list_of_events[i][1]
            day_1_event7 = list_of_events[i][2]
            day_1_color7 = list_of_events[i][3]
        elif day_1_count == 8:
            day_1_time8 = list_of_events[i][1]
            day_1_event8 = list_of_events[i][2]
            day_1_color8 = list_of_events[i][3]
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
        elif day_2_count == 6:
            day_2_time6 = list_of_events[i][1]
            day_2_event6 = list_of_events[i][2]
            day_2_color6 = list_of_events[i][3]
        elif day_2_count == 7:
            day_2_time7 = list_of_events[i][1]
            day_2_event7 = list_of_events[i][2]
            day_2_color7 = list_of_events[i][3]
        elif day_2_count == 8:
            day_2_time8 = list_of_events[i][1]
            day_2_event8 = list_of_events[i][2]
            day_2_color8 = list_of_events[i][3]
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
        elif day_3_count == 6:
            day_3_time6 = list_of_events[i][1]
            day_3_event6 = list_of_events[i][2]
            day_3_color6 = list_of_events[i][3]
        elif day_3_count == 7:
            day_3_time7 = list_of_events[i][1]
            day_3_event7 = list_of_events[i][2]
            day_3_color7 = list_of_events[i][3]
        elif day_3_count == 8:
            day_3_time8 = list_of_events[i][1]
            day_3_event8 = list_of_events[i][2]
            day_3_color8 = list_of_events[i][3]
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
        elif day_4_count == 6:
            day_4_time6 = list_of_events[i][1]
            day_4_event6 = list_of_events[i][2]
            day_4_color6 = list_of_events[i][3]
        elif day_4_count == 7:
            day_4_time7 = list_of_events[i][1]
            day_4_event7 = list_of_events[i][2]
            day_4_color7 = list_of_events[i][3]
        elif day_4_count == 8:
            day_4_time8 = list_of_events[i][1]
            day_4_event8 = list_of_events[i][2]
            day_4_color8 = list_of_events[i][3]
        day_4_count = day_4_count+1
    if day_5_num == list_of_events[i][0]:
        if day_5_count == 1:
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
        elif day_5_count == 6:
            day_5_time6 = list_of_events[i][1]
            day_5_event6 = list_of_events[i][2]
            day_5_color6 = list_of_events[i][3]
        elif day_5_count == 7:
            day_5_time7 = list_of_events[i][1]
            day_5_event7 = list_of_events[i][2]
            day_5_color7 = list_of_events[i][3]
        elif day_5_count == 8:
            day_5_time8 = list_of_events[i][1]
            day_5_event8 = list_of_events[i][2]
            day_5_color8 = list_of_events[i][3]
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
        elif day_6_count == 6:
            day_6_time6 = list_of_events[i][1]
            day_6_event6 = list_of_events[i][2]
            day_6_color6 = list_of_events[i][3]
        elif day_6_count == 7:
            day_6_time7 = list_of_events[i][1]
            day_6_event7 = list_of_events[i][2]
            day_6_color7 = list_of_events[i][3]
        elif day_6_count == 8:
            day_6_time8 = list_of_events[i][1]
            day_6_event8 = list_of_events[i][2]
            day_6_color8 = list_of_events[i][3]
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
        elif day_7_count == 6:
            day_7_time6 = list_of_events[i][1]
            day_7_event6 = list_of_events[i][2]
            day_7_color6 = list_of_events[i][3]
        elif day_7_count == 7:
            day_7_time7 = list_of_events[i][1]
            day_7_event7 = list_of_events[i][2]
            day_7_color7 = list_of_events[i][3]
        elif day_7_count == 8:
            day_7_time8 = list_of_events[i][1]
            day_7_event8 = list_of_events[i][2]
            day_7_color8 = list_of_events[i][3]
        day_7_count = day_7_count+1
    i= i+1

times = [
        [day_1_time1,day_2_time1,day_3_time1,day_4_time1,day_5_time1,day_6_time1,day_7_time1],
        [day_1_time2,day_2_time2,day_3_time2,day_4_time2,day_5_time2,day_6_time2,day_7_time2],
        [day_1_time3,day_2_time3,day_3_time3,day_4_time3,day_5_time3,day_6_time3,day_7_time3],
        [day_1_time4,day_2_time4,day_3_time4,day_4_time4,day_5_time4,day_6_time4,day_7_time4],
        [day_1_time5,day_2_time5,day_3_time5,day_4_time5,day_5_time5,day_6_time5,day_7_time5],
        [day_1_time6,day_2_time6,day_3_time6,day_4_time6,day_5_time6,day_6_time6,day_7_time6],
        [day_1_time7,day_2_time7,day_3_time7,day_4_time7,day_5_time7,day_6_time7,day_7_time7],
        [day_1_time8,day_2_time8,day_3_time8,day_4_time8,day_5_time8,day_6_time8,day_7_time8]
]

events = [
    [day_1_event1,day_2_event1, day_3_event1, day_4_event1, day_5_event1, day_6_event1, day_7_event1],
    [day_1_event2,day_2_event2, day_3_event2, day_4_event2, day_5_event2, day_6_event2, day_7_event2],
    [day_1_event3,day_2_event3, day_3_event3, day_4_event3, day_5_event3, day_6_event3, day_7_event3],
    [day_1_event4,day_2_event4, day_3_event4, day_4_event4, day_5_event4, day_6_event4, day_7_event4],
    [day_1_event5,day_2_event5, day_3_event5, day_4_event5, day_5_event5, day_6_event5, day_7_event5],
    [day_1_event6,day_2_event6, day_3_event6, day_4_event6, day_5_event6, day_6_event6, day_7_event6],
    [day_1_event7,day_2_event7, day_3_event7, day_4_event7, day_5_event7, day_6_event7, day_7_event7],
    [day_1_event8,day_2_event8, day_3_event8, day_4_event8, day_5_event8, day_6_event8, day_7_event8]
]

colors = [
    [day_1_color1,day_2_color1, day_3_color1, day_4_color1, day_5_color1, day_6_color1, day_7_color1],
    [day_1_color2,day_2_color2, day_3_color2, day_4_color2, day_5_color2, day_6_color2, day_7_color2],
    [day_1_color3,day_2_color3, day_3_color3, day_4_color3, day_5_color3, day_6_color3, day_7_color3],
    [day_1_color4,day_2_color4, day_3_color4, day_4_color4, day_5_color4, day_6_color4, day_7_color4],
    [day_1_color5,day_2_color5, day_3_color5, day_4_color5, day_5_color5, day_6_color5, day_7_color5],
    [day_1_color6,day_2_color6, day_3_color6, day_4_color6, day_5_color6, day_6_color6, day_7_color6],
    [day_1_color7,day_2_color7, day_3_color7, day_4_color7, day_5_color7, day_6_color7, day_7_color7],
    [day_1_color8,day_2_color8, day_3_color8, day_4_color8, day_5_color8, day_6_color8, day_7_color8]
]

    
hw = get_homework_response()

# times = make_calendar_vars(list_of_events)
# print(f"\n\nthis is list_of_events: {list_of_events} \n\n\n\nthis is events: {events}\n\n\n this is times: {times}\n\n\n this is dates: {dates}\n\n\n this is colors: {colors}\n\n\nthis is homework: {hw}")
dc.print_calendar(times, events, dates, colors, hw)
x = os.get_terminal_size()
columns = int(x[0])
columns_half = columns/2
print(f"\t\t\t\t\t\t COLOR CODES:\t{cs('HOME', HOME_CALENDAR_COLOR).bold().underline()} {cs('HOMEWORK', HOME_WORK_CALENDAR_COLOR).bold().underline()} {cs('BIRTHDAY', BIRTHDAY_CALENDAR_COLOR).bold().underline()} {cs('CLASSES', CLASSES_CALENDAR_COLOR).bold().underline()} {cs('HOLIDAY CALENDAR', HOLIDAY_CALENDAR_COLOR).bold().underline()} {cs('NORMAL CALENDAR', NORMAL_CALENDAR_COLOR).bold().underline()}")
