import time
begin=time.time()

################################################################################
# =============================EXECUTION TIME: 7ms==============================

x1,x2,y1,y2=0,-4,0,0
horizontal=[(x1,x2,y1)]
vertical=[]

def cross_point(ll,line_now):
	for e in ll:
		if line_now[2]>min(e[0],e[1]) and line_now[2]<max(e[0],e[1]):
			if e[2]>min(line_now[0],line_now[1]) and e[2]<max(line_now[0],line_now[1]):
				if ll==vertical:
					print "intersection point : (%d,%d)"%(e[2],line_now[2])
				else:
					print "intersection point : (%d,%d)"%(line_now[2],e[2])

def main():
	global x1,x2,y1,y2
	f=open('day1.txt','r')
	lst=f.read().split(',')
	lst.pop(0)
	for e in lst:
		if x2<x1:
			x1,y1=x2,y2
			if e[1]=='L':
				y2-=int(e[2:])
			elif e[1]=='R':
				y2+=int(e[2:])
			vertical.append((y1,y2,x2))
			cross_point(horizontal,vertical[-1])

		elif x2>x1:
			x1,y1=x2,y2
			if e[1]=='R':
				y2-=int(e[2:])
			elif e[1]=='L':
				y2+=int(e[2:])
			vertical.append((y1,y2,x2))
			cross_point(horizontal,vertical[-1])

		elif y2<y1:
			x1,y1=x2,y2
			if e[1]=='R':
				x2-=int(e[2:])
			elif e[1]=='L':
				x2+=int(e[2:])
			horizontal.append((x1,x2,y2))
			cross_point(vertical,horizontal[-1])

		elif y2>y1:
			x1,y1=x2,y2
			if e[1]=='L':
				x2-=int(e[2:])
			elif e[1]=='R':
				x2+=int(e[2:])
			horizontal.append((x1,x2,y2))
			cross_point(vertical,horizontal[-1])	

	return x2,y2	

print main()
print x2+y2
print time.time()-begin