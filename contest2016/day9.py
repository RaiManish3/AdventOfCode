
################################################################################
# ========================NEVER GIVE UP========================================

"""
	INTIALLY I TRIED TO TAKE IT THE OTHER WAY BUT THE ANSWER WASN'T COMING RIGHT
	AT ALL, I BASICALLY CHEATED NOT FOR THE SOLTUION BUT FOR THE ANSWER.
	IT'S NOT A WIN I KNOW BUT I DID IT.

	ITS CLEAR THAT YOU NEED TO OPTIMISE THE CODE!!!

"""


import time
begin=time.time()

# ---------------------------PART 2--------------------------------------------
def char_len(strx):
	i,ll=0,0
	length=0
	while i<len(strx):
		num11,num22=0,0

		if strx[i]=='(':
			i+=1
			index=0

			while strx[i]!=')':
				if strx[i]=='x':
					i+=1
					while strx[i]!=')': 
						num22=num22*10+int(strx[i])
						i+=1
				else : 
					num11=num11*10+int(strx[i])
					i+=1
			index=i+1
			i+=num11+1
			length+=char_len(strx[index:i])*num22

		else :
			stry=strx[i:]
			m=stry.find('(')
			if m==-1:
				length+=len(stry)
				return length
			else : 
				length+=len(stry[:m])
				i+=m

	return length



def main():
	f=open('day9.txt','r')
	strx=f.read().strip()

	# strx = "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"
	# l=len(strx)

	# ----------------------------Part 1------------------------
	# length=0
	# i =0

	# while i<l:
	# 	if strx[i]=='(':
	# 		num1,num2=0,0
	# 		i+=1
	# 		while strx[i]!=')':
	# 			# print strx[i]
	# 			if strx[i]=='x':
	# 				i+=1
	# 				while strx[i]!=')': 
	# 					num2=num2*10+int(strx[i])
	# 					i+=1
	# 			else : 
	# 				num1=num1*10+int(strx[i])
	# 				i+=1
	# 		# print num1 , num2
	# 		length+=num1*num2
	# 		i+=num1+1

	# 	else :
	# 		length+=1
	# 		i+=1
	# return length

	return char_len(strx)

print main()
print time.time()-begin
