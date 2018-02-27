import os
import psutil

pid = os.getpid()
k ='pmap '+str(pid)
mem = os.system(k)
def cost(num):
	if num in [1,2,3]:
		return 1
	elif num in [4,5,6]:
		return 2
	else:
		return 3
			
def moves(next_move,new,post,move):
	new[0][post+next_move],new[0][post] = new[0][post],new[0][post+next_move]
	if new[0] not in closed_list:
		new[1].append(move)
		open_list.append(new)
		

def successor(minimum):
	#print 'min', minimum 
	post=minimum[0].index(0)

	if post+3 < 9:
		new = copy.deepcopy(minimum)

		moves(+3,new,post,'d')
		
	if post-3 > -1:
		new = copy.deepcopy(minimum)

		moves(-3,new,post,'u')
	
	if post not in [0,3,6]:
		new = copy.deepcopy(minimum)

		moves(-1,new,post,'l')
	
	if post not in [2,5,8]:
		new = copy.deepcopy(minimum)

		moves(+1,new,post,'r')



import copy
r=input()
while r!=0:
	r-=1
	closed_list=[]
	open_list=[]
	final_state=[1,2,3,4,5,6,7,8,0]
	temp_list=[]


	#print "enter the initial state"
	for i in range(0,3):
	#	print "enter the ",i+1," row"
		for j in range(1,4):
			k = input()
			temp_list.append(k)

	t=[temp_list,[]]                    ###################################value,state,path
	open_list=[t]
	minimum = copy.deepcopy(open_list[0])

	while  minimum[0]!=final_state:
		closed_list.append(minimum[0])
		del(open_list[0])
		successor(copy.deepcopy(minimum))
		minimum=copy.deepcopy(open_list[0])
		 

		 
		 
	#print "the final state has been attained"
	print minimum[1]
		 
