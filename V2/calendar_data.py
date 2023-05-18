from __future__ import print_function
import datetime
import os.path
import os
from datetime import timedelta
from datetime import date
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

tokenPath = r'/home/kevin/code/google-calendar-command-line/V2/token.json'
credPath = r'/home/kevin/code/google-calendar-command-line/V2/credentials.json'
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
# If modifying these scopes, delete the file token.json.


class Event_handler:
    def __init__(self):
        self.birthdayID = "93ree9e9e3piqpimt1uiu596tg@group.calendar.google.com"
        self.workID = "jd68d64fb2t5jr453apkuvkkcs@group.calendar.google.com"
        self.basicID = "n12ih9qm9q8tfae88lhdu8gg24@group.calendar.google.com"
        self.num_of_calendars = 3

    def get_num_of_calendars(self):
        return(self.num_of_calendars)

    def main(self,calID):
        """Shows basic usage of the Google Calendar API.
        Prints the start and name of the next 10 events on the user's calendar.
        """
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(tokenPath):
            creds = Credentials.from_authorized_user_file(tokenPath, SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    credPath, SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(tokenPath, 'w') as token:
                token.write(creds.to_json())

        try:
            service = build('calendar', 'v3', credentials=creds)

            # Call the Calendar API
            now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
            end = datetime.datetime.utcnow() + datetime.timedelta(days=6)  
            end = end.isoformat() + 'Z'
            events_result = service.events().list(calendarId=calID, timeMin=now,
                                                timeMax=end,
                                                maxResults=10, singleEvents=True,
                                                orderBy='startTime').execute()
            events = events_result.get('items', [])

            if not events:
                return_list = []
                for i in range (7):
                    if (i == 0):
                        if (calID == "93ree9e9e3piqpimt1uiu596tg@group.calendar.google.com" ):
                            calName = "Birthdays"
                        if (calID == "jd68d64fb2t5jr453apkuvkkcs@group.calendar.google.com" ):
                            calName = "Work"
                        if (calID == "n12ih9qm9q8tfae88lhdu8gg24@group.calendar.google.com" ):
                            calName = "Normal"
                        return_list.append(calName)
                    else:
                        return_list.append(' ')
                return(return_list)

            # Prints the start and name of the next 10 events
            return_list = []
            for event in events:
               

                start = event['start'].get('dateTime', event['start'].get('date'))
                date_1 = datetime.datetime.strptime(start, r'%Y-%m-%d')
                start = (datetime.datetime.strptime(start, r'%Y-%m-%d')).strftime(r'%m/%d/%y')

           
                for i in range (7):
                    if (i == 0):
                        if (calID == "93ree9e9e3piqpimt1uiu596tg@group.calendar.google.com" ):
                            calName = "Birthdays"
                        if (calID == "jd68d64fb2t5jr453apkuvkkcs@group.calendar.google.com" ):
                            calName = "Work"
                        if (calID == "n12ih9qm9q8tfae88lhdu8gg24@group.calendar.google.com" ):
                            calName = "Normal"
                        return_list.append(calName)
                    elif (start == str((datetime.datetime.utcnow() + datetime.timedelta(days=i-2    )).strftime(r'%m/%d/%y'))):
                        return_list.append(event['summary'])
                    else:
                        return_list.append(' ')
                return(return_list)


        except HttpError as error:
            print('An error occurred: %s' % error)