# Citlaly Garcia 
# CSE 5408 Spring 2021 
# Lab 4: GitHub - Advanced 
# Part c: Time Conversion 
# Group: APP-itizer Enthusiasts 

from datetime import datetime 
import pytz

tz_CA = pytz.timezone('America/Los_Angeles')
datetime_CA = datetime.now(tz_CA)
t = datetime_CA.strftime("%H:%M:%S")
print("The current time in 24-Hour/Military time is ")

print(t) 
