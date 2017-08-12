import subprocess as s  
import os
from threading import Timer

def battery_check():

	with open ('/sys/class/power_supply/BAT0/charge_now', 'r') as content_file:
		battery_level = int(content_file.read())

	with open ('/sys/class/power_supply/BAT0/charge_full', 'r') as content_file2:
		full_battery = int(content_file2.read())

	with open ('/sys/class/power_supply/BAT0/status', 'r') as content_file3:
		state = int(content_file3.read())

	battery_percentage = int((battery_level/full_battery)*100)

	img = os.path.abspath('battery2.png')

	if(battery_percentage < 20):
		if state == "discharging":
			s.Popen(["notify-send", "-i", img, "BATTERY ALERT!!!", "Connect Charger"])

	elif(battery_percentage >90):
		if state == "charging":
			s.Popen(["notify-send", "-i", img, "BATTERY ALERT!!!", "Disconnect Charger"])
			

		timer = Timer(600, battery_check)
		timer.start()

if __name__ == "__main__" :
	battery_check()

