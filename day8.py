no_row,no_col=6,50
lst=[[0 for i in xrange(no_col)] for j  in xrange(no_row)]

def rect(width,height):
	for i in xrange(height):
		for j in xrange(width):
			lst[i][j]=1

def row(row_no,num_by):
	ll=[0 for i in xrange(no_col)]
	for i in xrange(no_col):
		ll[(num_by+i)%no_col]=lst[row_no][i]
	# lst[row_no]=ll[:]
	for i in xrange(no_col):
		lst[row_no][i]=ll[i]

def col(col_no,num_by):
	ll2=[0 for i in xrange(no_row)]
	for i in xrange(no_row):
		ll2[(num_by+i)%no_row]=lst[i][col_no]
	for i in xrange(no_row):
		lst[i][col_no]=ll2[i]


def main():
	f=open('day8.txt','r')
	for i in xrange(173):
		inp=f.readline().strip().split(" ")
		if inp[0]=="rect":
			rr=inp[1].split("x")
			rect(int(rr[0]),int(rr[1]))
		else:
			rr=inp[2].split("=")
			if inp[1]=="row":
				row(int(rr[1]),int(inp[4]))
			else : col(int(rr[1]),int(inp[4]))

	count=0
	for i in xrange(no_row):
		count+=sum(lst[i])
	return count

print main()

# ----------------part 2
for i in xrange(no_row):
	for j in xrange(no_col):
		if lst[i][j]==0: lst[i][j]="'"
		else : lst[i][j]="@"

for i in xrange(no_row):
	print lst[i]