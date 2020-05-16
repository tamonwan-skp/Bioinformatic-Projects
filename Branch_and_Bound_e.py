# -*- coding: utf-8 -*-
"""
Created on Mon Nov 07 10:37:54 2016

@author: Tamonwan
"""

from motif import ByPass, NextVertex, Score, PartialScore

def Branch_and_Bound(dna,t,n,l):
    tempstarts = ['*']*(t+1)
    starts = [1]*t
    curnode = 0
    for i in range(len(starts)):
        tempstarts[i+1] = starts[i]
    bestScore = 0
    level = 1
    bestMotif = []
    while level > 0:
        if level < t:
            align_mat,tempScore = PartialScore(dna,starts,level,t,n,l)
            OptimisticScore = tempScore + (t-level)*l
            curnode+=1
            if OptimisticScore < bestScore:
                tempstarts,level = ByPass(tempstarts,level,t,n-l+1)
                starts[0:4][:] = tempstarts[1:5][:]
            else:
                tempstarts,level = NextVertex(tempstarts,level,t,n-l+1)               
                starts[0:4][:] = tempstarts[1:5][:]
        else:
            align_mat,tempScore = Score(dna,starts,t,n,l)
            curnode+=1
            if tempScore > bestScore:
                bestScore = tempScore
                bestMotif = [starts[0],starts[1],starts[2],starts[3],starts[4]]
            tempstarts,level = NextVertex(tempstarts,level,t,n-l+1)
            starts[0:4][:] = tempstarts[1:5][:]

    return (bestMotif,bestScore,curnode)

