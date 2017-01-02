import time
begin=time.time()

########################################################################
# ====================EXCECUTION TIME: BOTH PARTS UNDER 1ms=============

def recur(fr,to,lst,dic):
	dic[lst[fr][1]]+=dic[lst[to][1]]
	dic[lst[to][1]]=0

def main():
	f=open('day12.txt','r')
	lst=[]
	for i in xrange(23):
		lst.append(f.readline().strip())
		lst[i]=lst[i].split(' ')

	index=0
	l=len(lst)

	# part 1---> c=0, part 2--->c=1
	dic={'a':0,'b':0,'c':1,'d':0,'1':1}

	while index<l:

		# cpy
		if lst[index][0]=="cpy":
			if lst[index][1] in dic.keys():
				dic[lst[index][2]]=dic[lst[index][1]]
			else : dic[lst[index][2]]=int(lst[index][1])
			index+=1

		# inc
		elif lst[index][0]=="inc":
			dic[lst[index][1]]+=1
			index+=1

		elif lst[index][0]=="dec":
			dic[lst[index][1]]-=1
			index+=1

		elif lst[index][0]=="jnz":
			count=0
			if dic[lst[index][1]]:
				if int(lst[index][2])<0:
					for i in xrange(index+int(lst[index][2]),index):
						if lst[i][0]=="jnz":
							count=1
							break
					if count==0:
						recur(index+int(lst[index][2]),index-1,lst,dic)
						index+=1

					else : index+=int(lst[index][2])

				else: index+=int(lst[index][2])
			else : index+=1

	return dic


print main()
print time.time()-begin