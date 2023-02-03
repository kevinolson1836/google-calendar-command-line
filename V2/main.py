from datetime import datetime
import cal_class as cal
import os
import calendar_data as cal_data

calendar = cal.Calendar()

cal_data = [
            ["oddddd", "odd", "english", "french", "sexxxxxx","bigmama"],
            ["it363", "math120", "", "french", "d","bigmama"],
            ["d", "d", "james bday", "d", "d","bigmama"],
            ["", "d", "d", "d", "d","d"],
            ["chore", "clean house", "drive mom", "", "","bigmama"]
           ]

calendar.draw_section(cal_data)



# events here    
# calendar_data = cal_data.calendar_data.run("")
# print(calendar_data, end ='\n\n\n\n')


# #  split on 'endofday' then pass the list

# event = []
# events = []
# for i in range(len(calendar_data)):
#     if (calendar_data[i] != 'endofday'):
#         event.append(calendar_data[i])
#     else:
#         events.append(event)
#         event = []

# # print(events)
# print("drwing")
# calendar.draw_section(events)
