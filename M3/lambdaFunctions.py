# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 08:12:56 2023

@author: jrbrad
"""

# f(x) = x**2
# x is the input
# x**2 is the output

f = lambda x:x**2

print(f(3))

y = 5
print(f(y))

data = [[9,1], [8,2]]

data.sort(key= lambda x:x[1], reverse=True)
print(data)

g = lambda x:x[1]
data.sort(key= g)
print(data)