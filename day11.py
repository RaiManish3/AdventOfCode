import copy

lst = [['G1','M1','G2','M2','G3','M3','G4',' ','G5',' '],
		[' ',' ',' ',' ',' ',' ',' ','M4',' ','M5'],
		[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
		[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']]
size=10


dic={'G1':[-1,-1,False],'M1':[-1,-1,False],'G2':[-1,-1,False],'M2':[-1,-1,False],'G3':[-1,-1,False],'M3':[-1,-1,False],'G4':[-1,-1,False],'M4':[-1,-1,False],'G5':[-1,-1,False],'M5':[-1,-1,False]}

min_steps=1000

# lst = [[' ','M1',' ','M2'],['G1',' ',' ',' '],[' ',' ','G2',' '],[' ',' ',' ',' ']]
# size=4
count=0

def print_list():
	for i in xrange(4):
		print lst[i]
	print "--------------------------------------------------------------"


def alone(floor,dirn):
	count1=0
	for i in xrange(0,size,1):
		if lst[floor][i]!=' ':
			count1+=1
	ck=0
	x=4 if dirn=="up" else -1
	inc=1 if x==4 else -1
	for i in xrange(floor+inc,x,inc):
		if ' ' not in lst[i]:
			return False
		else : 
			ck+=1

	if count1==1 and ck==x-floor-inc:
		return True
	return False


def chk_affected(floor,gen,f_old):
	if f_old==-1:
		for i in xrange(1,size,2):
			if lst[floor][i]!=' ' and lst[floor][i-1]==' ':
				return True

	else :
		if lst[f_old][lst[floor].index(gen)+1]!=' ':
			for i in xrange(0,size,2):
				if 'G' in lst[f_old][i]:
					return True

	return False




def no_Gpresent(floor):
	for i in xrange(0,size,2):
		if 'G' in lst[floor][i]:
			return False
	return True

def chk_cor_present(floor,chip):
	index=lst[floor].index(chip)
	if lst[floor][index-1]==' ':
		return False
	return True



def chk_conditions(gen1,gen2,chip1,chip2,floor,dirn):
	if gen1!=False:
		if chk_affected(floor,gen1,-1) or (dirn=="up" and chk_affected(floor,gen1,floor-1)) or (dirn=="down" and chk_affected(floor,gen1,floor+1)) or alone(floor,dirn):
			return False

	if gen2!=False:
		if chk_affected(floor,gen2,-1) or (dirn=="up" and chk_affected(floor,gen2,floor-1)) or (dirn=="down" and chk_affected(floor,gen2,floor+1)) or alone(floor,dirn):
			return False

	if chip1!=False:
		if not (no_Gpresent(floor) or chk_cor_present(floor,chip1)) or alone(floor,dirn):
			return False

	if chip2!=False:
		if not (no_Gpresent(floor) or chk_cor_present(floor,chip2)) or alone(floor,dirn):
			return False
	return True


def move(gen1,gen2,chip1,chip2,steps,floor,dirn):
	global min_steps,count
	if count>10000000:return
	count+=1

	# end-of-recursion case
	if floor>3 or floor<0 or steps>=min_steps:return

	if floor==3 and ' ' not in lst[floor]:
		min_steps=min(min_steps,steps)
		print min_steps,"**************************************************************************************************************************************************"
		return

	# conditions on move
	if gen1!='G' and not chk_conditions(gen1,gen2,chip1,chip2,floor,dirn):
		return

	# next move
	# print "#concrete step"
	# print_list()
	# print count,floor,steps

	# move single chip
	for i in xrange(1,size,2):
		if lst[floor][i]==' ':
			continue

		# move up
		if dic[lst[floor][i]][:2]!=[floor+1,floor] or dic[lst[floor][i]][2]==True:
			if floor<3:
				x,y,t=dic[lst[floor][i]][0],dic[lst[floor][i]][1],dic[lst[floor][i]][2]
				dic[lst[floor][i]]=[floor,floor+1,False]
				lst[floor+1][i]=lst[floor][i]
				lst[floor][i]=' '
				move(False,False,lst[floor+1][i],False,steps+1,floor+1,"up")
				lst[floor][i]=lst[floor+1][i]
				lst[floor+1][i]=' '
				dic[lst[floor][i]]=[x,y,t]

	# # move gen1
	# for i in xrange(0,size,2):
	# 	if lst[floor][i]==' ':
	# 		continue

	# 	# move up
	# 	if dic[lst[floor][i]][:2]!=[floor+1,floor] or dic[lst[floor][i]][2]==True:
	# 		if floor<3:
	# 			x,y,t=dic[lst[floor][i]][0],dic[lst[floor][i]][1],dic[lst[floor][i]][2]
	# 			dic[lst[floor][i]]=[floor,floor+1,False]
	# 			lst[floor+1][i]=lst[floor][i]
	# 			lst[floor][i]=' '
	# 			move(lst[floor+1][i],False,False,False,steps+1,floor+1,"up")
	# 			lst[floor][i]=lst[floor+1][i]
	# 			lst[floor+1][i]=' '
	# 			dic[lst[floor][i]]=[x,y,t]

	#move 2chips
	for i in xrange(1,size,2):
		if lst[floor][i]==' ':
			continue
		for j in xrange(i+2,size,2):
			if lst[floor][j]==' ':
				continue

			# move up
			if not (dic[lst[floor][i]][:2]==[floor+1,floor] and dic[lst[floor][j]][:2]==[floor+1,floor]) or (dic[lst[floor][i]][2]==False and dic[lst[floor][j]][2]==False):
				if floor<3:
					x1,y1,t1=dic[lst[floor][i]][0],dic[lst[floor][i]][1],dic[lst[floor][i]][2]
					dic[lst[floor][i]]=[floor,floor+1,True]
					x2,y2,t2=dic[lst[floor][j]][0],dic[lst[floor][j]][1],dic[lst[floor][j]][2]
					dic[lst[floor][j]]=[floor,floor+1,True]

					lst[floor+1][i]=lst[floor][i]
					lst[floor][i]=' '
					lst[floor+1][j]=lst[floor][j]
					lst[floor][j]=' '

					move(False,False,lst[floor+1][i],lst[floor+1][j],steps+1,floor+1,"up")

					lst[floor][i]=lst[floor+1][i]
					lst[floor+1][i]=' '
					lst[floor][j]=lst[floor+1][j]
					lst[floor+1][j]=' '

					dic[lst[floor][i]]=[x1,y1,t1]
					dic[lst[floor][j]]=[x2,y2,t2]


	#move 2gens
	for i in xrange(0,size,2):
		if lst[floor][i]==' ':
			continue
		for j in xrange(i+2,size,2):
			if lst[floor][j]==' ':
				continue

			# move up
			if not (dic[lst[floor][i]][:2]==[floor+1,floor] and dic[lst[floor][j]][:2]==[floor+1,floor]) or (dic[lst[floor][i]][2]==False and dic[lst[floor][j]][2]==False):
				if floor<3:
					x1,y1,t1=dic[lst[floor][i]][0],dic[lst[floor][i]][1],dic[lst[floor][i]][2]
					dic[lst[floor][i]]=[floor,floor+1,True]
					x2,y2,t2=dic[lst[floor][j]][0],dic[lst[floor][j]][1],dic[lst[floor][j]][2]
					dic[lst[floor][j]]=[floor,floor+1,True]

					lst[floor+1][i]=lst[floor][i]
					lst[floor][i]=' '
					lst[floor+1][j]=lst[floor][j]
					lst[floor][j]=' '
					move(lst[floor+1][i],lst[floor+1][j],False,False,steps+1,floor+1,"up")
					lst[floor][i]=lst[floor+1][i]
					lst[floor+1][i]=' '
					lst[floor][j]=lst[floor+1][j]
					lst[floor+1][j]=' '

					dic[lst[floor][i]]=[x1,y1,t1]
					dic[lst[floor][j]]=[x2,y2,t2]

	#move gen-chip
	for i in xrange(0,size,2):
		if lst[floor][i]==' ' or lst[floor][i+1]==' ':
			continue
		# move up
		if not (dic[lst[floor][i]][:2]==[floor+1,floor] and dic[lst[floor][i+1]][:2]==[floor+1,floor]) or (dic[lst[floor][i]][2]==False and dic[lst[floor][i+1]][2]==False):
			if floor<3:
				x1,y1,t1=dic[lst[floor][i]][0],dic[lst[floor][i]][1],dic[lst[floor][i]][2]
				dic[lst[floor][i]]=[floor,floor+1,True]
				x2,y2,t2=dic[lst[floor][i+1]][0],dic[lst[floor][i+1]][1],dic[lst[floor][i+1]][2]
				dic[lst[floor][i+1]]=[floor,floor+1,True]

				lst[floor+1][i]=lst[floor][i]
				lst[floor][i]=' '
				lst[floor+1][i+1]=lst[floor][i+1]
				lst[floor][i+1]=' '
				move(lst[floor+1][i],False,lst[floor+1][i+1],False,steps+1,floor+1,"up")
				lst[floor][i]=lst[floor+1][i]
				lst[floor+1][i]=' '
				lst[floor][i+1]=lst[floor+1][i+1]
				lst[floor+1][i+1]=' '

				dic[lst[floor][i]]=[x1,y1,t1]
				dic[lst[floor][i+1]]=[x2,y2,t2]


		# move chip1
		# move down
	for i in xrange(1,size,2):
		if lst[floor][i]==' ':
			continue
		if dic[lst[floor][i]][:2]!=[floor-1,floor] or dic[lst[floor][i]][2]==True:		
			if floor>0 :
				x,y,t=dic[lst[floor][i]][0],dic[lst[floor][i]][1],dic[lst[floor][i]][2]
				dic[lst[floor][i]]=[floor,floor-1,False]
				lst[floor-1][i]=lst[floor][i]
				lst[floor][i]=' '
				move(False,False,lst[floor-1][i],False,steps+1,floor-1,"down")
				lst[floor][i]=lst[floor-1][i]
				lst[floor-1][i]=' '
				dic[lst[floor][i]]=[x,y,t]

	
	# move gen1
	# for i in xrange(0,size,2):
	# 	if lst[floor][i]==' ':
	# 		continue
	# 	# move down
	# 	if dic[lst[floor][i]][:2]!=[floor-1,floor] or dic[lst[floor][i]][2]==True:
	# 		if floor>0:
	# 			x,y,t=dic[lst[floor][i]][0],dic[lst[floor][i]][1],dic[lst[floor][i]][2]
	# 			dic[lst[floor][i]]=[floor,floor-1,False]
	# 			lst[floor-1][i]=lst[floor][i]
	# 			lst[floor][i]=' '
	# 			move(lst[floor-1][i],False,False,False,steps+1,floor-1,"down")
	# 			lst[floor][i]=lst[floor-1][i]
	# 			lst[floor-1][i]=' '
	# 			dic[lst[floor][i]]=[x,y,t]


	# # move 2gens
	# 	# move down
	# for i in xrange(0,size,2):
	# 	if lst[floor][i]==' ':
	# 		continue
	# 	for j in xrange(i+2,size,2):
	# 		if lst[floor][j]==' ':
	# 			continue

	# 		if not (dic[lst[floor][i]][:2]==[floor-1,floor] and dic[lst[floor][j]][:2]==[floor-1,floor]):
	# 			if floor>0:
	# 				x1,y1,t1=dic[lst[floor][i]][0],dic[lst[floor][i]][1],dic[lst[floor][i]][2]
	# 				dic[lst[floor][i]]=[floor,floor-1,True]
	# 				x2,y2,t2=dic[lst[floor][j]][0],dic[lst[floor][j]][1],dic[lst[floor][j]][2]
	# 				dic[lst[floor][j]]=[floor,floor-1,True]

	# 				lst[floor-1][i]=lst[floor][i]
	# 				lst[floor][i]=' '
	# 				lst[floor-1][j]=lst[floor][j]
	# 				lst[floor][j]=' '
	# 				move(lst[floor-1][i],lst[floor-1][j],False,False,steps+1,floor-1,"down")
	# 				lst[floor][i]=lst[floor-1][i]
	# 				lst[floor-1][i]=' '
	# 				lst[floor][j]=lst[floor-1][j]
	# 				lst[floor-1][j]=' '

	# 				dic[lst[floor][i]]=[x1,y1,t1]
	# 				dic[lst[floor][j]]=[x2,y2,t2]

	# 	# move 2chips
	# 		# move down
	# for i in xrange(1,size,2):
	# 	if lst[floor][i]==' ':
	# 		continue
	# 	for j in xrange(i+2,size,2):
	# 		if lst[floor][j]==' ':
	# 			continue

	# 		if not (dic[lst[floor][i]][:2]==[floor-1,floor] and dic[lst[floor][j]][:2]==[floor-1,floor]):
	# 			if floor>0 :
	# 				x1,y1,t1=dic[lst[floor][i]][0],dic[lst[floor][i]][1],dic[lst[floor][i]][2]
	# 				dic[lst[floor][i]]=[floor,floor-1,True]
	# 				x2,y2,t2=dic[lst[floor][j]][0],dic[lst[floor][j]][1],dic[lst[floor][j]][2]
	# 				dic[lst[floor][j]]=[floor,floor-1,True]

	# 				lst[floor-1][i]=lst[floor][i]
	# 				lst[floor][i]=' '
	# 				lst[floor-1][j]=lst[floor][j]
	# 				lst[floor][j]=' '
	# 				move(False,False,lst[floor-1][i],lst[floor-1][j],steps+1,floor-1,"down")
	# 				lst[floor][i]=lst[floor-1][i]
	# 				lst[floor-1][i]=' '
	# 				lst[floor][j]=lst[floor-1][j]
	# 				lst[floor-1][j]=' '

	# 				dic[lst[floor][i]]=[x1,y1,t1]
	# 				dic[lst[floor][j]]=[x2,y2,t2]

	# # move gen-chip
	# 	# move down
	# for i in xrange(0,size,2):
	# 	if lst[floor][i]==' ' or lst[floor][i+1]==' ':
	# 		continue
	# 	if not (dic[lst[floor][i]][:2]==[floor-1,floor] and dic[lst[floor][i+1]][:2]==[floor-1,floor]):
	# 		if floor>0 :
	# 			x1,y1,t1=dic[lst[floor][i]][0],dic[lst[floor][i]][1],dic[lst[floor][i]][2]
	# 			dic[lst[floor][i]]=[floor,floor-1,True]
	# 			x2,y2,t2=dic[lst[floor][i+1]][0],dic[lst[floor][i+1]][1],dic[lst[floor][i+1]][2]
	# 			dic[lst[floor][i+1]]=[floor,floor-1,True]

	# 			lst[floor-1][i]=lst[floor][i]
	# 			lst[floor][i]=' '
	# 			lst[floor-1][i+1]=lst[floor][i+1]
	# 			lst[floor][i+1]=' '
	# 			move(lst[floor-1][i],False,lst[floor-1][i+1],False,steps+1,floor-1,"down")
	# 			lst[floor][i]=lst[floor-1][i]
	# 			lst[floor-1][i]=' '
	# 			lst[floor][i+1]=lst[floor-1][i+1]
	# 			lst[floor-1][i+1]=' '

	# 			dic[lst[floor][i]]=[x1,y1,t1]
				# dic[lst[floor][i+1]]=[x2,y2,t2]



move('G',False,False,False,0,0,"down")
print "min_steps = ", min_steps
print "count = ", count