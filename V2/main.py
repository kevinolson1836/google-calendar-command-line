from datetime import datetime
import cal_class as cal
import os
import calendar_data as cal_data

call_event_handler = cal_data.Event_handler()
num_of_calendars = call_event_handler.get_num_of_calendars()

birthdayID = "93ree9e9e3piqpimt1uiu596tg@group.calendar.google.com"   
workID = "jd68d64fb2t5jr453apkuvkkcs@group.calendar.google.com"
basicID = "n12ih9qm9q8tfae88lhdu8gg24@group.calendar.google.com"

calendar = cal.Calendar(num_of_calendars)
cal_data = [

           ]

# print(call_event_handler.main())
# cal_data = cal_data.get_all_events()
# cal_data.append([call_event_handler.main(workID)])
# cal_data.append([call_event_handler.main(basicID)])
print(call_event_handler.main(birthdayID))
cal_data.append([call_event_handler.main(workID)])
cal_data.append([call_event_handler.main(basicID)])
cal_data.append([call_event_handler.main(birthdayID)])
calendar.draw_section(cal_data)

