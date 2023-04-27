# Import Module
from tkinter import *

root = Tk()


root.title('Chat Bot')

# Add Geometry
root.geometry("500x300")

# Keep track of the button state on/off
# global is_on
is_on = True

print("Im on driving 1")

# Create Label
my_label = Label(root,
                 text="Driving Mode Turned On!",
                 fg="green",
                 font=("Helvetica", 32))

my_label.pack(pady=20)


# Define our switch function
def switch():
    global is_on


    # Determine is on or off
    if is_on:
        on_button.config(image=off)
        my_label.config(text="Driving Mode Off!",
                        fg="grey")
        is_on = False
        print("Im not driving")
    else:

        on_button.config(image=on)
        my_label.config(text="Driving Mode Turned On!", fg="green")
        is_on = True
        print("Im on driving")
        from main import wa_bot


# Define Our Images
on = PhotoImage(file="on.png")
off = PhotoImage(file="off.png")

# Create A Button
on_button = Button(root, image=on, bd=0,
                   command=switch)
on_button.pack(pady=50)

# Execute Tkinter
root.mainloop()
