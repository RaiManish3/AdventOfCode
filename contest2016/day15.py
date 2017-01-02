import time
start=time.time()

# for part 1 comment everything related to disc 7

p_1,i_p1=17,5
p_2,i_p2=19,8
p_3,i_p3=7,1
p_4,i_p4=13,7
p_5,i_p5=5,1
p_6,i_p6=3,0
p_7,i_p7=11,0

t=-1
while 1:
	t+=1
	if (i_p1+t+1)%p_1==0 and (i_p2+t+2)%p_2==0 and (i_p3+t+3)%p_3==0 and (i_p4+t+4)%p_4==0 and (i_p5+t+5)%p_5==0 and (i_p6+t+6)%p_6==0 and (i_p7+t+7)%p_7==0:
		break

print t
print time.time()-start