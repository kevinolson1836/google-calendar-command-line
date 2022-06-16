from __future__ import print_function
import datetime
import os.path
import os
from rfc3339 import rfc3339
from datetime import timedelta
from datetime import date
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
# If modifying these scopes, delete the file token.json.

birthday = "93ree9e9e3piqpimt1uiu596tg@group.calendar.google.com"
classes = "4tikr714t89qsjprpeijog83po@group.calendar.google.com"
homework = "jd68d64fb2t5jr453apkuvkkcs@group.calendar.google.com"
basic = "n12ih9qm9q8tfae88lhdu8gg24@group.calendar.google.com"

def get_events(service, calid, mintime, maxtime):
    return_list =[]
    events_result = service.events().list(calendarId=calid, timeMin=mintime, timeMax=maxtime,
                                            maxResults=10, singleEvents=True,
                                            orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        pass
    for event in events:
        data = []
        start = event['start'].get('dateTime', event['start'].get('date'))

        x = [start, event['summary']]

        return_list.append(x)
    return(return_list)

class calendar_data:
    def response_from_api(calID, service, max_time, now, color):
        events_result = service.events().list(calendarId=calID, timeMax=max_time, timeMin=now,
                                            maxResults=200, singleEvents=True,
                                            orderBy='startTime').execute()
        events = events_result.get('items', [])

    def run(data):
        """Shows basic usage of the Google Calendar API.
        Prints the start and name of the next 10 events on the user's calendar.
        """
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        service = build('calendar', 'v3', credentials=creds)
        


        term_size = os.get_terminal_size()
        num_section = int(term_size[1])/4
        dates = []
        for i in range(int(num_section)):
            da = datetime.date.today() + timedelta(days=i)
            dates.append(da.strftime('%Y-%m-%d'))
        # print(dates)
        # Call the Calendar API

        #time data
        mintime = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        maxtime = datetime.date.today() + datetime.timedelta(days=num_section)  #math.floor(self.y/4)
        maxtime = rfc3339(maxtime)

        #calendars
        birthday_calendar = get_events(service, birthday, mintime, maxtime)
        classes_calendar = get_events(service, classes, mintime, maxtime)
        homework_calendar = get_events(service, homework, mintime, maxtime)
        basic_calendar = get_events(service, basic, mintime, maxtime)

        max_len = [len(birthday_calendar) , len(classes_calendar), len(homework_calendar), len(basic_calendar)]
        max_len.sort()
        all_events = []
        for i in range(max_len[-1]):
            try:
                # print(birthday_calendar[i][0])
                day = datetime.datetime.today().strftime('%Y-%m-%d')
                # print(homework_calendar[i])
                # print("current day: " + day)
                # print("next day: " + )
            
            except:
                pass
            try:
                if (homework_calendar[i][0] == dates[i]):  # compaire dates if its current date, next loop would be current day +1
                    all_events.append(homework_calendar[i][1])
            except:
                pass
            try:
                if (homework_calendar[i][0] == dates[i]):
                    all_events.append(birthday_calendar[i][1])
            except:
                pass
            try:
                if (homework_calendar[i][0] == dates[i]):
                    all_events.append(basic_calendar[i][1])
            except:
                pass
            try:
                if (homework_calendar[i][0] == dates[i]):
                    all_events.append(classes_calendar[i][1])
            except:
                pass
            all_events.append("endofday")
        return (all_events)