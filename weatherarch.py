import os

def cls():
	os.system("clear")

def Dependencies():

	print("Checking for missing dependencies.")
	os.system("pacman -Qi curl > log.txt")

	with open('log.txt', 'r') as file:
		dep = file.read().replace('\n', '')

	if "was not found" in dep:
		os.system("sudo pacman -S curl")
	else:
		cls()
		print("All dependencies are present.")
		cls()
		os.system("rm -rf log.txt")

def CurlWeather():

	os.system("curl wttr.in")


Dependencies()
CurlWeather()

### Report any issues on Github.
