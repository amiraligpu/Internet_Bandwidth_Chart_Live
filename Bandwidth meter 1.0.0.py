from time import time, ctime
import time
import psutil
import pandas as pd
from matplotlib import pyplot as plt

#last bytes recieved
last_recieved = psutil.net_io_counters().bytes_recv
last_sent = psutil.net_io_counters().bytes_sent
last_total = last_recieved + last_sent

#charts and print datas
while True:
      #collecting datas
  bytes_recieved = psutil.net_io_counters().bytes_recv
  bytes_sent = psutil.net_io_counters().bytes_sent
  bytes_total = last_recieved + last_sent

  #converting new datas
  new_recieved = bytes_recieved - last_recieved
  new_sent = bytes_sent - last_sent
  new_total = bytes_total - last_total

  #converting bytes to Megabytes
  mb_new_recieved = new_recieved / 1024 / 1024
  mb_new_sent = new_sent / 1024/ 1024
  mb_new_total = new_total / 1024 / 1024
  
  #changing last datas
  last_recieved = bytes_recieved
  last_sent = bytes_sent
  last_total = bytes_total
  
  #chart
  left = [1,2]
  height = [mb_new_recieved,mb_new_sent]
  tick_label = ['New MB recieved', 'New MB sent']
  plt.bar(left, height, tick_label = tick_label,
        width = 0.8, color = ['red', 'green'])
  plt.xlabel('name of datas')
  plt.ylabel('data amount')
  plt.title('Bandwidth meter chart')
  plt.draw()
  plt.pause(0.0001)
  plt.clf()
  time.sleep(1)