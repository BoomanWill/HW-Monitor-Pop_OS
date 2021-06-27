import keyboard
import time
import os

os.system('wmctrl -r \':ACTIVE:\' -b toggle,fullscreen') #toggles fullscreen for the terminal window
while True:
    if not keyboard.is_pressed('q'):  #checks that q is not pressed, then repeats sensors every 0.1s
        os.system('echo \'PRESS Q TO EXIT\'')
        os.system('clear')
        os.system('sensors')
        os.system('echo \'PRESS Q TO EXIT\'')
        time.sleep(0.1)
        continue
    else:
        os.system('wmctrl -r \':ACTIVE:\' -b toggle,fullscreen') #untoggles fullscreen when q is pressed and exits the program
        exit()









