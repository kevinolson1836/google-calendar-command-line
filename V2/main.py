from datetime import datetime
import cal_class as cal
import os
import calendar_data as cal_data

call_event_handler = cal_data.Event_handler()
num_of_calendars = call_event_handler.get_num_of_calendars()

birthdayID = "93ree9e9e3piqpimt1uiu596tg@group.calendar.google.com"
workID = "jd68d64fb2t5jr453apkuvkkcs@group.calendar.google.com"
Normal = "kevin.olson1836@gmail.com"
#Normal = "n12ih9qm9q8tfae88lhdu8gg24@group.calendar.google.com"

calendar = cal.Calendar(num_of_calendars)
cal_data = []

cal_data.append([call_event_handler.main(workID)])
cal_data.append([call_event_handler.main(Normal)])
cal_data.append([call_event_handler.main(birthdayID)])


calendar.draw_section(cal_data)

