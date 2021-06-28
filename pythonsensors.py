import sys
import os
import time
import keyboard

arg = sys.argv

def getAll():
    os.system('wmctrl -r \':ACTIVE:\' -b toggle,fullscreen')
    while True:
        if not keyboard.is_pressed('q'):
            os.system('echo \'PRESS Q TO EXIT\'')
            os.system('clear')
            os.system('sensors')
            os.system('echo \'PRESS Q TO EXIT\'')
            time.sleep(0.1)
            continue
        else:
            os.system('wmctrl -r \':ACTIVE:\' -b toggle,fullscreen')
            exit()

def getSensors():
    global arg
    n = 1
    string = 'sensors | grep \'' 
    for i in range(len(arg) - 1):
        indstring = str(arg[n]) + '\|'
        string = string + indstring
        n += 1

    string = string[:-2]
    string = string + '\''
        


    os.system('wmctrl -r \':ACTIVE:\' -b toggle,fullscreen')
    while True:
        if not keyboard.is_pressed('q'):
            os.system('echo \'PRESS Q TO EXIT\'')
            os.system('clear')
            os.system(string)
            os.system('echo \'PRESS Q TO EXIT\'')
            time.sleep(0.1)
            continue
        else:
            os.system('wmctrl -r \':ACTIVE:\' -b toggle,fullscreen')
            exit()


if len(arg) == 1:
    getAll()
else:
    getSensors()










