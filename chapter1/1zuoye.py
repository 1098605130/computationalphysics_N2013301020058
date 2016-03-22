# -*- coding: utf-8 -*-
v=[]
t=[]
g=9.8
dt=float(input('time step='))
v.append(0)
t.append(0)
end_time=10
f=open('chapter1.txt','w')
for i in range(int(end_time/dt)):
    vi=v[i]-g*dt
    v.append(vi)
    t.append(dt*(i+1))
    print t[-1],v[-1]
    print >> f,t[-1],v[-1]
f.close()
#plot
from pylab import *
plot(t,v,'-')
legend('v')
title('problem 1.1',fontsize=20)
xlabel('t/s')
ylabel('v/(m/s)')
savefig('chapter1.png')
show()