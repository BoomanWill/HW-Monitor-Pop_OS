import keyboard
import time
import os

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









