import smu
import pylab as plt
from time import time

def linspace(initial, final, n = 100):
    if n>=2:
        increment = (float(final) - float(initial))/(n - 1)
        return [float(initial) + i*increment for i in range(n)]
    else:
        return []

s = smu.smu()
s.set_current(2, 0)
v = linspace(0, 5, 101)
i = linspace(0, 5, 101)

plt.ion()
graph = plt.plot(v,i)[0]

while True:
    for n in range(len(v)):
        s.set_voltage(1, v[n])
        s.autorange(1)
        i[n]=1000*s.get_current(1)
        print "Vg: "+str(s.get_voltage(2))+'; Vd: '+str(v[n])+'; Id:  '+str(i[n])
        graph.set_ydata(i)
        plt.draw()

s.set_voltage(1, 0.)
