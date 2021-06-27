# sensors
Instructions for installation:
ONLY TESTED ON POP OS, will probably work on other distributions although installing packages may be different
1) make sure 'lm-sensors' is installed ('sudo apt-get install lm-sensors', 'sensors-detect', hit enter to go with default options for everything)
2) make sure python module 'keyboard' is installed (sudo pip install keyboard)
3) make sure 'wmctrl' is installed ('sudo apt-get install wmctrl')
4) download and extract the .zip
5) in the terminal cd to sensors-main
6) run 'sudo chmod +x setup.sh'
7) run './setup.sh'

Use:
from your home directory run './sensors.sh'
