# -*- coding: utf-8 -*-
"""
Created on Mon Nov 07 10:37:54 2016

@author: Tamonwan
"""
from motif import Score, PartialScore

def greedymotif(dna,t,n,l):
    bestMotif = [1]*t
    starts = [1]*t
    curnode = 0
    for starts[0] in range(n-l+1):
        for starts[1] in range(n-l+1):
            align_mat,parscore = PartialScore(dna,starts,2,t,n,l)
            align_mat,bestscore = PartialScore(dna,bestMotif,2,t,n,l)
            curnode+=1
            if parscore > bestscore:
                bestMotif[0] = starts[0]
                bestMotif[1] = starts[1]
    starts[0] = bestMotif[0]
    starts[1] = bestMotif[1]
    for i in range(2,t):
        for starts[i] in range(n-l+1):
            align_mat,parscore = PartialScore(dna,starts,i+1,t,n,l)
            align_mat,bestscore = PartialScore(dna,bestMotif,i+1,t,n,l)
            curnode+=1
            if parscore > bestscore:
                bestMotif[i] = starts[i]
        starts[i] = bestMotif[i]
    align_mat, score = Score(dna,starts,t,n,l)
    return (bestMotif,align_mat, score,curnode)
    