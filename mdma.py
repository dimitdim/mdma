import smu
import pylab as plt

def linspace(initial, final, n = 100): #Creds to Brad Minch
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
lline = plt.plot(v,i,'g--')[0]
graph = plt.plot(v,i)[0]
point = plt.plot(v[0],i[0],'ob')[0]
xlabl = plt.xlabel('$V_D$',fontsize=24)
ylabl = plt.ylabel('$I_D$',fontsize=24)
vgtxt = plt.text(.5,4.5,'$V_G=$ ',fontsize=24)

run=True

while run:
    for n in range(len(v)):
        s.set_voltage(1, v[n])
        s.autorange(1)
        i[n]=1000*s.get_current(1)
        vg=s.get_voltage(2)
        vgtxt.set_text('$V_G=$ '+str(vg))
        graph.set_ydata(i)
        point.set_xdata(v[n])
        point.set_ydata(i[n])
        plt.draw()

s.set_voltage(1, 0.)
