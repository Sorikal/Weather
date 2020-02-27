import os

def cls():
    os.system("clear")

def Dependencies():

    os.system("dpkg -l | grep -E '^ii' | grep curl > log.txt")
    with open('log.txt', 'r') as file:
        cmdlog = file.read().replace('\n', '')

    os.system("rm -rf log.txt")

    if cmdlog == "":
        os.system("sudo apt install curl")
        cls()
    else:
        cls()

def CurlWeather():
    os.system("curl wttr.in")



    
    