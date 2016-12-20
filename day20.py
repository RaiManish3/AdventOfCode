def main():
	limit=4294967295
	lst=[]

	f=open('day20.txt','r')
	size=1005

	for x in xrange(size):
		strx=f.readline().strip().split('-')
		n1 = int(strx[0])
		n2 = int(strx[1])
		
		indicator=True
		for i in xrange(len(lst)):
			ind=False
			# n1 is in a range
			if n1>=lst[i][0] and n1<=lst[i][1]:
				indicator=False
				r1 = lst[i][0]
				for k in xrange(i,len(lst)):
					# n2 is also in a range
					if n2>=lst[k][0] and n2<=lst[k][1]:
						r2 = lst[k][1]
						del lst[i:k+1]
						lst.insert(i,[r1,r2])
						ind=True
						break

					# n2 in between two ranges
					elif n2>=lst[k][1] and (k+1==len(lst) or n2<=lst[k+1][0]):
						r2=n2
						del lst[i:k+1]
						lst.insert(i,[r1,r2])
						ind=True
						break
			if ind:
				break


		if indicator:
			for i in xrange(len(lst)):
				# n2 is in a range
				ind=False
				if n2>=lst[i][0] and n2<=lst[i][1]:
					indicator=False
					r2=lst[i][1]
					for k in xrange(i,-1,-1):
						# n1 is in between two ranges
						if n1<=lst[k][0] and (k-1==-1 or n1>=lst[k-1][0]):
							r1=n1
							del lst[k:i+1]
							lst.insert(k,[r1,r2])
							ind=True
							break

				if ind:
					break					

		if indicator:
			ind=False
			# for when n1 and n2 form a superset of already existing list
			for i in xrange(len(lst)):
				if n1<lst[i][0]:
					for k in xrange(len(lst)-1,i-1,-1):
						if n2>lst[k][1]:
							del lst[i:k+1]
							lst.insert(i,[n1,n2])
							ind = True
							break
				if ind:
					break

			# they are new
			if not ind:
				lst.append([n1,n2])

		# sorting helps reduction is calculation
		lst.sort()

	# print lst
	min_ip=limit
	count=0
	for i in xrange(len(lst)-1):
		if lst[i+1][0]-lst[i][1]>1:
			count+=lst[i+1][0]-lst[i][1]-1
			if min_ip>lst[i][1]+1:
				min_ip=lst[i][1]+1

	print "total ip allowed : ",count+limit-lst[-1][1]
	print "minimum available ip : ",min_ip


main()
