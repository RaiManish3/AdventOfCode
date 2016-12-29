# word="abcdefgh"
word ="fbgdceah"

"""
	FOR PART 1 UNCOMMENT THE PRESENTLY COMMENTED SECTION AND VICE-VERSA.

"""

def swap_pos(x,y):
	global word
	letter_x=word[x]
	letter_y=word[y]
	word = word.replace(letter_x,'t').replace(word[y],letter_x).replace('t',letter_y)

def swap_letters(x,y):
	global word
	word = word.replace(x,'t').replace(y,x).replace('t',y)

def rotate_steps(x,left):
	global word
	l=len(word)
	x%=l
	# part 1
	# if left:
	# part 2
	if not left:
		word = word[x:]+word[0:x]
	else : word = word[l-x:]+word[0:l-x]

def part2_rotate(index,elem):
	global word
	strx =word
	l=len(word)

	while True:
		# index equality
		strx = strx[1:]+strx[0:1]
		new_index = strx.index(elem)
		new_index =  (new_index+2)%l if new_index>=4 else (new_index+1)%l
		new_index= (new_index+strx.index(elem))%l
		if index == new_index:
			break
	word = strx


def reverse_through(start,end):
	global word
	strx = (word[start:end+1])[::-1]
	word = word[:start]+strx+word[end+1:]

def move(x,y):
	global word
	if x<y:
		word = word[:x]+word[x+1:y+1]+word[x]+word[y+1:]
	elif x>y:
		word = word[:y]+word[x]+word[y:x]+word[x+1:]


def main():
	f=open('day21.txt','r')
	lines=100
	strx=[]

	for i in xrange(lines):
		state = f.readline().strip().split(" ")
		strx.append(state[:])

	for i in xrange(lines-1,-1,-1):
	# part1
	# for i in xrange(lines):
		if strx[i][0]=="swap":
			if strx[i][1]=="position":
				swap_pos(int(strx[i][2]),int(strx[i][5]))

			else : swap_letters(strx[i][2],strx[i][5])

		if strx[i][0]=="rotate":
			if strx[i][1]=="left":
				rotate_steps(int(strx[i][2]),True)
			elif strx[i][1]=="right":
				rotate_steps(int(strx[i][2]),False)

			else : 
				# part 1
				# steps = word.index(strx[i][6])
				# steps = steps+2 if steps>=4 else steps+1
				# rotate_steps(steps,False)

				# part 2
				new_index = word.index(strx[i][6])
				part2_rotate(new_index,strx[i][6])

		if strx[i][0]=="reverse":
			reverse_through(int(strx[i][2]),int(strx[i][4]))

		if strx[i][0]=="move":
			# part 1
			# move(int(strx[i][2]),int(strx[i][5]))

			# part 2
			move(int(strx[i][5]),int(strx[i][2]))

		# print strx[i]
		# print word

main()
print word