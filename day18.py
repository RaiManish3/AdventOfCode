import time
start=time.time()

def main():
	f=open('day18.txt','r')
	strx = f.readline()
	l=len(strx)

	rows = 400000-1
	count = 0
	count+= count_safe(strx)
	# print strx

	for i in xrange(rows):
		stry=""
		for j in xrange(l):
			if(check_safe(j,strx)):
				stry+="."
			else : stry+="^";
		strx=stry
		# print strx
		count+= count_safe(strx)

	print count

def count_safe(strx):
	count=0
	for i in strx:
		if(i=="."):
			count+=1
	return count

def check_safe(index,strx):
	# left and center are traps
	if(index-1>=0 and strx[index-1]=='^' and strx[index]=='^'):
		if(index+1>=len(strx) or strx[index+1]=='.'):
			return False

	# center and right are traps
	if(index+1<len(strx) and strx[index+1]=='^' and strx[index]=='^'):
		if(index-1<0 or strx[index-1]=='.'):
			return False

	# left only
	if(index-1>=0 and strx[index-1]=='^' and strx[index]=='.' and (index+1>=len(strx) or strx[index+1]=='.')):
		return False

	# right only
	if(index+1<len(strx) and strx[index+1]=='^' and strx[index]=='.' and (index-1<0 or strx[index-1]=='.')):
		return False
	return True


main()
print time.time()-start