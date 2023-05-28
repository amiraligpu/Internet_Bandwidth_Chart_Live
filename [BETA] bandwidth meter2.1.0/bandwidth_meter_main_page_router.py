from netmiko import ConnectHandler
from tkinter import *
from netmiko import ConnectHandler
from netmiko.exceptions import NetMikoTimeoutException
from tkinter import messagebox
def router_workout():
    messagebox.showinfo("continue", "Continue in terminal.")
    try:
        device = ConnectHandler(device_type=str(input("enter device_type: ")),
                                ip= str(input("enter ip address: ")),
                                username=str(input("enter username: ")),
                                password=str(input("enter password: ")))
        output = device.send_command("write memory")
        print(output)
        device.disconnect()
    except NetMikoTimeoutException:
        print(f"Error")