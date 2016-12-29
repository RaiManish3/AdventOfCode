import time
begin = time.time()

def main():
	f=open('day25.txt','r')
	lst=[]
	for i in xrange(30):
		lst.append(f.readline().strip().split(" "))

	dic = {'a':0,'b':0,'c':0,'d':0}

	# i want to  check upon 10 outputs, i think that is satisfactory
	r=1
	while 1:
		out = 0
		index =0
		flag =False
		dic['a']=r
		# print "-------------------",r
		count = 0

		while count < 10:
			if index == 2:
				dic['a']=0
				dic['d']=dic['d']+231*dic['c']
				dic['b']=dic['d']
				dic['c']=2
				index =13

			elif index == 3:
				dic['d']+=dic['b']
				dic['b']=0
				index = 6

			if lst[index][0]=="cpy":
				if lst[index][1].isdigit() or lst[index][1][1:].isdigit():
					dic[lst[index][2]]=int(lst[index][1])
				else :
					dic[lst[index][2]]=dic[lst[index][1]]
				index+=1

			elif lst[index][0]=="inc":
				dic[lst[index][1]]+=1
				index+=1

			elif lst[index][0]=="dec":
				dic[lst[index][1]]-=1
				index+=1

			elif lst[index][0]=="jnz":
				if (lst[index][1].isdigit() or lst[index][1][1:].isdigit()) and int(lst[index][1]):
					index+=int(lst[index][2])

				elif  lst[index][1] in dic.keys() and dic[lst[index][1]]:
					index+=int(lst[index][2])

				else:
					index+=1

			elif lst[index][0]=="out":
				count+=1
				# print "out =",dic[lst[index][1]]
				if flag:
					if dic[lst[index][1]]==1:
						index+=1
						flag=False
					else :
						out = -1
						break

				else :
					if dic[lst[index][1]]==0:
						index+=1
						flag=True
					else :
						out = -1
						break

		if out == 0:
			return r
		r+=1

print "the answer is :",main()
print time.time()-begin