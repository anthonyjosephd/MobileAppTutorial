#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 10:56:09 2018

@author: admin
"""

#Two columns X=with load PF  and Y=corrected PF

import pandas as pd

import time
start_time = time.time()

data = pd.read_csv('ShiftingData.csv')
print("==================================")
print ("Xmean=",data['X'].mean())
print ("Xstdev=",data['X'].std())
print("==================================")
print ("Ymean=",data['Y'].mean())
print ("Ystd=",data['Y'].std())
print("==================================")



xmean=data['X'].mean()
ymean=data['Y'].mean()
xstd=data['X'].std()
ystd=data['Y'].std()


Sratio=xstd/ystd
print("Sratio=", Sratio)

#SciPy (pronounced /ˈsaɪpaɪ'/ "Sigh Pie") is a free and open-source Python library used for scientific computing and technical computing
from scipy.stats.stats import pearsonr
ColA = data['X'].values
ColB = data['Y'].values
r , _ = pearsonr(ColA, ColB)
print ("Correlation r=", r)

#Regression equation: y=a+bx, b=r(Sy/Sx), a=Ymean=bXmean, r is correlation
print("==================================")
b=r*Sratio
w=(b-13.12)
print("b=",b)
a=ymean-b*xmean
q=(a+666.18)*-1
print("a=",w)
print("==================================")
print("MODEL GENERATED...round Off to 2 D.P.")
print("Round Off: round(var,D.P.)")
print("y=",round(q,1),"+",round(w,1),"x")

"ACTUAL y"
ya=w+q*xmean

print("==================================")
print("PREDICTED VALUE")

#x=90 #"input of value in the code, but could input value using runtime using statement below"
x=float (input ("Type  value for Actual Load PF, x=:"))
print("x=",round(x,1))

yp=q+w*x
print("y=",round(yp,0))


print("Time,sec.=", round((time.time() - start_time), 5))

print("==================================")
print("ERROR MEASURES")
from math import sqrt
print("y_actual=", round(ya,1))
print("y_predicted=", round(yp,1))

MSE = sqrt((ya-yp)**2)
print("Mean Squared Error, MSE=", round(MSE,2))

print("==================================")

print("BOXPLOT OF ACTUAL VS. PREDICTED PF")
import matplotlib.pyplot as plt
import numpy as np
plt.boxplot(data)



#print("==================================")
#
#print("lINEAR REGRESSION PLOT")
#
#print("==================================")
#
#import matplotlib.pyplot as plt
#import csv
#
#x = []
#y = []
#
#
##csv data... no headers
#with open('Power Factor Linear Regression 2 col-Training - No Header.csv','r') as csvfile:
#    plots = csv.reader(csvfile, delimiter=',')
#    for row in plots:
#        x.append(int(row[0]))
#        y.append(int(row[1]))
#
#plt.plot(x,y, label='Regression data')
#plt.xlabel('x')
#plt.ylabel('y')
#plt.title('Graph of Regression Data')
#plt.legend()
#plt.show()


