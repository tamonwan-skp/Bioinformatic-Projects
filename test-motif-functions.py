import sys,os
from motif import ByPass, NextVertex, AllLeaves, Score, partial_Score

def test_AllLeaves():
	print("******** Test AllLeaves() ********")
	L = 3	# no. of sequence
	k = 3	# last possible starting position
	AllLeaves(L,k)

def test_NextVertex():
	print("******** Test NextVertex() ********")
	a=["*",1,1,2,1]
	i=3
	L=4
	k=2
	print "current=%s" % (a)

	[n,ln] = NextVertex(a,i,L,k)
	print "NextVertex=%s, i=%d\n" % (n,ln)


	a=["*",1,2,2,1]
	i=3
	L=4
	k=2
	print "current=%s" % (a)

	[n,ln] = NextVertex(a,i,L,k)
	print "NextVertex=%s, i=%d\n" % (n,ln)

		
def test_ByPass():
	print("******** Test ByPass() ********")
	a=["*",1,1,2,1]
	i=3
	L=4
	k=2
	print "current=%s" % (a)

	[b,lb] = ByPass(a,i,L,k)
	print "Bypass=%s, i=%d\n" % (b,lb)

	a=["*",1,2,2,1]
	i=3
	L=4
	k=2
	print "current=%s" % (a)

	[b,lb] = ByPass(a,i,L,k)
	print "Bypass=%s, i=%d\n" % (b,lb)


def test_Score():

	l = 4  # motif length
	s = [4,3,7,6] # [1,4,5,2] where 1<= si <= (n-l+1)

	print("******** Test Score() DNA1 ********")

	dna = [ [0,1,2,3,2,2,3,4,1,2,3], # t = 4
			[0,2,2,3,2,2,3,4,1,2,3], # 1=A,2=T,3=G,4=C
			[0,3,2,1,4,2,3,4,1,2,3],
			[0,1,2,3,2,2,3,4,1,2,3] ]

	t = len(dna)	# number of input sequences
	n=len(dna[0])	# sequence length

	align_mat, score = Score(dna,s,t,n,l)
	for seq in align_mat: 
		print seq
	print ("Score: %d\n") % score


	print("******** Test Score() DNA2 ********")

	dna2 = ["ACGGGGTCTCGAAAAAAGGAGAATGGGA",
			"TTCATCCTAGTCTTCCAGTTATCGTTTC",
			"CTCTCTCTCATTTTCTTTGCCTGGGCCC",
			"GATGTTCTTGTGTCCGAAATTGGTGGGT"]

	t = len(dna2)	# number of input sequences
	n=len(dna2[0])	# sequence length

	align_mat, score = Score(dna2,s,t,len(dna2[0]),l)
	for seq in align_mat: 
		print seq
	print ("Score: %d\n") % score

def test_partialScore():
    l = 4  # motif length
    s = [4,3,7,6] # [1,4,5,2] where 1<= si <= (n-l+1)
    level = 2
	
 
    print("******** Test partial Score() DNA1 ********")
    
    dna = [ [0,1,2,3,2,2,3,4,1,2,3], # t = 4
			[0,2,2,3,2,2,3,4,1,2,3], # 1=A,2=T,3=G,4=C
			[0,3,2,1,4,2,3,4,1,2,3],
			[0,1,2,3,2,2,3,4,1,2,3] ]

    t = len(dna)	# number of input sequences
    n=len(dna[0])	# sequence length

    align_mat, score = partial_Score(dna,s,level,t,n,l)
    
    for seq in align_mat: 
        print seq
    
    print ("Score: %d\n") % score


    print("******** Test Score() DNA2 ********")

    dna2 = ["ACGGGGTCTCGAAAAAAGGAGAATGGGA",
			"TTCATCCTAGTCTTCCAGTTATCGTTTC",
			"CTCTCTCTCATTTTCTTTGCCTGGGCCC",
			"GATGTTCTTGTGTCCGAAATTGGTGGGT"]

    t = len(dna2)	# number of input sequences
    n=len(dna2[0])	# sequence length

    align_mat, score = partial_Score(dna2,s,level,t,n,l)
    for seq in align_mat: 
		print seq
    print ("Score: %d\n") % score
    
if __name__ == "__main__":

#	test_AllLeaves()
#	raw_input("Enter to continue...\n")
    test_ByPass()
    raw_input("Enter to continue...\n")
#	test_NextVertex()
#	raw_input("Enter to continue...\n")
#    test_Score()
 #   raw_input("Enter to continue...\n")
 #  test_partialScore()
    
    print "End-Of-Program\n"
