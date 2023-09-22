import tkinter as tk
from time import strftime

#create a tkinter window
root = tk.Tk()
root.title("DIGITAL CLOCK")


#Function to update the time
def time():
  string =strftime('%I:%M:%S %p')
  label.config(text=string)
  label.after(1000,time)

#Create a label widget to display time
label=tk.Label(root,font=('arial',40,'bold'),background='white',foreground='black')
label.pack(anchor='center')

#call the time function to update the time
time()

#run the tkinter main loop
root.mainloop() 
