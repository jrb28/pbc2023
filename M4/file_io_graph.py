# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 10:28:01 2023

@author: jrbrad
"""

import matplotlib.pyplot as plt

f = open('sf.csv','r')
sf = f.readlines()

''' Don't do this 
for row in sf:
    # whitespace characters include, spaces, tabs, line feeds, etc.
    row = row.strip() # removes whitespace characters from right and left
    row = row.split(',')  '''
    
for i in range(len(sf)):
    # whitespace characters include, spaces, tabs, line feeds, etc.
    sf[i] = sf[i].strip() # removes whitespace characters from right and left
    sf[i] = sf[i].split(',')
    sf[i] = [sf[i][0][2:], int(sf[i][1])]
    
x = []
y = []

for row in sf:
    x.append(row[0])
    y.append(row[1])
    
plt.plot(y)
plt.suptitle('SF Housing Prices')
plt.xlabel('Date (YY-MM)')
plt.ylabel('Average Home Price')
#plt.xticks(range(len(x)), x)
p = 24
plt.xticks([i for i in range(len(x)) if i%p==0], [x[i] for i in range(len(x)) if i%p==0])
plt.show()