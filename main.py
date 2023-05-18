from datetime import datetime
import cal_class as cal
import os
import calendar_data as cal_data

call_event_handler = cal_data.Event_handler()
num_of_calendars = call_event_handler.get_num_of_calendars()

birthdayID = ""   
workID = ""
basicID = ""

calendar = cal.Calendar(num_of_calendars)
cal_data = []

cal_data.append([call_event_handler.main(workID)])
cal_data.append([call_event_handler.main(basicID)])
cal_data.append([call_event_handler.main(birthdayID)])


calendar.draw_section(cal_data)

