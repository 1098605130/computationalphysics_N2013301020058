# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 16:25:12 2016

@author: asus
"""

v1=[]       #velocity
v2=[]       #velocity
t=[]       #time
a=10       #assign a value to a
b=1        #assign a value to b
det_t=0.05     #time step
v01=float(input('the initial volecity 1 is '))
v02=float(input('the initial volecity 2 is '))
v1.append(v01) #assign a value to first item of v1[]
v2.append(v02) #assign a value to first item of v2[]
t.append(0) #assign a value to first item of t[]
end_time=15  #total time
f=open('problem1.3.txt','w')
for i in range(int(end_time/det_t)):
    v1mp=v1[i]+(a-b*v1[i])*det_t  #Euler method
    v2mp=v2[i]+(a-b*v2[i])*det_t  #Euler method
    v1.append(v1mp)  #add new value of v to v1[]
    v2.append(v2mp)  #add new value of v to v2[]
    t.append(det_t*(i+1)) #add new value of t to t[]
    print >>f,t[-1],v1[-1],v2[-1] #print the value of v and t on each stap
f.close()
ymax=max(max(v1),max(v2))
import matplotlib.pyplot as plt
plt.figure(figsize=(8,6))  #set the size of corresponding figure
plt.plot(t,v1,label="v01",color="black",linewidth=1) #plot the figure and set label and color and linewidth of the figure
plt.plot(t,v2,label="v02",color="red",linewidth=1) #plot the figure and set label and color and linewidth of the figure
plt.legend(loc = 'upper right')
plt.xlabel("t/s")   #set the label of x axis
plt.ylabel("v/(m/s)")  #set the label of y axis
plt.title("a=10,b=1,v=0") #set title
plt.ylim(0,ymax*1.2) #set the range of y axis
plt.savefig('problem1.3.png')
plt.show()  #activate