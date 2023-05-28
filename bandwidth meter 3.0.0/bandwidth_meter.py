from time import time, ctime
import time
import psutil
#import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.pyplot
from tkinter import messagebox
import tkinter as tk

fig, ax = matplotlib.pyplot.subplots()

running = True

total = 0
total_download = 0
total_upload = 0

#define the function to stop the loop
def stop_loop(event):
    global running, total, total_upload, total_download
    running = False
    messagebox.showinfo("Results", f"Results:\nTotal Download: {total_download} MB\nTotal Upload: {total_upload} MB\nTotal Usage Of Internet: {total} MB")

#set the close event callback function to stop_loop
fig.canvas.callbacks.connect('close_event', stop_loop)

# charts and print datas
def chart_calculation(speed):
    global total, total_download, total_upload
    # last bytes recieved
    last_recieved = psutil.net_io_counters().bytes_recv
    last_sent = psutil.net_io_counters().bytes_sent
    last_total = last_recieved + last_sent
    while running:
        # collecting datas
        bytes_recieved = psutil.net_io_counters().bytes_recv
        bytes_sent = psutil.net_io_counters().bytes_sent
        bytes_total = last_recieved + last_sent

        # converting new datas
        new_recieved = bytes_recieved - last_recieved
        new_sent = bytes_sent - last_sent
        new_total = bytes_total - last_total

        # converting bytes to Megabytes
        mb_new_recieved = new_recieved / 1024 / 1024
        mb_new_sent = new_sent / 1024 / 1024
        mb_new_total = new_total / 1024 / 1024

        # changing last datas
        last_recieved = bytes_recieved
        last_sent = bytes_sent
        last_total = bytes_total

        # sum
        total += round(mb_new_recieved,4) + round(mb_new_sent, 4)
        #print(round(mb_new_sent, 4), round(mb_new_recieved,4), round(total, 4))
        total_download += round(mb_new_recieved, 4)
        total_upload += round(mb_new_sent, 4)

        # chart
        left = [1, 2]
        height = [mb_new_recieved, mb_new_sent]
        tick_label = ['New MB recieved', 'New MB sent']
        plt.bar(left, height, tick_label=tick_label,
                    width=0.8, color=['red', 'green'])
        plt.xlabel('name of datas')
        plt.ylabel('data amount')
        plt.title('Bandwidth meter chart')
        plt.draw()
        plt.pause(0.0001)
        plt.clf()
        time.sleep(speed)