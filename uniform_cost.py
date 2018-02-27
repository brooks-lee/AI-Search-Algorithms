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
	new[1][post+next_move],new[1][post] = new[1][post],new[1][post+next_move]
	#print 'new list', new , 'closed_list ',closed_list 
	if new[1] not in closed_list:
		new[0]=new[0]+cost(new[1][post])
		new[2].append(move)
		open_list.append(new)
		

def successor(minimum):
	#print 'min', minimum 
	post=minimum[1].index(0)

	if post+3 < 9:
		new = copy.deepcopy(minimum)
	#	print closed_list
		moves(+3,new,post,'d')
		
	if post-3 > -1:
		new = copy.deepcopy(minimum)
	#	print closed_list
		moves(-3,new,post,'u')
	
	if post not in [0,3,6]:
		new = copy.deepcopy(minimum)
	#	print closed_list
		moves(-1,new,post,'l')
	
	if post not in [2,5,8]:
		new = copy.deepcopy(minimum)
	#	print closed_list
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


	t=[0,temp_list,[]]                    ###################################value,state,path
	open_list=[t]
	minimum = copy.deepcopy(min(open_list)) 
	min_ind = open_list.index(minimum)


	while  minimum[1]!=final_state:
		 closed_list.append(minimum[1])
		 del(open_list[min_ind])
		 successor(copy.deepcopy(minimum))
		 minimum=copy.deepcopy(min(open_list))
		 min_ind = open_list.index(minimum)
		 
		 
	#print "the final state has been attained"
	print minimum[0],' ',minimum[2]
	 
	 
	 



		
