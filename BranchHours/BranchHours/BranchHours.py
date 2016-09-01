#Branch Hours Program
#Shows when a branch from a different time zone is open or closed
#open = 9:00:00
#close = 21:00:00 
from tkinter import *
from datetime import datetime, timedelta

#Define function to check local time of each location and 
#compare that to a set open and close time in their timezone  
def ask_if_open():
    
    #Get the current time
    now = datetime.now()
    
    #Set variable to hold NY time
    ny_time = datetime.now() 
    
    #Set variable to hold london time
    london_time = datetime.now() 
    
    #Set NY time to three hours ahead of local time
    ny_time = ny_time+timedelta(hours=3)
    
    #Set london time to eight hours ahead of local time
    london_time = london_time+timedelta(hours=8)
    
    def is_london_open():
        
        #set open and closed times
        branch_open = london_time.replace(hour=9, minute=0, second=0, microsecond=0)
        branch_close = london_time.replace(hour=21, minute=0, second=0, microsecond=0)
        
        #logical if statement to compare time to open/close time
        if london_time >= branch_open and london_time < branch_close:
            #if london time is within open/close times then make a label saying open and place it next to london label
            Label(frame1, text="Open").grid(row=0, column=1, sticky=W)
        else:
            #otherwise make the label say closed
            Label(frame1, text="Closed").grid(row=0, column=1, sticky=W)

            #repeat for NY time zone
    def is_ny_open():
        branch_open = ny_time.replace(hour=9, minute=0, second=0, microsecond=0)
        branch_close = ny_time.replace(hour=21, minute=0, second=0, microsecond=0)
        if ny_time >= branch_open and ny_time < branch_close:
            Label(frame1, text="Open").grid(row=1, column=1, sticky=W)
        else:
            Label(frame1, text="Closed").grid(row=1, column=1, sticky=W)
    
    #call functions for both time zones        
    is_ny_open()
    is_london_open()

#tkinter window creation
win = Tk()
frame1 = Frame(win)
frame1.pack()
Label(frame1, text="London").grid(row=0, column=0, sticky=W)
Label(frame1, text="New York").grid(row=1, column=0, sticky=W)

#create button and link get_hours() function to it
b = Button(frame1, text = 'Who is open?', command=ask_if_open)
b.grid(row=3, column=0, columnspan=2)  

#loop through the window waiting for button press
win.mainloop()