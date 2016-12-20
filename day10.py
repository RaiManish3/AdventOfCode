import time
begin =time.time()

###################################################################
# =============EXECUTION TIME: PT1::4ms PT2::6ms====================

num1,num2=61,17
bot=-1
out=[0,0,0]

def up_list(lst,rr,cur_ind):
	global bot,num1,num2
	if rr[2]>-1:
		if lst[rr[2]][1]==-1:
			lst[rr[2]][1]=rr[0]
		elif rr[0]<lst[rr[2]][1]:
			tmp=lst[rr[2]][1]
			lst[rr[2]][1]=rr[0]
			lst[rr[2]][2]=tmp
		else : 
			lst[rr[2]][2]=rr[0]

	if rr[3]>-1:
		if lst[rr[3]][1]==-1:
			lst[rr[3]][1]=rr[1]	
		elif rr[1]<lst[rr[3]][1]:
			tmp=lst[rr[3]][1]
			lst[rr[3]][1]=rr[1]
			lst[rr[3]][2]=tmp
		else : lst[rr[3]][2]=rr[1]

	# output
	if rr[2] in [-100,-200,-300]:
		out[(rr[2]*-1)/100-1]=rr[0]
	if rr[3] in [-100,-200,-300]:
		out[(rr[3]*-1)/100-1]=rr[1]

	if [num2,num1]==lst[rr[2]][1:3]:
		bot=rr[2]
	elif [num2,num1]==lst[rr[3]][1:3]:
		bot=rr[3]
	elif [num2,num1]==lst[cur_ind][1:3]:
		bot=cur_ind

	for i in xrange(5):
		lst[cur_ind][i]=-1

# for part 1-------------------
def clear_all(lst):
	index=0
	modulo=300
	count=0
	global bot
	ref=[-1 for i in xrange(5)]
	while 1:
		if lst[index]==ref:
			count+=1
		else : count=0
		# -----pt1----
		# if bot>-1:
		# 	return bot
		if count==300:
			return -1
		if -1 not in lst[index][1:]:
			up_list(lst,lst[index][1:],index)
		index=(index+1)%modulo

def main():
	global bot
	lst=[[-1 for i in xrange(5)] for i in xrange(300)]
	f=open('day10.txt','r')
	for i in xrange(231):
		ll=f.readline().strip().split(' ')
		if ll[0]=="bot":
			if ll[5]=="bot":
				lst[int(ll[1])][3]=int(ll[6])
			else :
				if int(ll[6]) in [0,1,2]:
					lst[int(ll[1])][3]=-100*(int(ll[6])+1) 
				else : lst[int(ll[1])][3]=-10

			if ll[10]=="bot":
				lst[int(ll[1])][4]=int(ll[11])
			else : 
				if int(ll[11]) in [0,1,2]:
					lst[int(ll[1])][3]=-100*(int(ll[11])+1)
				else : lst[int(ll[1])][4]=-10

			if -1 not in lst[int(ll[1])][1:]:
				up_list(lst,lst[int(ll[1])][1:],int(ll[1]))

		else :
			if lst[int(ll[5])][1]==-1:
				lst[int(ll[5])][1]=int(ll[1])
			elif int(ll[1])<lst[int(ll[5])][1]:
				tmp=lst[int(ll[5])][1]
				lst[int(ll[5])][1]=int(ll[1])
				lst[int(ll[5])][2]=tmp
			else : 
				lst[int(ll[5])][2]=int(ll[1])
			if -1 not in lst[int(ll[5])][1:]:
				up_list(lst,lst[int(ll[5])][1:],int(ll[5]))

	return clear_all(lst)
		

 
# print main()
# ----------part 2-----------
# print out
# print out[0]*out[1]*out[2]
print time.time()-begin