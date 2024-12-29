import time
import pywhatkit as kit
a="Happy bithday"
phone_number = "+919433353180" 
target_hour=23
target_minute=59
target_second=59
present_hour=int(time.strftime("%H"))
present_minute=int(time.strftime("%M"))
present_second=int(time.strftime("%S"))
current_seconds = present_hour * 3600 + present_minute * 60 + present_second
target_seconds = target_hour * 3600 + target_minute * 60 + target_second
time_gap = target_seconds - current_seconds
if time_gap < 0:
    time_gap += 24 * 3600

try:
    
    kit.sendwhatmsg(phone_number, a, target_hour, target_minute, 10)
    print("message sceduled succesfully")
except:
    print("Error")    