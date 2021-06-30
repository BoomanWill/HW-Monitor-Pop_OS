import os
import time
import subprocess
import keyboard

def getinfo():
    cpuhigh = 0
    gpuhigh = 0
    nvmehigh = 0
    vcorehigh = 0
    vbathigh = 0
    systinhigh = 0
    cputinhigh = 0
    auxtin0high = 0
    auxtin2high = 0
    smbusmasterhigh = 0
    gpumemhigh = 0

    while True:
        if not keyboard.is_pressed('q'):
            cputemp = subprocess.getoutput('sensors | grep Tccd1')
            cputemp = float(cputemp[-8:-4])
            if cputemp > cpuhigh:
                cpuhigh = cputemp

            gputemp = subprocess.getoutput('nvidia-smi | grep %')
            gputemp = float(gputemp[8:10])
            if gputemp > gpuhigh:
                gpuhigh = gputemp

            gpumem = subprocess.getoutput('nvidia-smi | grep %')
            gpumem = float(gpumem[36:40])
            if gpumem > gpumemhigh:
                gpumemhigh = gpumem

            nvmetemp = subprocess.getoutput('sensors | grep Composite')
            nvmetemp = float(nvmetemp[15:19])
            if nvmetemp > nvmehigh:
                nvmehigh = nvmetemp

            vcore = subprocess.getoutput('sensors | grep in0')
            vcore = float(vcore[25:29])
            if vcore > vcorehigh:
                vcorehigh = vcore

            vbat = subprocess.getoutput('sensors | grep in8')
            vbat = float(vbat[25:29])
            if vbat > vbathigh:
                vbathigh = vbat

            systin = subprocess.getoutput('sensors | grep SYSTIN')
            systin = float(systin[25:29])
            if systin > systinhigh:
                systinhigh = systin

            cputin = subprocess.getoutput('sensors | grep CPUTIN')
            cputin = float(cputin[25:29])
            if cputin > cputinhigh:
                cputinhigh = cputin

            auxtin0 = subprocess.getoutput('sensors | grep AUXTIN0')
            auxtin0 = float(auxtin0[25:29])
            if auxtin0 > auxtin0high:
                auxtin0high = auxtin0

            auxtin2 = subprocess.getoutput('sensors | grep AUXTIN2')
            auxtin2 = float(auxtin2[25:29])
            if auxtin2 > auxtin2high:
                auxtin2high = auxtin2

            smbusmaster = subprocess.getoutput('sensors | grep SMBUSMASTER')
            smbusmaster = float(smbusmaster[25:29])
            if smbusmaster > smbusmasterhigh:
                smbusmasterhigh = smbusmaster
        
            os.system('clear')
            print('GPU temp:    {}C HIGH:   {}C'.format(gputemp, gpuhigh))
            print('GPU mem:     {}MiB High: {}MiB'.format(gpumem, gpumemhigh))
            print('CPU temp:    {}C HIGH:   {}C'.format(cputemp, cpuhigh))
            print('NVME temp:   {}C HIGH:   {}C'.format(nvmetemp, nvmehigh))
            print('Vcore:       {}V HIGH:   {}V'.format(vcore, vcorehigh))
            print('Vbat:        {}V HIGH:   {}V'.format(vbat, vbathigh))
            print('SYSTIN:      {}C HIGH:   {}C'.format(systin, systinhigh))
            print('CPUTIN:      {}C HIGH:   {}C'.format(cputin, cputinhigh))
            print('AUXTIN0:     {}C HIGH:   {}C'.format(auxtin0, auxtin0high))
            print('AUXTIN2:     {}C HIGH:   {}C'.format(auxtin2,auxtin2high))
            print('SMBUSMASTER: {}C HIGH:   {}C'.format(smbusmaster, smbusmasterhigh))
            print('Press Q to exit')
            time.sleep(0.5)
        else:
            os.system('clear')
            exit()
        


getinfo()
