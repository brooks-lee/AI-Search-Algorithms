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
			
def moves(next_move,new,post,move,f):
	if f==1:
		open_list=open_list_1
		closed_list=closed_list_1
	else:
		open_list=open_list_2
		closed_list=closed_list_2
		
	new[0][post+next_move],new[0][post] = new[0][post],new[0][post+next_move]

	if new[0] not in closed_list:

		new[1].append(move)
		open_list.append(new)
		

def successor(minimum,f):
	#print 'min', minimum 
	post=minimum[0].index(0)

	if post+3 < 9:
		new = copy.deepcopy(minimum)

		moves(+3,new,post,2,f) #d
		
	if post-3 > -1:
		new = copy.deepcopy(minimum)

		moves(-3,new,post,3,f) #u
	
	
	
	if post not in [0,3,6]:
		new = copy.deepcopy(minimum)

		moves(-1,new,post,1,f) #r
	
	if post not in [2,5,8]:
		new = copy.deepcopy(minimum)

		moves(+1,new,post,4,f) #l



import copy

r=input()
while r!=0:
	r-=1
	closed_list_1=[]
	open_list_1=[]
	closed_list_2=[]
	open_list_2=[]
	final_state_1=[1,2,3,4,5,6,7,8,0]
	final_state_2=[]
	temp_list=[]

	#print "enter the initial state"
	for i in range(0,3):
		#print "enter the ",i+1," row"
		for j in range(1,4):
			k = input()
			final_state_2.append(k)

	t=[final_state_2,[]]                    ###################################value,state,path
	open_list_1=[t]
	t=[final_state_1,[]]                    ###################################value,state,path
	open_list_2=[t]

	minimum_1 = copy.deepcopy(open_list_1[0]) 
	minimum_2 = copy.deepcopy(open_list_2[0]) 




	while  minimum_1[0]!=final_state_1 and minimum_2[0]!=final_state_2 and minimum_1[0]!=minimum_2[0]:

		closed_list_1.append(minimum_1[0])
		closed_list_2.append(minimum_2[0])
		del(open_list_1[0])
		del(open_list_2[0])
		successor(copy.deepcopy(minimum_1),1)
		successor(copy.deepcopy(minimum_2),2)
		minimum_1=copy.deepcopy(open_list_1[0])
		minimum_2=copy.deepcopy(open_list_2[0])
		 
		 
	#print "code 1:right 2:down 3:up 4:left"
	if minimum_1[0]==final_state_1:
		#print "the final state has been attained"
		print minimum_1[1]
	
	elif  minimum_2[0]==final_state_2:
		#print "the final state has been attained"
		minimum_2[1]=minimum_2[1][::-1]
		minimum_2[1]=map(lambda x:5-x,minimum_2[1])
		print minimum_2[1]
	else:
		#print "the final state has been attained from final"
		minimum_2[1]=minimum_2[1][::-1]
		minimum_2[1]=map(lambda x:5-x,minimum_2[1])
		print minimum_1[1]+minimum_2[1]
		
#print mem

	 
