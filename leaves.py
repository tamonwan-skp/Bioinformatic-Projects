import sys,os
def Nextvertex(a,i,L,k):
    if i<L:
        a[i+1]=1
        return[a,i+1]
    else:
        for j in range(L,0,-1):
            if a[j]<k: 
                a[j]+=1
                return[a,j]
    return[a,0]
            
def NextLeaf(a,L,k):
    #print " NextLeaf\n"
    #give [L,L-1,...,1]
    for i in range(L,0,-1):
        if  a[i]<k:
            a[i]=a[i]+1
            return a
            
        a[i] = 1
    return a
    
    
def AllLeaves(L,k):
    print " You are in AllLeave\n"
    a = [1]*(L+1)
    # a is list so you can do like this to increase element in [...]    
        
    while True: #always true
        #print a
        a = NextLeaf(a,L,k)
        if a == [1]*(L+1):
            return  
            
def Bypass(a,i,L,k):
    for j in range(i,0,-1): #middle is step (dont count)
        if a[j] < k:
            a[j]+=1
            return [a,j]
    return[a,0]

def score(s,DNA) :
    n = len(DNA[0])
    am = []
    
    for i in range(t):
        am.append([])

        if(s[i]>n-l+1):
           s[i]=n-l+1;

        for j in range(s[i],s[i]+l,1):
            am[i].append(DNA[i][j])
    print("\nAlignment :\n") 
    
    for seq in am:   
        print seq

    max_col_freq = [0]*l

    for i in range(l):
        col_freq = [0]*4 
    
        for j in range(t):
            ch = am[j][i]

            if ch =='A' : col_freq[0]+=1;
            elif   ch =='T' : col_freq[1]+=1;
            elif   ch =='C' : col_freq[2]+=1;
            elif   ch =='G' : col_freq[3]+=1;
           
        max_col_freq[i] = max(col_freq)
    score = 0 
    
    for e in max_col_freq :
        score = score + e

    print '\nscore : %d' %(score) 
    return       
             
if __name__ == "__main__":
#     L = 3 #no of sequence
#     k = 3 #last possible strating position
#        #AllLeaves(L,k)
#        
#   a=["*",1,1,2,1]# add one more dont care
#   i=3
#   L=4
#   k=2
#   [a,i]=Bypass(a,i,L,k)
#   print"a=%s, i=%d" %(a,i)
   
    n = 10
    l = 4 #motif length
    t = 4 #no of input sequences
    s = [1,2,2,1] #strating position 
#    DNA=[[0,1,2,3,2,2,3,4,1,2,3], #t=4  
#         [0,2,2,3,2,2,3,4,1,2,3], #1=A,2=T,3=G,4=C
#         [0,3,2,1,4,2,3,4,1,2,3],
#         [0,1,2,3,2,2,3,4,1,2,3]]
    DNA2=['AAATTGGGCCCCAAAATTT',
          'GGGTTTTAAAACCTAGAAT',
          'TTCGAATGCCCGTAATGCC',
          'GATAGATAGATCACACCCT',]

    score(s,DNA2)

