# -*- coding: utf-8 -*-
# file_name.py
# Python 3.7
"""
@author: Wei-shan
Created on Thu Jan  3 23:27:34 2019
Modified on Thu Jan  3 23:27:34 2019

Description
------------------------
Plot the function which is continuous everywhere but not differentiable
anywhere. From Rudin P. 154.
"""
import numpy as np
import matplotlib.pyplot as plt
import pyprind
from matplotlib.ticker import AutoMinorLocator, FormatStrFormatter
import decimal

#%% confine x within the range -1<=x<=1
#   return a decimal.Decimal type xx
#   need to change mod and period if the function's period changes
def confineX(x_input): 
    xx = decimal.Decimal(str(x_input%2)) # xx is type decimal
    if ( float(xx) >= -1.0 ) and ( float(xx) <= 1.0 ):
        return xx
    else:
        if ( float(xx) >= 1.0 ) and ( float(xx) <= 2.0 ):
            xx = xx - decimal.Decimal('2.0')
            return xx
        elif ( float(xx) >= -2.0 ) and ( float(xx) <= -1.0 ):
            xx = xx + decimal.Decimal('2.0')
            return xx
        else:
            print("something is wrong with confineX()")
#%% calculate big numbers product with the form xx*base**exponent
#   where xx is a float while base and exponent are integers
def bigNumMul(xx,base,exponent): 
    float_string = str(xx) # to show that rounding works
    decimal.getcontext().prec = exponent #+ 1
    cc = base ** exponent # + 1
    dd = decimal.Decimal(float_string) * cc
    return dd

#%% function phi(x)
def phi(x):
    xx = float(confineX(x))
    return abs(xx)
#%% function f(x)
infinity = 1000  #000
def fn(x):
    sum_ =0.0
    #xlong = get_decimal(x,base,exponent)
    for n in range(infinity):
        if n == 0:
            temp = phi(x)
            sum_ = sum_ + temp
            continue
        sum_ = sum_ + (3.0/4.0)**n*phi( bigNumMul(x,4,n) )
    return sum_
#%%
nPoints = 1000
halfPeriod = 1.0
xValues =  np.linspace(-halfPeriod, 0, nPoints, endpoint=False)

pbar = pyprind.ProgBar(len(xValues), monitor=True,
                       title = "NoWhereDiffContinuousFunction")
yValues = [] #list( map(fn,xValues) )

for xx in xValues:
    yy = fn(xx)
    yValues.append(yy) #yValues += [yy]
    pbar.update()
printpbar = open("C:/Users/Wei-shan/.spyder-py3/NoWhereDiffContiFunction" + \
                 "/printpbar.dat",'w')
print(pbar, file=printpbar)
printpbar.close()
#%%
xValues = np.append(xValues,np.linspace(0, 
                    halfPeriod, nPoints+1, endpoint=True),axis=0)

yValues = np.asarray(yValues)

yValues_reverse = yValues[::-1]  # yValues[::-1] reverse the array
yValues = np.append(yValues,fn(0))
yValues = np.append(yValues,yValues_reverse) 

xyValues = open("C:/Users/Wei-shan/.spyder-py3/NoWhereDiffContiFunction" + \
                "/xyValues.dat",'w')
#C:\Users\Wei-shan\.spyder-py3\NoWhereDiffContiFunction

for ii in range( len(xValues) ):
    xyValues.write( "%g\t%g\n" % ( xValues[ii],yValues[ii] ) )
    
xyValues.close()

plt.plot(xValues, yValues, 'k-')
plt.xlabel("x values")
plt.ylabel("$\ f(x)$")
plt.title('Iteration of n = ' + str(infinity) + '; ' + 'Number of Point = ' 
          + str(nPoints))
#plt.legend(loc="upper corner")
plt.show()
plt.savefig("C:/Users/Wei-shan/.spyder-py3/NoWhereDiffContiFunction" + \
            "/Iteration_" + str(infinity) +".jpg")
