# ---------------------PART 2 NOT YET WORKING

import copy
lst = []
used, avail = [],[]
min_steps = 1000
x_max,y_max =34,28
# x_max,y_max =2,2
t_index = [0,0]
visited = []
visited.append([x_max,0])
vis_s=[[27,12]]
# vis_s=[[1,1]]
ngbr=[[33,0],[34,1]]
# ngbr = [[1,0],[2,1]]

f_index = [27,12]
# f_index=[1,1]
d_index = [x_max,0]
free =86
# free =8

def main():
	f=open('day22.txt','r')
	f.readline()
	f.readline()
	ll = []

	for i in xrange(1,1016):
	# for i in xrange(1,10):
		strx = f.readline().strip().split()
		ll.append([int(strx[2][:-1]),int(strx[3][:-1])])
		# used.append([int(strx[2][:-1]),((i-1)/29,(i-1)%29)])
		# avail.append([int(strx[3][:-1]),((i-1)/29,(i-1)%29)])

		if i%29==0:
			lst.append(ll[:])
			del ll[:]

	# used.sort()
	# avail.sort()
	# size=1015
	# vp = 0

	# part 1---------------------
	# for i in  xrange(size):
	# 	count = 1
	# 	for j in xrange(size):
	# 		if used[i][1]==avail[j][1]:
	# 			count=0
	# 		if used[i][0]<=avail[j][0] and used[i][0]!=0:
	# 			vp += size -j-count
	# 			break
		
	# print vp

	#part 2--------------------
	# print lst
	for i in xrange(35):
		for j in xrange(29):
			if i==0 and j ==0 :print "(.)",
			elif i==34 and j==0 : print "G",
			elif i==27 and j==12 : print "@", 
			elif lst[i][j][0]>86:
				print "#",
			else : print ".",
		print
	# recur(0)
	print min_steps

def swap(x_index,y_index):
	# change lst structure and update f_index
	tmp = copy.deepcopy(lst[x_index[0]][x_index[1]])
	lst[x_index[0]][x_index[1]] = copy.deepcopy(lst[y_index[0]][y_index[1]])
	lst[y_index[0]][y_index[1]] = copy.deepcopy(tmp)


def make_ngbr():
	up = d_index[0]-1
	down = d_index[0]+1
	left = d_index[1]-1
	right = d_index[1]+1
	del ngbr[:]

	if up>=0 and [up,d_index[1]]!=f_index:
		ngbr.append([up,d_index[1]])
	if down<=x_max and [down,d_index[1]]!=f_index:
		ngbr.append([down,d_index[1]])
	if left>=0 and [d_index[0],left]!=f_index:
		ngbr.append([d_index[0],left])
	if right<=y_max and [d_index[0],right]!=f_index:
		ngbr.append([d_index[0],right])

flag=False

def recur(steps):
	global min_steps,d_index,f_index,t_index,ngbr,vis_s,flag
	print "*****************************",f_index,d_index,steps, ngbr

	if f_index[1]<3:
		flag=True

	if steps >=min_steps or f_index==d_index or d_index[1]>0 or (flag and f_index[1]>2):
		return
	if d_index == t_index :
		min_steps = steps
		print min_steps
		print "#############################################################################################"
		return

	# make f_index a neighbour
	# if f_index not in ngbr:

	if f_index not in visited and f_index in ngbr:
		# print "------------",f_index,d_index
		# print lst
		x1 =vis_s[:]
		del vis_s[:]
		vis_s.append(f_index[:])
		visited.append(f_index[:])

		swap(f_index,d_index)
		xx = f_index[:]
		f_index = d_index[:]
		d_index = xx[:]
		tmp2 = ngbr[:]
		make_ngbr()

		recur(steps+1)

		visited.pop(-1)
		swap(f_index,d_index)
		d_index = f_index[:]
		f_index = xx[:]
		ngbr = tmp2[:]
		vis_s=x1[:]



	if f_index[0]+1<=x_max and lst[f_index[0]+1][f_index[1]][0]<=free and [f_index[0]+1,f_index[1]] not in vis_s:
		ind = [f_index[0]+1,f_index[1]]
		vis_s.append(ind)
		swap(f_index,ind)
		tmp = f_index[:]
		f_index = ind[:]
		ind = tmp[:]
		recur(steps+1)
		swap(f_index,ind)
		ind = f_index[:]
		f_index = tmp[:]
		vis_s.pop(-1)

	if f_index[1]-1>=0 and lst[f_index[0]][f_index[1]-1][0]<=free and [f_index[0],f_index[1]-1] not in vis_s:
		ind = [f_index[0],f_index[1]-1]
		vis_s.append(ind)
		swap(f_index,ind)
		tmp = f_index[:]
		f_index = ind[:]
		ind = tmp[:]
		recur(steps+1)
		swap(f_index,ind)
		ind = f_index[:]
		f_index = tmp[:]
		vis_s.pop(-1)


	if f_index[0]-1>=0 and lst[f_index[0]-1][f_index[1]][0]<=free and [f_index[0]-1,f_index[1]] not in vis_s:
		x1,y1= f_index[0]-1,f_index[1]
		vis_s.append([x1,y1])
		swap(f_index,[x1,y1])
		x2,y2 = f_index
		f_index = [x1,y1]
		recur(steps+1)
		swap(f_index,[x2,y2])
		f_index = [x2,y2]
		vis_s.pop(-1)

	if f_index[1]+1<=y_max and lst[f_index[0]][f_index[1]+1][0]<=free and [f_index[0],f_index[1]+1] not in vis_s:
		ind = [f_index[0],f_index[1]+1]
		vis_s.append(ind)
		swap(f_index,ind)
		tmp = f_index[:]
		f_index = ind[:]
		ind = tmp[:]
		recur(steps+1)
		swap(f_index,ind)
		ind =f_index[:]
		f_index = tmp[:]
		vis_s.pop(-1)



main()
