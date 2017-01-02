import time
begin =time.time()

"""
	HAVEN'T FOUND A BETTER SOLUTION TO THIS PROBLEM. BASICALLY WHAT I DID IS COMPUTING THE
	DISTANCES BETWEEN ALL PAIR OF VERTICES USING DJIKSTRA'S ALGORITHM AND THEN CREATING ALL PERMUTATINS
	FOR THE PATH.
"""

locations = {}
lst, ngbr = [], []
row_max,col_max=0,0
dollar = 10**6

def main():
	global row_max,col_max
	f=open('day24.txt','r')
	size=43
	# upto 7 : total 8 elements
	row_max = size

	for i in xrange(size):
		strx = f.readline().strip()
		# store the locations of number
		if '0' in strx:
			locations['0']=[i,strx.find('0')]
		if '1' in strx:
			locations['1']=[i,strx.find('1')]
		if '2' in strx:
			locations['2']=[i,strx.find('2')]
		if '3' in strx:
			locations['3']=[i,strx.find('3')]
		if '4' in strx:
			locations['4']=[i,strx.find('4')]
		if '5' in strx:
			locations['5']=[i,strx.find('5')]
		if '6' in strx:
			locations['6']=[i,strx.find('6')]
		if '7' in strx:
			locations['7']=[i,strx.find('7')]
		lst.append(list(strx))

	col_max =len(lst[0])

	dis_dic = {('0','1'):djikstra(locations['0'],locations['1']),('0','2'):djikstra(locations['0'],locations['2']),
				('0','3'):djikstra(locations['0'],locations['3']),('0','4'):djikstra(locations['0'],locations['4']),
				('0','5'):djikstra(locations['0'],locations['5']),('0','6'):djikstra(locations['0'],locations['6']),
				('0','7'):djikstra(locations['0'],locations['7']),('1','2'):djikstra(locations['1'],locations['2']),
				('1','3'):djikstra(locations['1'],locations['3']),('1','4'):djikstra(locations['1'],locations['4']),
				('1','5'):djikstra(locations['1'],locations['5']),('1','6'):djikstra(locations['1'],locations['6']),
				('1','7'):djikstra(locations['1'],locations['7']),('2','3'):djikstra(locations['2'],locations['3']),
				('2','4'):djikstra(locations['2'],locations['4']),('2','5'):djikstra(locations['2'],locations['5']),
				('2','6'):djikstra(locations['2'],locations['6']),('2','7'):djikstra(locations['2'],locations['7']),
				('3','4'):djikstra(locations['3'],locations['4']),('3','5'):djikstra(locations['3'],locations['5']),
				('3','6'):djikstra(locations['3'],locations['6']),('3','7'):djikstra(locations['3'],locations['7']),
				('4','5'):djikstra(locations['4'],locations['5']),('4','6'):djikstra(locations['4'],locations['6']),
				('4','7'):djikstra(locations['4'],locations['7']),('5','6'):djikstra(locations['5'],locations['6']),
				('5','7'):djikstra(locations['5'],locations['7']),('6','7'):djikstra(locations['6'],locations['7']),
				}

	# create configurations
	ll = ['1','2','3','4','5','6','7']
	min_config = []
	min_dis = 10**6
	z_config = []

	# total permuations 7! = 5040
	for x1 in xrange(7):
		for x2 in xrange(7):
			if x2 == x1 : continue
			for x3 in xrange(7):
				if x3 ==x1 or x3==x2:continue
				for x4 in xrange(7):
					if x4 ==x1 or x4==x2 or x4==x3:continue
					for x5 in xrange(7):
						if x5==x1 or x5==x2 or x5==x3 or x5==x4:continue
						for x6 in xrange(7):
							if x6==x1 or x6==x2 or x6==x3 or x6==x4 or x6==x5:continue
							z_config.append(['0',ll[x1],ll[x2],ll[x3],ll[x4],ll[x5],ll[x6],ll[21-(x1+x2+x4+x3+x5+x6)]])


	part2 = False

	for i in xrange(5040):
		this_dis = 0
		for j in xrange(7):
			lower = min(z_config[i][j],z_config[i][j+1])
			high = max(z_config[i][j],z_config[i][j+1])	
			this_dis+=dis_dic[(lower,high)]
		if part2:
			this_dis+=dis_dic[('0',z_config[i][-1])]
		if this_dis<min_dis:
			min_dis=this_dis
			min_config = z_config[i]

	print min_dis
	print min_config					



def distance(cell,dest):
	return abs(dest[0]-cell[0])+abs(dest[1]-cell[1])

def makengbr(source):
	global row_max,col_max
	i,j = source[0],source[1]
	del ngbr[:]
	if i>1 and lst[i-1][j]!='#':
		ngbr.append([i-1,j])
	if i+1<row_max and lst[i+1][j]!='#':
		ngbr.append([i+1,j])
	if j>1 and lst[i][j-1]!='#':
		ngbr.append([i,j-1])
	if j+1<col_max and lst[i][j+1]!='#':
		ngbr.append([i,j+1])

def djikstra(source,dest):
	dis_list = []
	visited = []
	dis_list.append([0,source[0],source[1]])	

	while True:
		dis_list.sort()
		s = dis_list.pop(0)
		visited.append(s[1:3])
		makengbr(s[1:3])

		if s[1:3]==dest:
			return s[0]

		for y in ngbr:
			# if visited:: skip
			if y in visited:
				continue
			flag = True
			# already in dis_list
			for k in dis_list:
				if k[1:3]==y:
					if k[0]>s[0]+1:
						k[0]=s[0]+1
					flag = False

			# new to the list
			if flag:
				dis_list.append([s[0]+1,y[0],y[1]])

main()
print time.time()-begin