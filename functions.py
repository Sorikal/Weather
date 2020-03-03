import os


def Dependencies():
    os.system("apt > pm.txt")
    with open('pm.txt', 'r') as file:
        pm = file.read().replace('\n', '')
    if "command not found" in pm:
        os.system("sudo apt install curl -y")
    else:
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
    os.system("rm -rf pm.txt && rm -rf __pycache__")
        

def CurlWeather():
    os.system("curl wttr.in")
