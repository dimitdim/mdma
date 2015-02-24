import smu
import pylab as plt

def linspace(initial, final, n = 100): #Creds to Brad Minch
    if n>=2:
        increment = (float(final) - float(initial))/(n - 1)
        return [float(initial) + i*increment for i in range(n)]
    else:
        return []

vt=2.1
v = linspace(0, 5, 101)
i = linspace(0, 5, 101)

plt.ion()
rline = plt.plot(v,i,'g--')[0]
graph = plt.plot(v,i)[0]
point = plt.plot(v[0],i[0],'ob')[0]
xlabl = plt.xlabel('$V_D$',fontsize=24)
ylabl = plt.ylabel('$I_D$',fontsize=24)
vgtxt = plt.text(.5,4.5,'$V_G=$ ',fontsize=24)
title = plt.title('IV Charecteristic of BS170 nMOSFET',fontsize=24)

s = smu.smu() #Creds to Brad Minch
s.set_current(2, 0)

run=True
while run:
    for n in range(len(v)):
        try:
            s.set_voltage(1, v[n])
            s.autorange(1)
            i[n]=1000*s.get_current(1)
            vg=s.get_voltage(2)
        except:
            print "Device disconnected"
            run = False
            break
        off=vg<vt
        vgtxt.set_text('$V_G=$ '+str(vg)+' > '*(not off)+' < '*off+str(vt))
        vgtxt.set_color('r'*off+'g'*(not off))
        graph.set_ydata(i)
        point.set_xdata(v[n])
        point.set_ydata(i[n])
        plt.draw()
plt.text(1,2.5,'DEVICE DISCONNECTED',fontsize=24,color='r')
plt.draw()
from time import sleep
sleep(3)
#s.set_voltage(1, 0.)
