import hashlib
import re
salt = "ahsbgdzn"
# salt="abc"

concrete_keys=[]
assumed_keys={}
remove_lst=[]

hex_digit3=['000','111','222','333','444','555','666','777','888','999','aaa','bbb','ccc','ddd','eee','fff']
hex_digit5=['00000','11111','22222','33333','44444','55555','66666','77777','88888','99999','aaaaa','bbbbb','ccccc','ddddd','eeeee','fffff']

def make_ckey(index):
	concrete_keys.append(index)

def put_akey(index,hashed_string,repeat_c):
	assumed_keys[hashed_string]=[index+1,index+1000,repeat_c]

def remove_akey(hashed_string):
	del assumed_keys[hashed_string]

def otp():
	index=0


	while 1:
		if len(concrete_keys)>=64:
			break
		print index, len(concrete_keys)

		# generate md5 hash
		this_string=salt+str(index)
		hmd=''

		# remove for loop for part1
		for i in xrange(2017):
			hash_object = hashlib.md5(this_string.encode())
			hmd=hash_object.hexdigest()
			this_string=hmd

		this_string=salt+str(index)

		# find pattern for 3
		found,xv=1000000,'-1'
		for i in xrange(16):
			if hex_digit3[i] in hmd:
				if hmd.index(hex_digit3[i])<found:
					found=hmd.index(hex_digit3[i])
					xv=hex_digit3[i][0]

		if xv!='-1':
			put_akey(index,this_string,xv)

		# find pattern for 5
		found,xv=1000000,'-1'
		for i in xrange(16):
			if hex_digit5[i] in hmd:
				if hmd.index(hex_digit5[i])<found:
					found=hmd.index(hex_digit5[i])
					xv=hex_digit5[i][0]

		if xv!='-1':			
			for k in assumed_keys.keys():
				if assumed_keys[k][1]<index:
					remove_lst.append(k)
					continue
				if assumed_keys[k][2]==xv and k!=this_string:
					make_ckey(assumed_keys[k][0]-1)
					remove_akey(k)

		# remove invalid keys
		for k in assumed_keys.keys():
			if assumed_keys[k][1]<=index:
				remove_lst.append(k)

		for i in remove_lst:
			remove_akey(i)
		del remove_lst[:]
		index+=1

otp()
print sorted(concrete_keys)[63]