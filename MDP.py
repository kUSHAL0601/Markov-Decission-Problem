import copy

print("Enter n m:   ",end='')
i=input()
i=i.split()
n=int(i[0])
m=int(i[1])

arr=[]

for it in range(n):
	i=input()
	i=i.split()
	i = list(map(int, i))
	arr.append(i)
# print(arr)
print("Enter e w:   ",end='')
i=input()
i=i.split()

e=int(i[0])
w=int(i[1])

end=[]
for it in range(e):
	i=input()
	i=i.split()
	i = list(map(int, i))
	end.append((i[0],i[1]))

for it in range(w):
	i=input()
	i=i.split()
	i = list(map(int, i))
	arr[i[0]][i[1]]="WALL"

# print(arr)

print("Enter start coordinates:   ",end='')
i=input()
i=i.split()

start_x=int(i[0])
start_y=int(i[1])

print("Enter step cost:   ",end='')
step_cost=float(input())

adjacency_list={}
visited={}

for i in range(n):
	for j in range(m):
		if((i,j) not in end and arr[i][j]!="WALL"):
			adjacency_list[(i,j)]=[]
			visited[(i,j)]=False
			if(i-1>=0 and arr[i-1][j]!="WALL" and (i-1,j) not in end):
				adjacency_list[(i,j)].append((i-1,j))
			if(i+1<n and arr[i+1][j]!="WALL" and (i+1,j) not in end):
				adjacency_list[(i,j)].append((i+1,j))
			if(j+1<m and arr[i][j+1]!="WALL" and (i,j+1) not in end):
				adjacency_list[(i,j)].append((i,j+1))
			if(j-1>=0 and arr[i][j-1]!="WALL" and (i,j-1) not in end):
				adjacency_list[(i,j)].append((i,j-1))

# print(adjacency_list)
queue=[]
visiting_order=[]
queue.append((start_x,start_y))
visited[(start_x,start_y)]=True
while queue:
	s=queue.pop(0)
	# print(s)
	visiting_order.append(s)
	for i in adjacency_list[s]:
		if not visited[i]:
			queue.append(i)
			visited[i]=True

# print(visiting_order)
while True:
	old_arr=copy.deepcopy(arr)
	for i in visiting_order:
		x=i[0]
		y=i[1]
		max_val=-500000000000
		new_val=0.0
		old_val=arr[x][y]
		if(x-1>=0 and arr[x-1][y]!="WALL"):
			new_val+=0.8*arr[x-1][y];
			if(y-1>=0):
				new_val+=0.1*arr[x][y-1];
			else:
				new_val+=0.1*old_val;
			if(y+1<m):
				new_val+=0.1*arr[x][y+1];
			else:
				new_val+=0.1*old_val;
		max_val=max(max_val,new_val)
		new_val=0.0
		if(x+1<n and arr[x+1][y]!="WALL"):
			new_val+=0.8*arr[x+1][y];
			if(y-1>=0):
				new_val+=0.1*arr[x][y-1];
			else:
				new_val+=0.1*old_val;
			if(y+1<m):
				new_val+=0.1*arr[x][y+1];
			else:
				new_val+=0.1*old_val;
		max_val=max(max_val,new_val)
		new_val=0.0
		if(y+1<m and arr[x][y+1]!="WALL"):
			new_val+=0.8*arr[x][y+1];
			if(x-1>=0):
				new_val+=0.1*arr[x-1][y];
			else:
				new_val+=0.1*old_val;
			if(x+1<n):
				new_val+=0.1*arr[x+1][y];
			else:
				new_val+=0.1*old_val;
		max_val=max(max_val,new_val)
		new_val=0.0
		if(y-1>=0 and arr[x][y-1]!="WALL"):
			new_val+=0.8*arr[x][y-1];
			if(x-1>=0):
				new_val+=0.1*arr[x-1][y];
			else:
				new_val+=0.1*old_val;
			if(x+1<n):
				new_val+=0.1*arr[x+1][y];
			else:
				new_val+=0.1*old_val;
		max_val=max(max_val,new_val)
		new_val=0.0
		arr[x][y]=max_val-((abs(start_x-x)+abs(start_y-y))*step_cost)
	flag=0
	# print(arr[0][0])
	for i in visiting_order:
		x=i[0]
		y=i[1]
		if(abs(arr[x][y]-old_arr[x][y]) >=0.01*old_val):
			flag=1
			break
	if(flag==0):
		for i in range(n):
			for j in range(m):
				print(arr[i][j],end=' ')
			print()
		break