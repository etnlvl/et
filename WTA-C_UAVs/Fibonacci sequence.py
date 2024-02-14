# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 11:21:09 2024

@author: elaval
"""

from time import perf_counter
import numpy as np 
import matplotlib.pyplot as plt 
### This is the usual way of calculating fibonacci sequence with recursive algorithm, 
### we call the funcction itself in this same function"""" 

# def fib(n) : 
#     if n==0 :
#         return 0 
#     if n==1 : 
#         return 1 
#     return fib(n-1) + fib (n-2)

###just few lines to determine the running time of this function 


# s= perf_counter()
# print (fib(45))
# print(perf_counter()-s)



### Fibonacci sequence using dynamic programming method 


temp_dict = dict()    #we create a dictionnary in order to save the values which can be usefull later 

## First method : Dynamic programming using top-down method, very similar to recursive approach but the 
## difference is that we'll save the solutions to subproblems we encounter. 

def fib_dp_td(n) : 
    if n==0 :
        return 0 
    if n==1 : 
        return 1 
    if temp_dict.get(n,-1) == -1:
        temp_dict[n] = fib_dp_td(n-1) + fib_dp_td(n-2)
    return temp_dict[n]


# still for calculating the running time of the dynamic program using Top-down method. 

a= perf_counter()
print (fib_dp_td(45))
print(perf_counter()-a)

## Second Method : Dynamic programming using bottom-up method. We'll reorganize the order in which 
## we solve the subproblems. The running time of this method is much better than the top-down approach. 

def fib_dp_bu(n) : 
    
    arr= [0]*(n+1)
    arr[0],arr[1] = 0, 1
    for i in range (2,n+1):
        arr[i]=arr[i-1] + arr[i-2]
    return arr[-1],arr

#Running time of the dynamic programm using a bottom-up approach. 

s= perf_counter()
print (fib_dp_bu(45)[0])
print(perf_counter()-s)




