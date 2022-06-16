from datetime import datetime
import cal_class as cal
import os
import calendar_data as cal_data

calendar = cal.Calendar()

# events here    
calendar_data = cal_data.calendar_data.run("d")
# print(calendar_data, end ='\n\n\n\n')


#  split on 'endofday' then pass the list

event = []
events = []
for i in range(len(calendar_data)):
    if (calendar_data[i] != 'endofday'):
        event.append(calendar_data[i])
    else:
        events.append(event)
        event = []

# print(events)
calendar.draw_section(events)
