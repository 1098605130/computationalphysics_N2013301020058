# -*- coding: utf-8 -*-
v=[]
t=[]
g=9.8
dt=float(input('time step='))
v.append(0)
t.append(0)
end_time=10
for i in range(int(end_time/dt)):
    vi=v[i]-g*dt
    v.append(vi)
    t.append(dt*(i+1))
    print t[-1],v[-1]