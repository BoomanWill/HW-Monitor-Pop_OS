# sensors

I am aware this is already a feature of lm-sensors, I just thought it would be fun to code my own.

**Instructions for installation:**

ONLY TESTED ON POP OS, will probably work on other distributions although installing packages may be different
1) make sure lm-sensors is installed (`sudo apt-get install lm-sensors`, `sensors-detect`, hit enter to go with default options for everything)
2) download and extract the .zip
3) in the terminal cd to sensors-main
4) run `sudo chmod +x setup.sh`
5) run `./setup.sh`
6) If you want to just run one command: 
6a) create a file called .bash_aliases in your home directory
6b) add the following lines to it:
```#!/bin/bash
ALIASNAME(){
sudo python3 pythonsensors.py $@
}
```
where ALIASNAME is what you want to call the command

**Use:**

without step 6: from your home directory run `sudo python3 pythonsensors.py "arg 1" "arg 2" etc.`
with step 6: run `ALIASNAME "arg 1" "arg 2" etc.`
args can be:
Tctl, Tdie, Tccd1 - variations on CPU temperature
in0-14 - voltages
fan1-6 - fan speeds
and others found if you just type sensors.



*This software is distributed free of charge by a not-for-profit entity. You use this software at your own risk and I will accept no liability to any damage to the computer or any financial loss incurred by software malfunction.*


