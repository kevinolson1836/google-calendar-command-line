import os
from datetime import timedelta
from datetime import date
import datetime
from termcolor import colored, cprint
import colorama


'''
usefull chars just for copy paste 
    ═

    ║

    ╚
    ╗

    ╝
    ╔

    ╠

    ╣

    ╦

    ╩

    ╬
'''

        #           example 
        # ╔═══════╦══════════╦═════════╗
        # ║       ║          ║         ║
        # ║       ║          ║         ║
        # ╠═══════╬══════════╬═════════╣
        # ║       ║          ║         ║
        # ║       ║          ║         ║
        # ╠═══════╬══════════╬═════════╣
        # ║       ║          ║         ║
        # ║       ║          ║         ║
        # ╚═══════╩══════════╩═════════╝



class Calendar:
    def __init__(self):
        colorama.init()

        #number of sections (number of calendars to display) 
        self.num_of_calendars = 4   

        # number of cells
        self.num_of_cells = 6

        # grabbing terminal size
        term_size = os.get_terminal_size()
        self.side_buffer = 2
        self.width = int(term_size[0]-self.side_buffer)-4    # gets terminal width, -4 for a buffer of 2 spaces on each side
        self.height = int(term_size[1]) -4     # gets terminal height, -4 for a buffer of 2 spaces on each side
        self.cell_size = int(self.width/self.num_of_cells) 
        self.cell_height = 5
        
        #gives us a 2 space buffer on the left side change the number to change the buffer 
        self.left_buffer = " "*4
        

        # CREATES THE TOP BAR BASED ON SCREEN LENGTH AND CELL SIZE 
        self.top_bar = self.gen_top_bar()

        # CREATES THE CELL SIDES BASED ON SCREEN LENGTH AND CELL SIZE 
        self.cell_side = self.gen_cell_side()

        # CREATES THE CELL's DATA BASED ON SCREEN LENGTH AND CELL SIZE


        # CREATES THE CELL END BASED ON SCREEN LENGTH AND CELL SIZE
        # self.cell_end =  "    ╠═══════════════════╬═══════════════════╬═══════════════════╬═══════════════════╬═══════════════════╬═══════════════════╣"
        self.cell_end = self.gen_cell_end()

        # CREATES THE BOTTOM BAR BASED ON SCREEN LENGTH AND CELL SIZE 
        self.bottom_bar =  self.gen_bottom_bar()

        # CREATES THE DATE BASED ON SCREEN LENGTH AND CELL SIZE 
        self.cell_date =  "    ║   2/2/2023   ║   2/3/2023   ║   2/4/2023   ║   2/5/2023   ║   2/6/2023   ║   2/7/2023   ║   2/8/2023   ║   2/9/2023   ║"


    def gen_top_bar(self):
        # start of conner
        return_str = self.left_buffer + "╔"
        
        #makes the cells
        for i in range(self.num_of_cells): 
            return_str = return_str + "═" *(self.cell_size-2)
            if(i != self.num_of_cells-1):
                return_str = return_str + "╦"
        
        # end of conner
        return_str = return_str + "╗"

        return(return_str)

    def gen_cell_side(self):
        return_str = self.left_buffer + "║"

        for i in range(self.num_of_cells): 
            return_str = return_str + " " *(self.cell_size-2)
            return_str = return_str + "║"

        return(return_str)


    def gen_bottom_bar(self):
            # start of conner
            return_str = self.left_buffer + "╚"
            
            #makes the cells
            for i in range(self.num_of_cells): 
                return_str = return_str + "═" *(self.cell_size-2)
                if(i != self.num_of_cells-1):
                    return_str = return_str + "╩"
            
            # end of conner
            return_str = return_str + "╝"

            return(return_str)


    def text_to_(self, nested_text_list):
        final_string = ""
        for text_list in nested_text_list:
            end_string = self.left_buffer + "║"
            for text in text_list:
                if (len(text) > self.cell_size-2):
                        # text is to long to fit in cell, trunkate at cell size
                        # print("too long remove after debug")
                        end_string = end_string + text[:self.cell_size-2] + "║"
                else:
                    end_string = end_string + text.center(self.cell_size-2) + "║"
            final_string = final_string + end_string + "\n"

        return(final_string[:(len(final_string))-1])    #the len(fin_string)-1 part removes the last newline char



    def text_to_string(self, nested_text_list):
            final_string = ""
            for text_list in nested_text_list:
                return_str = self.left_buffer + "║"
                for text in text_list:
                    text_length = len(text)
                    total_side_spaces = self.cell_size - text_length
                    if (text_length != 0):
                        # subtract 2 from the total for the  '║' on each side
                        total_side_spaces -2

                    front_side_spaces = int(total_side_spaces/2)
                    end_side_spaces = int(total_side_spaces/2)

                    if ((text_length%2) == 0):
                        # is even, subtract 1 space from end
                        end_side_spaces = end_side_spaces -1

                    if (total_side_spaces < 0):
                        # text is to long to fit in cell, trunkate at cell size
                        print("too long remove after debug")
                        return_str = "║" + text[:self.cell_size] + "║"
                    else:
                            return_str = return_str + (" "*front_side_spaces) + text + (" "*(end_side_spaces)) +"║"
                final_string = final_string + return_str + "\n"
            return(final_string[:(len(final_string))-1])    #the len(fin_string)-1 part removes the last newline char


    def draw_section(self, text):
            '''
            draws the calendar with given text.
            Text- nested list 
            '''

            print(self.top_bar)

            #Date section
            # print(self.cell_side) 
            # print(self.cell_date)  
            # print(self.cell_end)
            
            # Calendar data cells
            for i in range(self.num_of_calendars):
                print(self.cell_side)
                print(self.text_to_(text))
                print(self.cell_side)
                if(i != self.num_of_calendars-1):
                    print(self.cell_end)
            
            print(self.bottom_bar)

    def gen_cell_end(self):
        # start of conner
        return_str = self.left_buffer + "╠"
        
        #makes the cells
        for i in range(self.num_of_cells): 
            return_str = return_str + "═" *(self.cell_size-2)
            if(i != self.num_of_cells-1):
                return_str = return_str + "╬"
        
        # end of conner
        return_str = return_str + "╣"

        return(return_str)