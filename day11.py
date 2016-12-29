import copy

lst = [['G1','M1','G2','M2','G3','M3','G4',' ','G5',' '],
		[' ',' ',' ',' ',' ',' ',' ','M4',' ','M5'],
		[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
		[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']]
size=10
min_steps=1000

# lst = [[' ','M1',' ','M2'],['G1',' ',' ',' '],[' ',' ','G2',' '],[' ',' ',' ',' ']]
# size=4

iterations=0
configurations=[]
wrong_configs=[]
configurations.append(copy.deepcopy(lst))

def print_list():
	for i in xrange(1,5):
		print lst[4-i]
	print "--------------------------------------------------------------"

def alone(floor):
	global size
	if floor==3: return False
	for i in xrange(0,size,2):
		if lst[0][i]!=' ' and lst[3][i+1]!=' ':
			return True

	noG,noC=0,0
	if floor==2:
		for i in xrange(size):
			if lst[floor][i]!=' ':
				if i%2:
					noC+=1
				else :
					noG+=1

		if (noG==0 and noC==size/2) or (noG==size/2 and noC==0):
			return True

	return False


def corres(floor):
	global size
	isGen =False
	for i in xrange(0,size,2):
		if lst[floor][i]!=' ':
			isGen=True
			break
	if not isGen:
		return False

	for i in xrange(1,size,2):
		if lst[floor][i]!=' ' and lst[floor][i-1]==' ':
			return True
	return False

def new_config(index1,index2,floor,isOne,dirn,rever):
	if dirn=="up":
		if not rever:
			lst[floor+1][index1]=lst[floor][index1]
			lst[floor][index1] = ' '
			if not isOne:
				lst[floor+1][index2]=lst[floor][index2]
				lst[floor][index2] = ' '

		else :
			lst[floor][index1]=lst[floor+1][index1]
			lst[floor+1][index1]=' '
			if not isOne:
				lst[floor][index2]=lst[floor+1][index2]		
				lst[floor+1][index2]=' '		

	elif dirn=="down":
		if not rever:
			lst[floor-1][index1]=lst[floor][index1]
			lst[floor][index1] = ' '
			if not isOne:
				lst[floor-1][index2]=lst[floor][index2]
				lst[floor][index2] = ' '

		else :
			lst[floor][index1]=lst[floor-1][index1]
			lst[floor-1][index1]=' '
			if not isOne:
				lst[floor][index2]=lst[floor-1][index2]		
				lst[floor-1][index2]=' '


def move(floor,steps):
	global iterations,min_steps,size
	iterations+=1

	# out of bounds
	if floor<0 or floor>3 or steps>=min_steps:return

	# invalid moves
	if alone(floor) or corres(floor):
		wrong_configs.append(copy.deepcopy(lst))
		return

	# the required ones
	if floor==3 and ' ' not in lst[3]:
		min_steps = steps
		print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
		return

	print iterations, steps, min_steps
	# print_list()

	# UP-------------------------------

	if floor<3:
		# move two chips
		for i in xrange(1,size,2):
			for j in xrange(i+2,size,2):
				if lst[floor][i]!=' ' and lst[floor][j]!=' ':
					# new config
					new_config(i,j,floor,False,"up",False)

					if lst not in configurations and lst not in wrong_configs:
						configurations.append(copy.deepcopy(lst))
						move(floor+1,steps+1)
						configurations.pop(-1)

					# revert config
					new_config(i,j,floor,False,"up",True)


		# move two gens
		for i in xrange(0,size,2):
			for j in xrange(i+2,size,2):
				if lst[floor][i]!=' ' and lst[floor][j]!=' ':
					# new config
					new_config(i,j,floor,False,"up",False)

					if lst not in configurations and lst not in wrong_configs:
						configurations.append(copy.deepcopy(lst))
						move(floor+1,steps+1)
						configurations.pop(-1)

					new_config(i,j,floor,False,"up",True)
		

		# move gen-chip
		for i in xrange(0,size,2):
			if lst[floor][i]!=' ' and lst[floor][i+1]!=' ':
				# new config
				new_config(i,i+1,floor,False,"up",False)

				if lst not in configurations and lst not in wrong_configs:
					configurations.append(copy.deepcopy(lst))
					move(floor+1,steps+1)
					configurations.pop(-1)

				new_config(i,i+1,floor,False,"up",True)

		# move one chip
		for i in xrange(1,size,2):
			if lst[floor][i]!=' ':
				new_config(i,-1,floor,True,"up",False)

				if lst not in configurations and lst not in wrong_configs:
					configurations.append(copy.deepcopy(lst))
					move(floor+1,steps+1)
					configurations.pop(-1)

				new_config(i,-1,floor,True,"up",True)


		# move one gen
		for i in xrange(0,size,2):
			if lst[floor][i]!=' ':
				new_config(i,-1,floor,True,"up",False)

				if lst not in configurations and lst not in wrong_configs:
					configurations.append(copy.deepcopy(lst))
					move(floor+1,steps+1)
					configurations.pop(-1)

				new_config(i,-1,floor,True,"up",True)


	# DOWN -------------------------------------------
	if floor>0:

		# move one chip
		for i in xrange(1,size,2):
			if lst[floor][i]!=' ':
				new_config(i,-1,floor,True,"down",False)

				if lst not in configurations and lst not in wrong_configs:
					configurations.append(copy.deepcopy(lst))
					move(floor-1,steps+1)
					configurations.pop(-1)

				new_config(i,-1,floor,True,"down",True)

		# move one gen
		for i in xrange(0,size,2):
			if lst[floor][i]!=' ':
				new_config(i,-1,floor,True,"down",False)

				if lst not in configurations and lst not in wrong_configs:
					configurations.append(copy.deepcopy(lst))
					move(floor-1,steps+1)
					configurations.pop(-1)

				new_config(i,-1,floor,True,"down",True)

		# move two chips
		for i in xrange(1,size,2):
			for j in xrange(i+2,size,2):
				if lst[floor][i]!=' ' and lst[floor][j]!=' ':
					# new config
					new_config(i,j,floor,False,"down",False)

					if lst not in configurations and lst not in wrong_configs:
						configurations.append(copy.deepcopy(lst))
						move(floor-1,steps+1)
						configurations.pop(-1)

					# revert config
					new_config(i,j,floor,False,"down",True)


		# move two gens
		for i in xrange(0,size,2):
			for j in xrange(i+2,size,2):
				if lst[floor][i]!=' ' and lst[floor][j]!=' ':
					# new config
					new_config(i,j,floor,False,"down",False)

					if lst not in configurations and lst not in wrong_configs:
						configurations.append(copy.deepcopy(lst))
						move(floor-1,steps+1)
						configurations.pop(-1)

					new_config(i,j,floor,False,"down",True)
		

		# move gen-chip
		for i in xrange(0,size,2):
			if lst[floor][i]!=' ' and lst[floor][i+1]!=' ':
				# new config
				new_config(i,i+1,floor,False,"down",False)

				if lst not in configurations and lst not in wrong_configs:
					configurations.append(copy.deepcopy(lst))
					move(floor-1,steps+1)
					configurations.pop(-1)

				new_config(i,i+1,floor,False,"down",True)

move(0,0)
print min_steps