# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 13:08:20 2016

@author: user
"""
#def Global(v,w,m,n):
#    s=[]
#    w=[]
#    i=1
#    j=1
#    n = len(v)
#    m = len(w)
#    for i in range(0,n):
#        s.append([0] *m )        
#    s[0][0]=0
#
#    for i in range(n):
#        s[i][0]=s[i-1][0]+w[i][0]
#    for j in range(m):
#        s[0][j]=s[0][j]+w[0][j]
#    for i in range(n):
#        for j in range(m):
#            if (v[i]==w[j]):
#                s[i][j]= s[i-1][j-1]+1
#            if (s[i-1][j]+w[i][j] > s[i][j-1]+w[i][j]):
#                s[i][j]=s[i-1][j]+w[i][j] 
#            else:
#                s[i][j]=s[i][j-1]+w[i][j]
#    print s
#    return s[n][m]

#if __name__ == "__main__":
w = "ACCGGGTTAC"
v="AGGACCA"    
n = len(v)
m = len(w) 
s=[]
i=1
j=1

for i in range(0,n):
    s.append([0] *m )        

s[0][0]=0

for i in range(n):
    
    s[i][0]=s[i-1][0]
for j in range(m):
    s[0][j]=s[0][j]
for i in range(n):
    for j in range(m):
        if (v[i]==w[j]):
            s[i][j]= s[i-1][j-1]+5
        if (s[i-1][j] > s[i][j-1]):
            s[i][j]=s[i-1][j]+1 
        else:
            s[i][j]=s[i][j-1]+1
print s
#return s[n][m]