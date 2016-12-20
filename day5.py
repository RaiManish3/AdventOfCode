import hashlib


def main():
	main_string="ffykfhsq"
	# 2015 pt2
	# main_string="iwrupvqb"
	number=346386
	lst=[0 for i in xrange(8)]
	ll=['0','1','2','3','4','5','6','7']
	index=0
	while index<8:
		mystring = main_string+str(number)
		hash_object = hashlib.md5(mystring.encode())
		hmd=hash_object.hexdigest()
		if hmd[:5]=="00000" and hmd[5].isdigit() and hmd[5] in ll:
			lst[int(hmd[5])]=hmd[6]
			ll.remove(hmd[5])
			index+=1		

		# 2015 pt2
		# if hmd[:6]=="000000":
		# 	return number

		number+=1
		print number, index, mystring
	return lst

print main()