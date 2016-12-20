import time
start =time.time()

initial = "10010000000110000"
disk_length = 35651584

def check_sum(a):
	while 1:
		strx=""
		for i in xrange(0,len(a),2):
			if a[i]==a[i+1]:
				strx+='1'
			else : strx+='0'

		if len(strx)%2:
			break
		a=strx

	return strx

def dragon_curve(a):
	global disk_length

	while 1:
		b=""
		# the replace method
		b = a.replace('1', 'x').replace('0', '1').replace('x', '0')

		strx = a+ '0' + b[::-1]

		if len(strx)>=disk_length:
			break
		a=strx
	return strx[:disk_length]

def main():
	global initial
	strx = dragon_curve(initial)
	return check_sum(strx)

print main()
print time.time()-start