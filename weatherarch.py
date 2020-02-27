import os
import time

### Checking for dependencies

print("Checking for missing dependencies.")
os.system("pacman -Qi curl > log.txt")

with open('log.txt', 'r') as file:
	dep = file.read().replace('\n', '')

if "was not found" in dep:
	os.system("sudo pacman -S curl")
else:
	os.system("clear")
	print("All dependencies are present.")
	os.system("clear")

os.system("rm -rf log.txt")

### Curling weather

os.system("curl wttr.in")


### Report any issues on Github.
