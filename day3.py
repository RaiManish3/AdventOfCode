import time
begin=time.time()

################################################################################
# ==========================EXECUTION TIME: 30ms================================

def main():
	f=open('day3.txt','r')
	lst=[0 for i in xrange(9)]
	count=0

	for i in xrange(545):

		#taking input
		strx=f.readline().strip()
		strx+=' '+f.readline().strip()
		strx+=' '+f.readline().strip()

		index=0
		for j in xrange(9):
			while index<len(strx) and not strx[index].isspace():
				lst[j]=lst[j]*10+int(strx[index])
				index+=1
			while index<len(strx) and strx[index].isspace():
				index+=1
		
		lst0,lst1,lst2=[0,0,0],[0,0,0],[0,0,0]
		for x in xrange(3):
			lst0[x]=lst[3*x]
		for x in xrange(3):
			lst1[x]=lst[3*x+1]
		for x in xrange(3):
			lst2[x]=lst[3*x+2]

		lst0.sort()
		lst1.sort()
		lst2.sort()

		if lst0[0]+lst0[1]>lst0[2]:
			count+=1
		if lst1[0]+lst1[1]>lst1[2]:
			count+=1
		if lst2[0]+lst2[1]>lst2[2]:
			count+=1

		#resetting list
		lst=[0 for i in xrange(9)]

	return count

print main()
print time.time()-begin