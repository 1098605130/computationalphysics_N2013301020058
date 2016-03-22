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
import matplotlib.pyplot as plt
plt.plot(t,v,'-')
plt.legend('v')
plt.title('problem 1.1',fontsize=20)
plt.xlabel('t/s')
plt.ylabel('v/(m/s)')
plt.savefig('chapter1.png')
plt.show()