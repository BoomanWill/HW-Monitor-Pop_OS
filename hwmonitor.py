import os
import time
import subprocess
import keyboard
import matplotlib.pyplot as plt
import psutil
import platform


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
    memhigh = 0
    cpuusehigh = 0
    cpufreqhigh = 0
    cpugraph = []
    cpuusegraph = []
    gpugraph = []
    nvmegraph = []
    smbusgraph = []
    timelist = []
    memgraph = []
    timenum = 0 
    uname = platform.uname()

    system = subprocess.getoutput('neofetch | grep x86')
    system = system[-25:-12]

    cpucount = psutil.cpu_count()
    totram = round(psutil.virtual_memory().total / 1000000000, 3)
    architecture = uname.processor

    while True:
        if not keyboard.is_pressed('q'):
            timenum += 0.01
            timelist.append(timenum)

            cpufreq = psutil.cpu_freq()[0]
            cpufreq = round(cpufreq / 1000, 1)
            if cpufreq > cpufreqhigh:
                cpufreqhigh = cpufreq

            cpuusage = psutil.cpu_percent(0.1)
            if cpuusage > cpuusehigh:
                cpuusehigh = cpuusage
            cpuusegraph.append(cpuusage)

            memusage = psutil.virtual_memory()[3]
            memusage = round(memusage / 1000000000, 2)
            if memusage > memhigh:
                memhigh = memusage
            memgraph.append(psutil.virtual_memory()[2])

            cputemp = subprocess.getoutput('sensors | grep Tccd1')
            cputemp = float(cputemp[-8:-4])
            if cputemp > cpuhigh:
                cpuhigh = cputemp
            cpugraph.append(cputemp)

            gputemp = subprocess.getoutput('nvidia-smi | grep %')
            gputemp = float(gputemp[8:10])
            if gputemp > gpuhigh:
                gpuhigh = gputemp
            gpugraph.append(gputemp)

            gpumem = subprocess.getoutput('nvidia-smi | grep %')
            gpumem = float(gpumem[36:40])
            if gpumem > gpumemhigh:
                gpumemhigh = gpumem

            nvmetemp = subprocess.getoutput('sensors | grep Composite')
            nvmetemp = float(nvmetemp[15:19])
            if nvmetemp > nvmehigh:
                nvmehigh = nvmetemp
            nvmegraph.append(nvmetemp)

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
            smbusgraph.append(smbusmaster)
        
            os.system('clear')
            print('-------------------------------------------------------------------------------')
            print('GPU temp:    {}C | HIGH:   {}C           GPU mem:     {}MB | High:  {}MB'.format(gputemp, gpuhigh, gpumem, gpumemhigh))
            print('-------------------------------------------------------------------------------')
            print('CPU temp:    {}C | HIGH:   {}C           CPU usage:   {}% | HIGH:   {}%'.format(cputemp, cpuhigh, cpuusage, cpuusehigh))
            print('CPU freq     {}Ghz | High: {}GHz           Vcore:       {}V | HIGH:   {}V'.format(cpufreq, cpufreqhigh, vcore, vcorehigh))
            print('-------------------------------------------------------------------------------')
            print('Mem used     {}GB | High:  {}GB          NVME temp:   {}C | HIGH:   {}C'.format(memusage, memhigh, nvmetemp, nvmehigh))
            print('-------------------------------------------------------------------------------')
            print('Vbat:        {}V | HIGH:   {}V'.format(vbat, vbathigh))
            print('-------------------------------------------------------------------------------')
            print('SYSTIN:      {}C | HIGH:   {}C           CPUTIN:      {}C | HIGH:   {}C'.format(systin, systinhigh, cputin, cputinhigh))
            print('-------------------------------------------------------------------------------')
            print('AUXTIN0:     {}C | HIGH:   {}C           AUXTIN2:     {}C | HIGH:   {}C'.format(auxtin0, auxtin0high, auxtin2, auxtin2high))
            print('-------------------------------------------------------------------------------')
            print('SMBUSMASTER: {}C | HIGH:   {}C'.format(smbusmaster, smbusmasterhigh))
            print('-------------------------------------------------------------------------------')
            print('='*30, 'System Info', '='*30)
            print('CPU Count: {}    Total RAM:   {}GB'.format(cpucount, totram))
            print('System:  {}   Architecture:   {}'.format(system, architecture))
            print('Press Q to exit')
            time.sleep(0.01)
        else:
            print('Generating graph...')
            time.sleep(1)
            plt.plot(timelist, cpugraph, label='CPU')
            plt.plot(timelist, gpugraph, label='GPU')
            plt.plot(timelist, nvmegraph, label='NVME')
            plt.plot(timelist, smbusgraph, label='SMBUSMASTER')
            plt.plot(timelist, cpuusegraph, label='CPU Usage')
            plt.plot(timelist, memgraph, label='Memory Usage %')
            plt.ylabel('Temp(C) / Usage %')
            plt.axis([0, timelist[-1], 0, 100])
            plt.legend()
            plt.show()
            os.system('clear')
            exit()
        


getinfo()
