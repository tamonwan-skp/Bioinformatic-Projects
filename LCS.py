# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 10:37:02 2016

@author: Tamonwan

"""
def LCS(v,w,):
    i=0
    j=0
    s =[[]]
    b =[[]]
   # score = [1,1,1]
    
    for i in range(n):
        s[i][0]=0

    for j in range(m):
        s[0][j]=0
    
    for i in range(1,n):
        for j in range(1,m):
            if (v[i] == w[j]):
                s[i][j]=s[i-1][j-1]+1
                b[i][j]="diagonal"
            elif s[i][j-1]>s[i-1][j]:
                s[i][j]=s[i][j-1]
            else:
                s[i][j]=s[i-1][j]
    print s
                                    
if __name__ == "__main__":
    v = " ACCGGGTTAC"
    w=" AGGACCA"    
    n = len(v)
    m = len(w)   
    LCS(v,w);                
            
                    
    
