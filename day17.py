import hashlib
import time
begin=time.time()

#########################################################################
# -----------------------EXECUTION TIME : both under 0.3s----------------

key = "pxxbnzuo"
# key = "kglvqrro"

max_steps=0
min_steps=100000
thefinalpass=""

open_door = ['b','c','d','e','f']
part1=False

def recur(passcode,steps,i,j):
	global min_steps,thefinalpass,max_steps

	hash_object = hashlib.md5(passcode.encode())
	hmd=hash_object.hexdigest()[:4]

	# an optimisation to part 1 problem
	# uncomment the below for part 1
	# if steps>=min_steps:
	# 	return

	if(i==3 and j==3):
		if part1 and steps<min_steps:
			min_steps=steps
			thefinalpass=passcode

		if not part1 and steps>max_steps:
			max_steps=steps
			thefinalpass=passcode
		return

	if hmd[0] in open_door and i>0:
		recur(passcode+'U',steps+1,i-1,j)

	if hmd[1] in open_door and i<3:
		recur(passcode+'D',steps+1,i+1,j)

	if hmd[2] in open_door and j>0:
		recur(passcode+'L',steps+1,i,j-1)

	if hmd[3] in open_door and j<3:
		recur(passcode+'R',steps+1,i,j+1)

recur(key,0,0,0)
if part1: print thefinalpass[8:]
else : print max_steps

print time.time()-begin
