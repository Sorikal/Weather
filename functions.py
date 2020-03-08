import os, os.path


def Dependencies():
    dep = os.path.isfile("dep.txt")
    if dep is False:
        os.system("sudo apt install curl -y")
        os.system("touch dep.txt")
    os.system("clear")

def CurlWeather():
    os.system("curl wttr.in")
