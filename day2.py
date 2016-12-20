import time
begin=time.time()

#############################################################################
# ==========================EXECUTION TIME: 2ms==============================

# index=[1,1]
index=[2,0]
# grid=[[1,2,3],[4,5,6],[7,8,9]]
grid=[['1'],['2','3','4'],['5','6','7','8','9'],['A','B','C'],['D']]
allowed_index=[[0,2],[1,1],[1,2],[1,3],[2,0],[2,1],[2,2],[2,3],[2,4],[3,1],[3,2],[3,3],[4,2]]

def value(index):
	if index[0]==0:
		return grid[0][0]
	if index[0]==1:
		return grid[1][index[1]-1]
	if index[0]==2:
		return grid[2][index[1]]
	if index[0]==3:
		return grid[3][index[1]-1]
	if index[0]==4:
		return grid[4][0]

def main():
	global index
	f=open('day2.txt','r')
	answer=""

	for i in xrange(5):
		lst=list(f.readline())
		lst.pop(-1)
		for e in lst:
			tmp=index[:]
			if e=='L':
				# if index[0]>0:
				# 	index[0]-=1
				tmp[1]-=1
				if tmp in allowed_index:
					index=tmp[:]
			elif e=='R':
				# if index[0]<2:
				# 	index[0]+=1
				tmp[1]+=1
				if tmp in allowed_index:
					index=tmp[:]
			elif e=='U':
				# if index[1]>0:
				# 	index[1]-=1
				tmp[0]-=1
				if tmp in allowed_index:
					index=tmp[:]
			elif e=='D':
				# if index[1]<2:
				# 	index[1]+=1
				tmp[0]+=1
				if tmp in allowed_index:
					index=tmp[:]

		# answer+=str(grid[index[1]][index[0]])
		answer+=value(index)

	return answer

print main()
print time.time()-begin