# HWMonitor for Ubuntu


## Instructions for installation: ##

ONLY TESTED ON POP_OS, will probably work on other distributions although installing packages may be different.
1) make sure lm-sensors is installed (`sudo apt-get install lm-sensors`, `sensors-detect`, hit enter to go with default options for everything)
2) download and extract the .zip
3) in the terminal cd to HW-Monitor-Ubuntu-main
4) run `sudo chmod +x setup.sh`
5) run `./setup.sh`
6) If you want to just run one command: 
6a) create a file called .bash_aliases in your home directory
6b) add the following lines to it:
```
#!/bin/bash
ALIASNAME(){
sudo python3 hwmonitor.py
}
```
where ALIASNAME is what you want to call the command

**Use:**

without step 6: from your home directory run `sudo python3 hwmonitor.py`

with step 6: run `ALIASNAME`

## Description: ##
HW-Monitor-Ubuntu is a hardware monitor designed for Ubuntu.  It shows, CPU temp, GPU temp, NVME temp, Vcore, Vbat, SYSTIN, CPUTIN, AUXTIN0, AUXTIN2 and SMSUBMASTER, along with the high values.

*This software is distributed free of charge by a not-for-profit entity. You use this software at your own risk and I will accept no liability to any damage to the computer or any financial loss incurred by software malfunction.*


