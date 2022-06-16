import os
import math
from rfc3339 import rfc3339
from datetime import timedelta
from datetime import date
import datetime
from termcolor import colored, cprint


class Calendar:
    def __init__(self):
        term_size = os.get_terminal_size()
        self.side_buffer = 2
        self.x = int(term_size[0]-self.side_buffer)
        self.y = int(term_size[1]) -1
        self.count = 0
        t = self.x - self.side_buffer
        text = ""
        self.da = datetime.date.today() + timedelta(days=self.count)
        self.da = self.da.strftime('%Y-%m-%d')

        date_len = len(self.da)
        self.basic_text= f"{self.side_buffer*' '}|{self.side_buffer*' '} {text} {'|':>{t-len(text)}}"
        self.tops = self.side_buffer*" " + "|" + int(self.x - 3 - self.side_buffer)*"-" + "|"
        self.bars = self.side_buffer*" " + "|" + int(self.x - 3 -self.side_buffer)*" " + "|"

    def draw_blank_screen(self):
        for i in range(math.floor(self.y/4)):
            print(self.tops)
            print(self.bars)
            print(self.basic_text)
            print(self.bars)
        print(self.tops)

    def draw_data_line(self, text):
        # t = self.x - (self.side_buffer * 2)
        print(f"{self.side_buffer*' '}|{self.side_buffer*' '}", end='')
        cprint(text[:101], 'yellow', end='')
        print(f"{'|':>{self.x -6- len(text)}}")
        return(self.basic_text)

    def print_top_bars(self, date):
        print(self.side_buffer*" " + "|  ",end='')
        cprint(date, 'cyan', 'on_grey',  attrs=['bold', 'underline'], end='')
        print(int((self.x - 3 -self.side_buffer) - 12)*" " + "|")


    def draw_section(self, text):
        count = 0
        for i in range(math.floor(self.y/4)):
            print(self.tops)
            da = datetime.date.today() + timedelta(days=count)
            da = da.strftime('%Y-%m-%d')
            self.print_top_bars(da)
            count = count +1
            self.draw_data_line("".join(text[i]))
            print(self.bars)
        print(self.tops)

    def parse_calendar(self, cal):
        pass