from tkinter import Label, Tk 
import time

app_window = Tk() 
app_window.title("Digital Clock") 
app_window.geometry("420x150") 
app_window.resizable(1, 1)

text_font = ("Boulder", 68, 'bold')
background = "#f2e750"
foreground = "#363529"
border_width = 25  # Here is the corrected line

app_window.configure(bg=background)

# Create the Label widget
digital_clock = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
digital_clock.grid(row=0, column=1)

# Function to run the digital clock
def digital_time():
    time_live = time.strftime("%H:%M:%S")
    digital_clock.config(text=time_live)
    digital_clock.after(200, digital_time)

digital_time()

app_window.mainloop()
