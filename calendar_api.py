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
PATH = '/home/kevin/code/projects/google-calendar-command-line/credentials.json'
HOME_WORK_CALENDAR_COLOR = "#FF0000"
CLASSES_CALENDAR_COLOR = "#FFFFFF"
BIRTHDAY_CALENDAR_COLOR = "#FFC0CB"
HOME_CALENDAR_COLOR = "#6B8E23"
HOLIDAY_CALENDAR_COLOR = "#00FF00" 
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
    home_work_cal = Calendar (response_from_api ("jd68d64fb2t5jr453apkuvkkcs@group.calendar.google.com", service, max_time, now, color="#FF6347"), color = HOME_WORK_CALENDAR_COLOR)
    list_of_cals = [birthdays_cal, home_work_cal, classes, home_cal, holiday_cal]
    return(list_of_cals)

def parse_response(response):
    color = "#aaaaaa"
    i = -1
    for _ in response:
        i = i + 1
        event = _.get_response()
        if not event:
            # print("response is empty")
            pass
        else:
            for event in event:
                # print(event)
                event_name = event[26:]
                event_day = event[8:10]
                # print(event_name)
                # print(event_day)
                # pdb.set_trace()
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
    return (list_of_events)


def get_crypto_prices():

    btc = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin&order=market_cap_desc&per_page=100&page=1&sparkline=false")
    eth = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=ethereum&order=market_cap_desc&per_page=100&page=1&sparkline=false")
    scc = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=stakecube&order=market_cap_desc&per_page=100&page=1&sparkline=false")
    btc_response = btc.json()
    eth_response = eth.json()
    scc_response = scc.json()

    btc_price = str(btc_response[0].get("current_price", ""))
    eth_price = str(eth_response[0].get("current_price", ""))
    scc_price = str(scc_response[0].get("current_price", ""))

    return ([btc_price, eth_price, scc_price])

def get_long_lat():
    g = geocoder.ip('me')
    return ([g.lng, g.lat])

def get_task():
    return requests.get('https://www.googleapis.com/tasks/v1/users/@me/').json()

def get_email():
    # does not work right now
    print(requests.get("https://outlook.office.com/api/v2.0/me/MailFolders/Inbox/messages"))


def main():
    response = get_api_response()
    parsed_response = parse_response(response)
    # get_email()
    # print(get_task())



main()

crypto_prices = get_crypto_prices()
BTC_PRICE = "BTC: " + crypto_prices[0].ljust(10)
ETH_PRICE = "ETH: " + crypto_prices[1].ljust(10)
SCC_PRICE = "SCC: " + crypto_prices[2].ljust(10)

long_lat = get_long_lat()
lon = float(long_lat[0])
lat = float(long_lat[1])
req = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&%20exclude=minutely,hourly,daily&appid=1eccf9f2ce1ff09a93396d5c8013af5e"
weather_response = requests.get(req)
weather_response = weather_response.json()
dump = json.dumps(weather_response, indent=4)
temp = weather_response["current"].get("temp", "")
feel_like = weather_response["current"].get("feels_like", "")
weather = weather_response["current"].get("weather", "")[0].get("description", "")

temp = "temp " + str(((float(json.dumps(temp, indent=4))*9)/5)-459.67 )
feel_like = "feel like " + str(((float(json.dumps(feel_like, indent=4))*9)/5)-459.67 )
weather = (json.dumps(weather, indent=4)).strip('"')


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
            print(day_7_color5)
            print(day_7_color5)
            print(day_7_color5)
            print(day_7_color5)
            print(day_7_color5)
            print(day_7_color5)
            print(day_7_color5)
            print(day_7_color5)
        day_7_count = day_7_count+1
    i= i+1

times = [
        [day_1_time1,day_2_time1,day_3_time1,day_4_time1,day_5_time1,day_6_time1,day_7_time1],
        [day_1_time2,day_2_time2,day_3_time2,day_4_time2,day_5_time2,day_6_time2,day_7_time2],
        [day_1_time3,day_2_time3,day_3_time3,day_4_time3,day_5_time3,day_6_time3,day_7_time3],
        [day_1_time4,day_2_time4,day_3_time4,day_4_time4,day_5_time4,day_6_time4,day_7_time4],
        [day_1_time5,day_2_time5,day_3_time5,day_4_time5,day_5_time5,day_6_time5,day_7_time5]
]

events = [
    [day_1_event1,day_2_event1, day_3_event1, day_4_event1, day_5_event1, day_6_event1, day_7_event1],
    [day_1_event2,day_2_event2, day_3_event2, day_4_event2, day_5_event2, day_6_event2, day_7_event2],
    [day_1_event3,day_2_event3, day_3_event3, day_4_event3, day_5_event3, day_6_event3, day_7_event3],
    [day_1_event4,day_2_event4, day_3_event4, day_4_event4, day_5_event4, day_6_event4, day_7_event4],
    [day_1_event5,day_2_event5, day_3_event5, day_4_event5, day_5_event5, day_6_event5, day_7_event5]
]

colors = [
    [day_1_color1,day_2_color1, day_3_color1, day_4_color1, day_5_color1, day_6_color1, day_7_color1],
    [day_1_color2,day_2_color2, day_3_color2, day_4_color2, day_5_color2, day_6_color2, day_7_color2],
    [day_1_color3,day_2_color3, day_3_color3, day_4_color3, day_5_color3, day_6_color3, day_7_color3],
    [day_1_color4,day_2_color4, day_3_color4, day_4_color4, day_5_color4, day_6_color4, day_7_color4],
    [day_1_color5,day_2_color5, day_3_color5, day_4_color5, day_5_color5, day_6_color5, day_7_color5]
]
    

# times = make_calendar_vars(list_of_events)
# print(f"\n\nthis is events: {events}\n\n\n this is times: {times}\n\n\n this is dates: {dates}\n\n\n this is colors: {colors}\n\n\nn")
dc.print_calendar(times, events, dates, colors)
x = os.get_terminal_size()
columns = int(x[0])
columns_half = columns/2
print(f"\t\t\t\t\t\t COLOR CODES:\t{cs('HOME', HOME_CALENDAR_COLOR).bold().underline()} {cs('HOMEWORK', HOME_WORK_CALENDAR_COLOR).bold().underline()} {cs('BIRTHDAY', BIRTHDAY_CALENDAR_COLOR).bold().underline()} {cs('CLASSES', CLASSES_CALENDAR_COLOR).bold().underline()} {cs('HOLIDAY CALENDAR', HOLIDAY_CALENDAR_COLOR).bold().underline()}")
