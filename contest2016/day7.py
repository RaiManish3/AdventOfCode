import time
begin=time.time()

##################################################################################
# ============================EXECUTION TIME : 47ms===============================

def main():
	f=open('day7.txt','r')
	count=0
	for i in xrange(2000):
		lst=f.readline().strip().split('[')
		for x in xrange(len(lst)):
			if ']' in lst[x]:
				lst.insert(x,lst[x][:lst[x].index(']')])
				x+=1
				lst[x]=lst[x][lst[x].index(']')+1:]

		if ']' in lst[-1]:
			x=len(lst)-1
			lst.insert(x,lst[x][:lst[x].index(']')])
			x+=1
			lst[x]=lst[x][lst[x].index(']')+1:]


		# -------------P1-----------------
		# print lst
		# check pattern
		# tls=False

		flag=False
		l=len(lst)

		#---------------------Part 1----------------------
		# for x in xrange(l):
			# if x%2==0:
			# 	for y in xrange(len(lst[x])-3):
			# 		if(lst[x][y]==lst[x][y+3]):
			# 			if(lst[x][y+1]==lst[x][y+2]):
			# 				if(lst[x][y]!=lst[x][y+1]):
			# 					tls=True

			# else:
			# 	for y in xrange(len(lst[x])-3):
			# 		if(lst[x][y]==lst[x][y+3]):
			# 			if(lst[x][y+1]==lst[x][y+2]):
			# 				if(lst[x][y]!=lst[x][y+1]):
			# 					tls=False
			# 					flag=True

			# x+=1
			# if flag==True:
			# 	break

		l1=[lst[y] for y in xrange(0,l,2)]
		l2=[lst[y] for y in xrange(1,l,2)]

		for x in xrange(len(l1)):
			for y in xrange(len(l1[x])-2):
				if(l1[x][y]==l1[x][y+2] and l1[x][y]!=l1[x][y+1]):
					strx=l1[x][y+1]+l1[x][y]+l1[x][y+1]
					for z in l2:
						if strx in z:
							count+=1
							flag=True
							break
					if flag==True:
						break
			if flag==True:
						break

		# --------------------P1-----------------
		# if tls==True:
		# 	count+=1
		# 	print lst
	return count

print main()
print time.time()-begin