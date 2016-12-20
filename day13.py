import time
begin=time.time()

#####################################################################################################

# puzzle input------> 1364
lst=[]
size=100
fav_n=1364
t_x,t_y=31,39

# TEST INPUT
# t_x,t_y=7,4
# fav_n=10
# size=10

min_steps=100000
l=0
part1=False
his=[]

def print_lst():
	for i in xrange(size):
		print lst[i]

def ps(x,y):
	return x*x+3*x+2*x*y+y+y*y

def move(visited,c_x,c_y,steps):
	global min_steps,t_x,t_y,size

	# PART 1
	if steps>=min_steps and part1==True:
		return
	if c_x==t_x and c_y==t_y and part1==True:
		if steps<min_steps:
			min_steps=steps
		return
	
	# PART 2
	if part1==False and steps>50:
		return

	if part1==False and steps<=50:
		if [c_y,c_x] not in his:
			his.append([c_y,c_x])


	# check neighbours
	# right column
	if c_x+1<size and lst[c_y][c_x+1]==1 and [c_y,c_x+1] not in visited:
		visited.append([c_y,c_x+1])
		move(visited,c_x+1,c_y,steps+1)
		visited.pop(-1)

	# down row
	if c_y+1<size and lst[c_y+1][c_x]==1 and [c_y+1,c_x] not in visited:
		visited.append([c_y+1,c_x])
		move(visited,c_x,c_y+1,steps+1)
		visited.pop(-1)

	# up row
	if c_y-1>-1 and lst[c_y-1][c_x]==1 and [c_y-1,c_x] not in visited:
		visited.append([c_y-1,c_x])
		move(visited,c_x,c_y-1,steps+1)
		visited.pop(-1)

	# left column
	if c_x-1>-1 and lst[c_y][c_x-1]==1 and [c_y,c_x-1] not in visited:
		visited.append([c_y,c_x-1])
		move(visited,c_x-1,c_y,steps+1)
		visited.pop(-1)

def main():
	# making the maze
	global size
	for i in xrange(size):
		ll=[]
		for j in xrange(size):
			binary=bin(ps(j,i)+fav_n)[2:].strip()
			ones=0
			for k in binary:
				if k=='1':
					ones+=1
			ll.append(0 if (ones%2) else 1)
		lst.append(ll[:])
	# print_lst()

	# the move
	# initial at (1,1)
	move([],1,1,0)

main()
if part1:
	print min_steps
else : print len(his)
print time.time()-begin