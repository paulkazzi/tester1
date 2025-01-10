# https://www.youtube.com/watch?v=b0wk12EwnPQ

import netmiko
import json
import logging

# Global Logging continuous appends
# logging.basicConfig(filename='netmiko_global.log', level=logging.DEBUG)
# logger = logging.getLogger("netmiko")

connection = netmiko.ConnectHandler(ip='43.66.207.1', device_type= 'cisco_ios',
                                     username='cisco', password= 'password123',
                                     session_log= 'netmiko_session.log',
                                     secret='cisco')

print("Now lets do a show clock and check time- ")
print(connection.send_command("show clock"))
print(connection.find_prompt())
      

print("Now lets do an enable login")
# enable method below ties in with "secret" in ConnectHander
connection.enable()
#mycommand = "enable\n"
#reply = connection.send_command(mycommand)
#reply = connection.send_command("enable\n")

print(connection.find_prompt())
connection.disconnect()