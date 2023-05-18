# google-calendar-command-line
this is my google calendar app that connects to your google calendar and displays your calendar in a terminal window. make this program run every time you open a terminal

to get started you will need to get your calendar ID from google

When you have that you can have a max of 3 by default. 
    replace the text for the three ID's under under BirthdayID workID and normal in the 
    file main.py and calendar_dataa.py

save and run main.py

it should ask you to log in with your google account and you should be good to go!




to change the number of calendars:
     1)go to the line "self.num_of_calendars = 3" in the file calendar_dataa.py
       change it to the number you want.

    2)create a new var with the calendars ID in main.py

    3)paste the line below the other lines that look like this in main.py (starts on line16) and replace "THE_NEW_ID"  with you ID you made
        cal_data.append([call_event_handler.main(THE_NEW_ID)])
    
    4) save and run