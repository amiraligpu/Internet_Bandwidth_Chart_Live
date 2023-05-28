import tkinter as tk
from tkinter import *
import bandwidth_meter
import bandwidth_meter_main_page_router
from tkinter import messagebox
from PIL import Image, ImageTk

speed = 1
def live_chart():
    bandwidth_meter.chart_calculation(speed)

def intro():
    root = Tk()  # create root window
    root.title("Bandwidth Meter")
    root.config(bg="skyblue")

    #Set the minimum and maximum size of the window
    root.minsize(300, 300)
    root.maxsize(300, 300)

    # Create Frame widget
    left_frame = Frame(root, width=200, height=400)
    left_frame.grid(row=0, column=0, padx=10, pady=5)
    left_frame.propagate(0) #Disable propagaion of the size

    # Create frame within left_frame
    tool_bar = Frame(left_frame, width=180, height=185, bg="purple")
    tool_bar.grid(row=2, column=0, padx=5, pady=5)
    tool_bar.propagate(0) #Disable propagaion of the size

    # Create label above the tool_bar
    Label(left_frame, text="Bandwidth Meter").grid(row=1, column=0, padx=5, pady=5)
    left_frame.pack(expand=True)

    #Start Tracking Button
    start_chart_button = tk.Button(tool_bar, text = "Start Tracking With Chart",command = live_chart)
    start_chart_button.grid(row=1, column=1, padx=10, pady=10)

    start_chart_button = tk.Button(tool_bar, text = "Start Router Tracking",command = bandwidth_meter_main_page_router.router_workout)
    start_chart_button.grid(row=2, column=1, padx=10, pady=10)

    #options button
    close_button = tk.Button(tool_bar, text = "Quit", command=root.destroy)
    close_button.grid(row=3, column=1, padx=10, pady=10)

    root.mainloop()

intro()