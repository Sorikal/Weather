import os

#### This program will parse the weather in your area and dispay it to you
### This tool is using wttr.in for weather

### Check for dependencies

os.system("clear")

os.system("dpkg -l | grep -E '^ii' | grep curl > log.txt")
with open('log.txt', 'r') as file:
    cmdlog = file.read().replace('\n', '')

os.system("rm -rf log.txt")

if cmdlog == "":
    print("We have to install some depenencies...")
    os.system("sudo apt install curl")
    os.system("clear")
else:
    os.system("clear")

os.system("curl wttr.in")



    
    