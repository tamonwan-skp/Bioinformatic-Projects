# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 13:33:51 2016

@author: Tamonwan580635907
"""

##### HOW TO IMPLEMENT THE PROGRAMM #######
""" 1) insert python file(.py) and two input sequences (note:must add * at first element of the sequences)
      e.g. run lab05-lsa-580635907.py *CGTGAATCAT *GACTAC
      
    2) insert the scores for Match, Mismatch and Gap(indel) via IPython console
"""
import sys

print"\n\n-------------------------------------------------------"
print"  This is Local Sequence Alignment Algorithm "
print"-------------------------------------------------------"

#w= "*CGTGAATCAT"
#v= "*GACTAC"
w = sys.argv[1]
v = sys.argv[2]

print"\nPlease specify the scores for Match, Mismatch and Gap(indel)"
match = input("Match scores = ")
mismatch =  input("Mismatch scores = ")
gap =  input("Ga1p(indel) scores = ")

rows = len(v)
columns = len(w)   
    
#### Set up an empty rows x columns matrix #######
s = []
Diag = []
b=[]
best=0
for i in range(0, rows):
    s.append([0] * columns)
    Diag.append([0]* columns)
    b.append([0]*columns)
   
#### Fill in the first row and first column with 0 #######
for i in range(0, rows):
    s[i][0] = 0
for j in range(1, columns):
    s[0][j] = 0
#print s

#### Then fill in the rest of the table ########
for i in range(1, rows):
    for j in range(1, columns):
        if (v[i] == w[j]):
            Diag[i][j] = s[i-1][j-1]+match
    
        else:
            Diag[i][j] = s[i-1][j-1]+mismatch          
        s[i][j] = max(Diag[i][j], s[i-1][j] + gap, s[i][j-1] + gap ,0)
#### Then reconstruct backtracking pointer #######          
        if (s[i][j] == Diag[i][j]):
            b[i][j] = "dia" 
        elif (s[i][j] == s[i-1][j] + gap):
            b[i][j] = "top"
        elif (s[i][j] == s[i][j-1] + gap):
            b[i][j] = "left"
            
### find max score ########       
        if (s[i][j] > best ):
            best = s[i][j]
print "\n[[ Score is : %d ]]" %best
        
#### find all best score ####
found =[]
for i1,j in enumerate(s):
    for k,l in enumerate(j):
        if l==best:
            found.append([i1,k])
lenbest = len(found)
for k in range(lenbest):            
       r = found[k][0]
       c = found[k][1]
       
v_aln =[]
w_aln =[]

while r != 0 and c !=0:
    if(b[r][c] == "dia" ):
        v_aln.append(v[r])
        w_aln.append(w[c])
        r= r-1
        c= c-1
        
    elif(b[r][c] == "top" ):
        v_aln.append(v[r])
        w_aln.append('_')
        r=r-1
    else:
        v_aln.append("_")
        w_aln.append(w[c])
        c=c-1
#print v_aln
#print w_aln

### rearrange alignment #######

f_v = ['1']*len(v_aln)
f_w = ['1']*len(w_aln)
ind = len(v_aln)
ind2 = len(w_aln)
for i in range(ind):
    f_v[i] = v_aln[ind-1]
    ind-=1
for i in range(ind2):
    f_w[i] = w_aln[ind2-1]
    ind2-=1
print"\nThe alignments are :\n"
print f_v
print f_w

