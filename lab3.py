############################  12.16  Start #############################
'''

from scipy.optimize import fsolve
from math import exp, pi, tan
def my_func(x):
    return  exp(-x) - tan(x) * (x**2)  - pi 

x_star = fsolve(my_func, x0=1)
print('x_star = {:.4f}; checking: f(x_star) = {:.4f}.'.format(x_star[0],my_func(x_star[0])))

'''

############################  12.16  End #############################

############################  12.17  Start #############################
'''
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def my_func(x, a1, a2, t1, t2):
    return a1 * np.exp(-x/t1) + a2 * np.exp(-x/t2)

X, Y = np.loadtxt('some_data.dat',unpack=True)
par, cov = curve_fit(my_func,X,Y,p0=[1,1,1,1])


R2 = 1 - np.sum( (Y - my_func(X, *par) )**2 ) / np.sum( (Y - np.mean(Y))**2 )

print(R2)

my_x = np.linspace(min(X),max(X),10*len(X))
my_y = my_func(my_x,*par)
plt.scatter(X,Y,marker='o',color='black',label='data')
plt.plot(my_x,my_y,color='red',label='fit')
plt.legend()
plt.show()
'''

############################  12.17  End #############################

############################  12.19  Start #############################
'''

import numpy as np
with open("./linear_algebra.dat") as f:
    # determining number of columns from the first line of text
    n_cols = len(f.readline().split("  "))

A = np.loadtxt('linear_algebra.dat',  usecols= np.arange(0, n_cols-1)) 
B = np.loadtxt('linear_algebra.dat',  usecols=(n_cols-1))
x = np.linalg.solve(A,B)

print("{0:0.4f}".format(x[0]))
print("{0:0.4f}".format(x[1]))

'''
############################  12.19  End #############################


