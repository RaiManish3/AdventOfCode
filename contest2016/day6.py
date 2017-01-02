
lst=[[0 for i in xrange(26)] for j in xrange(8)]

def main():
	f=open('day6.txt','r')
	for i in xrange(598):
		strx=f.readline().strip()
		for j in xrange(len(strx)):
			lst[j][ord(strx[j])-97]+=1
	# ll=[chr(lst[i].index(max(lst[i]))+97) for i in xrange(8)]
	ll=[]
	for i in xrange(8):
		while 1:
			m=min(lst[i])
			if m>0:
				ll.append(chr(lst[i].index(m)+97))
				break
			else : lst[i].remove(lst[i].index(m))
	return ll

print main()

