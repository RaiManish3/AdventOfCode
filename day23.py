import time
begin=time.time()

def recur(fr,to,lst,dic):
	dic[lst[fr][1]]+=dic[lst[to][1]]
	dic[lst[to][1]]=0

def main():
	f=open('day23.txt','r')
	lst=[]
	size =26
	for i in xrange(size):
		lst.append(f.readline().strip())
		lst[i]=lst[i].split(' ')

	index=0
	l=len(lst)

	dic={'a':12,'b':0,'c':0,'d':0,'1':1}

	while index<l:

		# jump from index = 5 to index = 16 using maths
		# better would be , i beleive the method of memoization
		if index == 5:
			dic['a']=(dic['a']+dic['c'])*dic['d']
			dic['b']=dic['b']-1
			dic['c']=2*dic['b']
			dic['d']=0
			index=16

		if lst[index][0]=="cpy":
			# skip invalid step cpy 1 2
			if lst[index][1] not in dic.keys() and lst[index][2] not in dic.keys():
				index+=1
				continue

			if lst[index][1] in dic.keys():
				dic[lst[index][2]]=dic[lst[index][1]]
			else : dic[lst[index][2]]=int(lst[index][1])
			index+=1


		elif lst[index][0]=="inc":
			dic[lst[index][1]]+=1
			index+=1

		elif lst[index][0]=="dec":
			dic[lst[index][1]]-=1
			index+=1

		elif lst[index][0]=="jnz":
			count=0
			if (lst[index][1] in dic and dic[lst[index][1]]) or ((lst[index][1].isdigit() or lst[index][1][1:].isdigit()) and int(lst[index][1])):
				# sec arg is int and <0
				if (lst[index][2].isdigit() or lst[index][2][1:].isdigit()) and int(lst[index][2])<0:
					for i in xrange(index+int(lst[index][2]),index):
						if lst[i][0]=="jnz":
							count=1
							break
					if count==0:
						if lst[index-1][0]=="dec":
							ind_dec = index-1
							ind_inc = index-2
						else : 
							ind_dec = index-2
							ind_inc = index-1
						recur(ind_inc,ind_dec,lst,dic)
						index+=1

					else : index+=int(lst[index][2])

				# sec arg is int and >0
				elif  (lst[index][2].isdigit() or lst[index][2][1:].isdigit()) and int(lst[index][2])>0: 
					index+=int(lst[index][2])

				# sec arg is in dic and <0
				elif lst[index][2] in dic and dic[lst[index][2]]<0:
					for i in xrange(index+dic[lst[index][2]],index):
						if lst[i][0]=="jnz":
							count=1
							break
					if count==0:
						if lst[index-1][0]=="dec":
							ind_dec = index-1
							ind_inc = index-2
						else : 
							ind_dec = index-2
							ind_inc = index-1
						recur(ind_inc,ind_dec,lst,dic)
						index+=1

					else : index+=dic[lst[index][2]]

				else :
					index+=dic[lst[index][2]]

			else : index+=1

		elif lst[index][0]=="tgl":
			target = index +dic[lst[index][1]]
			
			index+=1
			if target<l:
				if lst[target][0]=="cpy":
					lst[target][0]="jnz"
				elif lst[target][0]=="jnz":
					lst[target][0]="cpy"
				elif lst[target][0]=="inc":
					lst[target][0]="dec"
				else :
					lst[target][0]="inc"


	return dic['a']

print main()
print time.time()-begin