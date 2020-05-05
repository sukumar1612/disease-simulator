# -*- coding: utf-8 -*-
"""
Created on Wed May  6 00:00:01 2020

@author: Sukumar Ganesan
"""
"""disease simulator"""

import secrets # better randomisation algorithm (used for encryption)
import matplotlib.pyplot as plt
#initial values or conditions 
Range=100 #this is space so the space allocated is range*range units
healthy=400
infected=3
no_of_hospitals=200
no_of_iterations=1000
#hospitals
h1=[secrets.randbelow(Range) for i in range(0,no_of_hospitals)]
h2=[secrets.randbelow(Range) for i in range(0,no_of_hospitals)]
h=[(h1[i],h2[i]) for i in range(0,no_of_hospitals)]
"""print(h1,'\n',h2)
for i in range(0,101): #test to check how good the algorithm is 
    a[i]=0
for i in range(0,100000):
    a[secrets.randbelow(100)]=a[secrets.randbelow(100)]+1
for i in range(0,101):
    sum1=sum1+a[i]
for i in range(0,101):
    print("for ",i," probablity is ",float(a[i]/sum1)*100)
"""

hea=[]
inf=[]

for i in range(0,no_of_iterations):
    hea.append(healthy)
    inf.append(infected)
    l1=[(secrets.randbelow(Range),secrets.randbelow(Range)) for i in range(0,healthy)]
    x=[l1[i][0] for i in range(0,healthy)]
    y=[l1[i][1] for i in range(0,healthy)]
    
    l2=[(secrets.randbelow(Range),secrets.randbelow(Range)) for i in range(0,infected)]
    x1=[l2[i][0] for i in range(0,infected)]
    y1=[l2[i][1] for i in range(0,infected)]
    """
    fig, ax = plt.subplots()
    #healthy 
    ax.scatter(x, y, color= "green",s=30) 
    #hospital
    ax.scatter(h1, h2, color= "blue",s=30)
    
    ax.scatter(x1, y1, color= "red",s=30)
    
    ax.legend()
    
    plt.legend() 
    
    plt.show() 
    """
    for i in l1:
        for j in l2:
            if(i[0]==j[0]):
                if(i[1]==j[1]-1):
                    healthy=healthy-1
                    infected=infected+1
                elif(i[1]==j[1]+1):
                    healthy=healthy-1
                    infected=infected+1
            elif(i[1]==j[1]):
                if(i[0]==j[0]-1):
                    healthy=healthy-1
                    infected=infected+1
                elif(i[0]==j[0]+1):
                    healthy=healthy-1
                    infected=infected+1
    for i in l2:
        for j in h:
            if(i[0]==j[0]):
                if(i[1]==j[1]-1):
                    healthy=healthy+1
                    infected=infected-1
                elif(i[1]==j[1]+1):
                    healthy=healthy+1
                    infected=infected-1
            elif(i[1]==j[1]):
                if(i[0]==j[0]-1):
                    healthy=healthy+1
                    infected=infected-1
                elif(i[0]==j[0]+1):
                    healthy=healthy+1
                    infected=infected-1

xaxis=[i for i in range(0,no_of_iterations)]
plt.plot(xaxis,hea,color="green")
plt.plot(xaxis,inf,color="red")
