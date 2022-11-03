#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math as m
import numpy as np
import matplotlib.pyplot as plt
    
def datapunkter():
    global x_liste
    global y_liste
    global x_akse
    global y_akse
    global label
    x_liste = []
    y_liste = []
    data_in = input("Skriv inn datapunkt, eller stopp for å avslutte. ")
    while(data_in != "stopp"):
        data_in = data_in.split(",")
        x_liste.append(float(data_in[0]))
        y_liste.append(float(data_in[1]))
        data_in = input("Skriv inn datapunkt, eller stopp for å avslutte. ")

    print(x_liste)
    print(y_liste)
    
    if handling_a == 'ny':
        plt.plot(x_liste, y_liste)
        label = plt.title(input("graf-tittel: "))
        x_akse = plt.xlabel(input("X-akse-tittel: "))
        y_akse = plt.ylabel(input("Y-akse-tittel: "))
        plt.show()
        
    else:
        vise()

def innstillinger():
    plt.plot(x_liste, y_liste)
    label = input("Tittel: ")
    x_akse = input("Xen-akse-tittel: ")
    y_akse = input("Y-akse-tittel: ")
    plt.xlabel(x_akse)
    plt.title(label)
    plt.ylabel(y_akse)
    plt.show()
    
def lagre():
    filnavn = input("Hvilket filnavn vil du lagre grafen din med? ")
    fil = open(filnavn, 'w', encoding="UTF-8")
    fil.write(str(label) + "\n")
    fil.write(str(x_akse) + "\n")
    fil.write(str(y_akse) + "\n")
    fil.write(str(x_liste))
    fil.write(str(y_liste))
    fil.close()
    print('Da har du lagret ', filnavn, '!')
    
def laste():
    global filnavn_open
    filnavn_open = input("Hvilken graf vil du åpne?")
    f = open(filnavn_open, "r+")
    print(f.read())
    vise()
    
def vise():
    plt.plot(x_liste, y_liste)
    plt.title(label)
    plt.xlabel(x_akse)
    plt.ylabel(y_akse)
    plt.show()

    
def hoved_funksjon():
    global handling_a 
    handling_a = input("Vil du starte en ny graf eller laste opp en gammel? (ny/gammel) ")
    if handling_a == 'ny':
        datapunkter()
    else:
        laste() 
    handling_b = input("Hva vil du gjøre med grafen? (lagre, innstillinger, endre datapunkter, avslutte, vise) ")
    while (handling_b != 'avslutte'):
        if (handling_b == 'lagre'):
            lagre()
        elif (handling_b == 'innstillinger'):
            innstillinger()
        elif (handling_b == 'endre datapunkter'):
            datapunkter()
        elif (handling_b == 'vise'):
            vise()
        handling_b = input("Hva vil du gjøre med grafen? (lagre, innstillinger, endre datapunkter, avslutte, vise) ")
    
hoved_funksjon()


# In[ ]:




