import os
import pdb
from stringcolor import *

WEATHER = "weather"
WEATHER_COLOR = "#FF000"
SPACE = " "
global OVERFLOW
OVERFLOW = ["","","","","","","","","","",]
OVERFLOW_ = "check calendar"
OVERFLOW_COLOR = "#FFCC00"
overflow_flag=False
x = os.get_terminal_size()
columns = x[0]
line = x[1]
spacing = int(((columns-10)/8)-3)
side = 5

def print_empty_line(spacing):
    print(f"    |"," "*spacing ,"|"," "*spacing ,"|"," "*spacing ,"|"," "*spacing ,"|"," "*spacing ,"|"," "*spacing ,"|"," "*spacing ,"|"," "*(spacing+side) ,"|")

def print_bar(columns):
    print("    |", end='')
    for _ in range(0,8):
        if _ == 7:
            print(f"-"* ((spacing)+7), end='')
            print("|", end='')
        else:
            print(f"-"* ((spacing)+2), end='')
            print("|", end='')
    print()

def overflow():
    print(f"    |"," "*spacing ,"|"," "*spacing ,"|"," "*spacing ,"|"," "*spacing ,"|"," "*spacing ,"|"," "*spacing ,"|"," "*spacing ,"|"," "*(spacing+side) ,"|")

def print_calendar(times, events, dates, colors, homework):
    overflow_flag=False
    WEATHER = "Homework"
    WEATHER_COLOR = "#FF0000"
    SPACE = " "
    x = os.get_terminal_size()
    columns = x[0]
    line = x[1]
    spacing = int(((columns-10)/8)-3)
    side = 5

    COUNT = 0
    print_bar(columns)
    for _ in range(line-24): 
        print_empty_line(spacing)
        if COUNT == 0:
            print(f"    |  {dates[0][0].ljust(spacing)[0:spacing-1]} |  {dates[1][0].ljust(spacing)[0:spacing-1]} |  {dates[2][0].ljust(spacing)[0:spacing-1]} |  {dates[3][0].ljust(spacing)[0:spacing-1]} |  {dates[4][0].ljust(spacing)[0:spacing-1]} |  {dates[5][0].ljust(spacing)[0:spacing-1]} |  {dates[6][0].ljust(spacing)[0:spacing-1]} |        {cs(WEATHER[0:spacing].ljust(spacing-1), WEATHER_COLOR )}|")
        if COUNT == 1:
            print_bar(columns)
        if COUNT == 2:
            print(f"    |   {cs(times[0][0].ljust(spacing-1)[0:spacing-1], colors[0][0])}|   {cs(times[0][1].ljust(17)[0:spacing-1], colors[0][1])}|   {cs(times[0][2].ljust(17)[0:spacing-1], colors[0][2])}|   {cs(times[0][3].ljust(17)[0:spacing-1], colors[0][3])}|   {cs(times[0][4].ljust(17)[0:spacing-1], colors[0][4])}|   {cs(times[0][5].ljust(17)[0:spacing-1], colors[0][5])}|   {cs(times[0][6].ljust(17)[0:spacing-1], colors[0][6])}|  {cs(homework[0][26:].ljust(22), WEATHER_COLOR)}|")
            print(f"    |   {cs(events[0][0].ljust(spacing-1)[0:spacing-1], colors[0][0])}|   {cs(events[0][1].ljust(17)[0:spacing-1], colors[0][1])}|   {cs(events[0][2].ljust(17)[0:spacing-1], colors[0][2])}|   {cs(events[0][3].ljust(17)[0:spacing-1], colors[0][3])}|   {cs(events[0][4].ljust(17)[0:spacing-1], colors[0][4])}|   {cs(events[0][5].ljust(17)[0:spacing-1], colors[0][5])}|   {cs(events[0][6].ljust(17)[0:spacing-1], colors[0][6])}|  {cs(homework[0][:10].ljust(22), WEATHER_COLOR)}|")
        if COUNT == 4:
            print(f"    |   {cs(times[1][0].ljust(spacing-1)[0:spacing-1], colors[1][0])}|   {cs(times[1][1].ljust(17)[0:spacing-1], colors[1][1])}|   {cs(times[1][2].ljust(17)[0:spacing-1], colors[1][2])}|   {cs(times[1][3].ljust(17)[0:spacing-1], colors[1][3])}|   {cs(times[1][4].ljust(17)[0:spacing-1], colors[1][4])}|   {cs(times[1][5].ljust(17)[0:spacing-1], colors[1][5])}|   {cs(times[1][6].ljust(17)[0:spacing-1], colors[1][6])}|  {cs(homework[1][26:].ljust(22), WEATHER_COLOR)}|")
            print(f"    |   {cs(events[1][0].ljust(spacing-1)[0:spacing-1], colors[1][0])}|   {cs(events[1][1].ljust(17)[0:spacing-1], colors[1][1])}|   {cs(events[1][2].ljust(17)[0:spacing-1], colors[1][2])}|   {cs(events[1][3].ljust(17)[0:spacing-1], colors[1][3])}|   {cs(events[1][4].ljust(17)[0:spacing-1], colors[1][4])}|   {cs(events[1][5].ljust(17)[0:spacing-1], colors[1][5])}|   {cs(events[1][6].ljust(17)[0:spacing-1], colors[1][6])}|  {cs(homework[1][:10].ljust(22), WEATHER_COLOR)}|")
        if COUNT == 6:
            print(f"    |   {cs(times[2][0].ljust(spacing-1)[0:spacing-1], colors[2][0])}|   {cs(times[2][1].ljust(17)[0:spacing-1], colors[2][1])}|   {cs(times[2][2].ljust(17)[0:spacing-1], colors[2][2])}|   {cs(times[2][3].ljust(17)[0:spacing-1], colors[2][3])}|   {cs(times[2][4].ljust(17)[0:spacing-1], colors[2][4])}|   {cs(times[2][5].ljust(17)[0:spacing-1], colors[2][5])}|   {cs(times[2][6].ljust(17)[0:spacing-1], colors[2][6])}|  {cs(homework[2][26:].ljust(22), WEATHER_COLOR)}|")
            print(f"    |   {cs(events[2][0].ljust(spacing-1)[0:spacing-1], colors[2][0])}|   {cs(events[2][1].ljust(17)[0:spacing-1], colors[2][1])}|   {cs(events[2][2].ljust(17)[0:spacing-1], colors[2][2])}|   {cs(events[2][3].ljust(17)[0:spacing-1], colors[2][3])}|   {cs(events[2][4].ljust(17)[0:spacing-1], colors[2][4])}|   {cs(events[2][5].ljust(17)[0:spacing-1], colors[2][5])}|   {cs(events[2][6].ljust(17)[0:spacing-1], colors[2][6])}|  {cs(homework[2][:10].ljust(22), WEATHER_COLOR)}|")
        if COUNT == 8:
            print(f"    |   {cs(times[3][0].ljust(spacing-1)[0:spacing-1], colors[3][0])}|   {cs(times[3][1].ljust(17)[0:spacing-1], colors[3][1])}|   {cs(times[3][2].ljust(17)[0:spacing-1], colors[3][2])}|   {cs(times[3][3].ljust(17)[0:spacing-1], colors[3][3])}|   {cs(times[3][4].ljust(17)[0:spacing-1], colors[3][4])}|   {cs(times[3][5].ljust(17)[0:spacing-1], colors[3][5])}|   {cs(times[3][6].ljust(17)[0:spacing-1], colors[3][6])}|  {cs(homework[3][26:].ljust(22), WEATHER_COLOR)}|")
            print(f"    |   {cs(events[3][0].ljust(spacing-1)[0:spacing-1], colors[3][0])}|   {cs(events[3][1].ljust(17)[0:spacing-1], colors[3][1])}|   {cs(events[3][2].ljust(17)[0:spacing-1], colors[3][2])}|   {cs(events[3][3].ljust(17)[0:spacing-1], colors[3][3])}|   {cs(events[3][4].ljust(17)[0:spacing-1], colors[3][4])}|   {cs(events[3][5].ljust(17)[0:spacing-1], colors[3][5])}|   {cs(events[3][6].ljust(17)[0:spacing-1], colors[3][6])}|  {cs(homework[3][:10].ljust(22), WEATHER_COLOR)}|")
        if COUNT == 10:
            print(f"    |   {cs(times[4][0].ljust(spacing-1)[0:spacing-1], colors[4][0])}|   {cs(times[4][1].ljust(17)[0:spacing-1], colors[4][1])}|   {cs(times[4][2].ljust(17)[0:spacing-1], colors[4][2])}|   {cs(times[4][3].ljust(17)[0:spacing-1], colors[4][3])}|   {cs(times[4][4].ljust(17)[0:spacing-1], colors[4][4])}|   {cs(times[4][5].ljust(17)[0:spacing-1], colors[4][5])}|   {cs(times[4][6].ljust(17)[0:spacing-1], colors[4][6])}|  {cs(homework[4][26:].ljust(22), WEATHER_COLOR)}|")
            print(f"    |   {cs(events[4][0].ljust(spacing-1)[0:spacing-1], colors[4][0])}|   {cs(events[4][1].ljust(17)[0:spacing-1], colors[4][1])}|   {cs(events[4][2].ljust(17)[0:spacing-1], colors[4][2])}|   {cs(events[4][3].ljust(17)[0:spacing-1], colors[4][3])}|   {cs(events[4][4].ljust(17)[0:spacing-1], colors[4][4])}|   {cs(events[4][5].ljust(17)[0:spacing-1], colors[4][5])}|   {cs(events[4][6].ljust(17)[0:spacing-1], colors[4][6])}|  {cs(homework[4][:10].ljust(22), WEATHER_COLOR)}|")
        if COUNT == 12:
            print(f"    |   {cs(times[5][0].ljust(spacing-1)[0:spacing-1], colors[5][0])}|   {cs(times[5][1].ljust(17)[0:spacing-1], colors[5][1])}|   {cs(times[5][2].ljust(17)[0:spacing-1], colors[5][2])}|   {cs(times[5][3].ljust(17)[0:spacing-1], colors[5][3])}|   {cs(times[5][4].ljust(17)[0:spacing-1], colors[5][4])}|   {cs(times[5][5].ljust(17)[0:spacing-1], colors[5][5])}|   {cs(times[5][6].ljust(17)[0:spacing-1], colors[5][6])}|  {cs(homework[5][26:].ljust(22), WEATHER_COLOR)}|")
            print(f"    |   {cs(events[5][0].ljust(spacing-1)[0:spacing-1], colors[5][0])}|   {cs(events[5][1].ljust(17)[0:spacing-1], colors[5][1])}|   {cs(events[5][2].ljust(17)[0:spacing-1], colors[5][2])}|   {cs(events[5][3].ljust(17)[0:spacing-1], colors[5][3])}|   {cs(events[5][4].ljust(17)[0:spacing-1], colors[5][4])}|   {cs(events[5][5].ljust(17)[0:spacing-1], colors[5][5])}|   {cs(events[5][6].ljust(17)[0:spacing-1], colors[5][6])}|  {cs(homework[5][:10].ljust(22), WEATHER_COLOR)}|")
        if COUNT == 14:
            print(f"    |   {cs(times[6][0].ljust(spacing-1)[0:spacing-1], colors[6][0])}|   {cs(times[6][1].ljust(17)[0:spacing-1], colors[6][1])}|   {cs(times[6][2].ljust(17)[0:spacing-1], colors[6][2])}|   {cs(times[6][3].ljust(17)[0:spacing-1], colors[6][3])}|   {cs(times[6][4].ljust(17)[0:spacing-1], colors[6][4])}|   {cs(times[6][5].ljust(17)[0:spacing-1], colors[6][5])}|   {cs(times[6][6].ljust(17)[0:spacing-1], colors[6][6])}|  {cs(homework[6][26:].ljust(22), WEATHER_COLOR)}|")
            print(f"    |   {cs(events[6][0].ljust(spacing-1)[0:spacing-1], colors[6][0])}|   {cs(events[6][1].ljust(17)[0:spacing-1], colors[6][1])}|   {cs(events[6][2].ljust(17)[0:spacing-1], colors[6][2])}|   {cs(events[6][3].ljust(17)[0:spacing-1], colors[6][3])}|   {cs(events[6][4].ljust(17)[0:spacing-1], colors[6][4])}|   {cs(events[6][5].ljust(17)[0:spacing-1], colors[6][5])}|   {cs(events[6][6].ljust(17)[0:spacing-1], colors[6][6])}|  {cs(homework[6][:10].ljust(22), WEATHER_COLOR)}|")
        if COUNT == 16:
            print(f"    |   {cs(times[7][0].ljust(spacing-1)[0:spacing-1], colors[7][0])}|   {cs(times[7][1].ljust(17)[0:spacing-1], colors[7][1])}|   {cs(times[7][2].ljust(17)[0:spacing-1], colors[7][2])}|   {cs(times[7][3].ljust(17)[0:spacing-1], colors[7][3])}|   {cs(times[7][4].ljust(17)[0:spacing-1], colors[7][4])}|   {cs(times[7][5].ljust(17)[0:spacing-1], colors[7][5])}|   {cs(times[7][6].ljust(17)[0:spacing-1], colors[7][6])}|  {cs(homework[7][26:].ljust(22), WEATHER_COLOR)}|")
            print(f"    |   {cs(events[7][0].ljust(spacing-1)[0:spacing-1], colors[7][0])}|   {cs(events[7][1].ljust(17)[0:spacing-1], colors[7][1])}|   {cs(events[7][2].ljust(17)[0:spacing-1], colors[7][2])}|   {cs(events[7][3].ljust(17)[0:spacing-1], colors[7][3])}|   {cs(events[7][4].ljust(17)[0:spacing-1], colors[7][4])}|   {cs(events[7][5].ljust(17)[0:spacing-1], colors[7][5])}|   {cs(events[7][6].ljust(17)[0:spacing-1], colors[7][6])}|  {cs(homework[7][:10].ljust(22), WEATHER_COLOR)}|")
        if COUNT == line-25:
            for i in range(0,7):
                if len(events[7][i]) > 1:
                    OVERFLOW[i] = "OVERFLOW"
            print_empty_line(spacing)
            print(f"    |   {cs(OVERFLOW[0].ljust(17)[0:spacing-1], OVERFLOW_COLOR)}|   {cs(OVERFLOW[2].ljust(17)[0:spacing-1], OVERFLOW_COLOR)}|   {cs(OVERFLOW[3].ljust(17)[0:spacing-1], OVERFLOW_COLOR)}|   {cs(OVERFLOW[4].ljust(17)[0:spacing-1], OVERFLOW_COLOR)}|   {cs(OVERFLOW[5].ljust(17)[0:spacing-1], OVERFLOW_COLOR)}|   {cs(OVERFLOW[6].ljust(17)[0:spacing-1], OVERFLOW_COLOR)}|   {cs(OVERFLOW[7].ljust(17)[0:spacing-1], OVERFLOW_COLOR)}|  {cs(OVERFLOW[8].ljust(22), OVERFLOW_COLOR)}|")
                # print(f"    |   {cs(events[7][0].ljust(spacing-1)[0:spacing-1], colors[7][0])}|   {cs(events[7][1].ljust(17)[0:spacing-1], colors[7][1])}|   {cs(events[7][2].ljust(17)[0:spacing-1], colors[7][2])}|   {cs(events[7][3].ljust(17)[0:spacing-1], colors[7][3])}|   {cs(events[7][4].ljust(17)[0:spacing-1], colors[7][4])}|   {cs(events[7][5].ljust(17)[0:spacing-1], colors[7][5])}|   FFCC00|  {cs(homework[7][:10].ljust(22), WEATHER_COLOR)}|")
        COUNT +=1
    print_bar(columns)
    # print("\t\t\t\t\t\t color codes here")

if __name__ == "__main__":
    test_events = [
        ["apple", "banana", "pizza", "kevin", "lion", "cake", "tumric"],
        ["apple", "banana", "pizza", "kevin", "lion", "cake", "tumric"],
        ["apple", "banana", "pizza", "kevin", "lion", "cake", "tumric"],
        ["apple", "banana", "pizza", "kevin", "lion", "cake", "tumric"],
        ["apple", "banana", "pizza", "kevin", "lion", "cake", "tumric"],
        ["apple", "banana", "pizza", "kevin", "lion", "cake", "tumric"],
        ["apple", "banana", "pizza", "kevin", "lion", "cake", "tumric"],
        ["apple", "banana", "pizza", "kevin", "lion", "cake", "tumric"]
    ]
    dates = ["Jul-Thu-16"]
    test_times = [
        ["10am","10am","10am","10am","10am","10am","10am","10am","10am","10am","10am"],
        ["10am","10am","10am","10am","10am","10am","10am","10am","10am","10am","10am"],
        ["10am","10am","10am","10am","10am","10am","10am","10am","10am","10am","10am"],
        ["10am","10am","10am","10am","10am","10am","10am","10am","10am","10am","10am"],
        ["10am","10am","10am","10am","10am","10am","10am","10am","10am","10am","10am"],
        ["10am","10am","10am","10am","10am","10am","10am","10am","10am","10am","10am"],
        ["10am","10am","10am","10am","10am","10am","10am","10am","10am","10am","10am"]
    ]



    print(f"colums: {columns}\nline: {line}\nspaceing: {spacing}\n")
    print(f"this is events: {test_events}\n\n\n this is times: {test_times}\n\n\n")
    print_calendar(test_times, test_events, dates)
    