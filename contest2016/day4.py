import operator
import time
begin=time.time()

###################################################################################
# ============================EXECUTION TIME: 60ms=================================

def main():
	f=open('day4.txt','r')
	dic={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,
		'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0,}
	result=0

	for i in xrange(991):
		# input read
		lst=f.readline().strip().split('-')
		ll=lst[-1].split('[')
		lst[-1]=int(ll[0])
		lst.append(ll[1][:-1])
		
		index,count=0,0
		for x in lst:
			if isinstance(x,int):
				index=lst.index(x)
				break

		for x in xrange(index):
			for y in lst[x]:
				dic[y]+=1

		sorted_x=sorted(dic.items(),key=operator.itemgetter(1),reverse=True)
		l=len(sorted_x)
		for x in xrange(l-1):
			if sorted_x[x][1]==sorted_x[x+1][1]:
				if sorted_x[x][0]>sorted_x[x+1][0]:
					tmp=sorted_x[x]
					sorted_x[x]=sorted_x[x+1]
					sorted_x[x+1]=tmp
		# print sorted_x

		for x in xrange(5):
			if sorted_x[x][0] in lst[-1]:
				count+=1

		if count==5:
			result+=lst[index]

			# # =============================PART_2
			steps=lst[index]
			strx=""
			for x in xrange(index):
				for e in xrange(len(lst[x])):
					strx+=chr((ord(lst[x][e])+steps%26+7)%26+97)
				strx+=" " if steps%2 else "-"
			if strx.find("northpole")>-1:
				return lst[index]

			# print strx


		dic=dict.fromkeys(dic,0)

	return result

print main()
print time.time()-begin