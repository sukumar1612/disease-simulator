# -*- coding: utf-8 -*-
"""
Created on Wed May  6 00:00:01 2020

@author: Sukumar Ganesan
"""
"""disease simulator"""

import secrets # better randomisation algorithm (used for encryption)
import matplotlib.pyplot as plt
#initial values or conditions 
Range=10 #this is the space allocated to the simulation so range=10 means that a 10*10 grid is the space allocated for the simulation
healthy=30 #this is the number of healthy patients in the beginning of the simulation
infected=3# this is the number of infected patients in the beginning of the simulation
no_of_hospitals=15# this is the number of hospitals patients in the beginning of the simulation
no_of_iterations=100# this is the number of iterations for which the simulation will run. It could be interpreted as the time allocated for the simulation

#this section of code randomly decides the position of the hospitals 
h1=[secrets.randbelow(Range) for i in range(0,no_of_hospitals)]
h2=[secrets.randbelow(Range) for i in range(0,no_of_hospitals)]
h=[(h1[i],h2[i]) for i in range(0,no_of_hospitals)]

"""
#this section is not directlty useful for the simulation
print(h1,'\n',h2)
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
print("range:",Range)
print("healthy:",healthy)
print("infected:",infected)
print("no of hospitals :",no_of_hospitals)
print("no of iterations :",no_of_iterations)
print("x-axis is no of iterations\ny-axis is number of people")


for i in range(0,no_of_iterations):
    hea.append(healthy)
    inf.append(infected)
    #this section of code moves the healthy and infected people radomly
    l1=[(secrets.randbelow(Range),secrets.randbelow(Range)) for i in range(0,healthy)]
    x=[l1[i][0] for i in range(0,healthy)]
    y=[l1[i][1] for i in range(0,healthy)]
    
    l2=[(secrets.randbelow(Range),secrets.randbelow(Range)) for i in range(0,infected)]
    x1=[l2[i][0] for i in range(0,infected)]
    y1=[l2[i][1] for i in range(0,infected)]
    """
    #this portion is to show the movement of patients in the simulation after each iteration
    #pls use this portion only for a small number of iterations
    #it uses the scatter plot to show the position of the people
    fig, ax = plt.subplots()
    #healthy 
    ax.scatter(x, y, color= "green",s=30) 
    #hospital
    ax.scatter(h1, h2, color= "blue",s=30)
    #infected
    ax.scatter(x1, y1, color= "red",s=30)
    
    ax.legend()
    
    plt.legend() 
    
    plt.show() 
    """
    #this section is the code that decides if the person is infected of healthy
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

#this is the plot that shows the healthy and infected versus number_of_iterations/time
xaxis=[i for i in range(0,no_of_iterations)]
plt.plot(xaxis,hea,color="green")
plt.plot(xaxis,inf,color="red")
