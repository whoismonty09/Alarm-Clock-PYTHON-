import time
import datetime
import winsound

print("Alarm Clock developed by Monty")
alarm_time = input("Enter alarm time (HH:MM:SS): ")

print("Alarm is set for", alarm_time)

while True:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    if current_time == alarm_time:
        print("Wake up")
        winsound.Beep(1000, 2000)
        break
    time.sleep(1)
