import student_code
import copy

grade=0

puzzle=[5,2,7,0,1,4,6,8,3]
depth=23
steps=678
path=[1,1,0,3,3,2,1,2,3,0,1,1,2,3,0,3,2,1,0,0,1,2,2]

print("\n\rrunning test 1")
depth_r,steps_r,path_r=student_code.astar(puzzle)


if steps_r==steps:
	grade=grade+1
	print("number of nodes expanded passed")
else:
	print("error in number of nodes expanded expected ",steps, " but got ",steps_r)


if depth_r==depth:
	grade=grade+1
	print("depth passed")
else:
	print("error in depth")

correct=1
if len(path)==len(path_r):
	for i in range(len(path)):
		if path[i]!=path_r[i]:
			correct=0
	if correct==1:
		grade=grade+1
		print("path is correct")
	else:
		print("error in path, expected ",path)
		print("got ",path_r)
else:
	print("error in path size",len(path),len(path_r))
	print("error in path, expected ",path)
	print("got                     ",path_r)
	
	
	
	
#######################################################################
puzzle=[2,4,3,6,7,5,0,8,1]
depth=20
steps=359
path= [0, 1, 2, 1, 0, 3, 2, 3, 0, 1, 0, 3, 2, 1, 2, 1, 0, 3, 2, 1]



print("\n\rrunning test 2")
depth_r,steps_r,path_r=student_code.astar(puzzle)


if steps_r==steps:
	grade=grade+1
	print("number of nodes expanded passed")
else:
	print("error in number of nodes expanded expected ",steps, " but got ",steps_r)



if depth_r==depth:
	grade=grade+1
	print("depth passed")
else:
	print("error in depth")

correct=1
if len(path)==len(path_r):
	for i in range(len(path)):
		if path[i]!=path_r[i]:
			correct=0
	if correct==1:
		grade=grade+1
		print("path is correct")
	else:
		print("error in path, expected ",path)
		print("got ",path_r)
else:
	print("error in path size")
	
	
	
	
#######################################################################
puzzle=[1,3,6,4,2,0,7,5,8]
depth=5
steps=6
path=[0,3,2,2,1]


print("\n\rrunning test 3")
depth_r,steps_r,path_r=student_code.astar(puzzle)


if steps_r==steps:
	grade=grade+1
	print("number of nodes expanded passed")
else:
	print("error in number of nodes expanded expected ",steps, " but got ",steps_r)



if depth_r==depth:
	grade=grade+1
	print("depth passed")
else:
	print("error in depth")

correct=1
if len(path)==len(path_r):
	for i in range(len(path)):
		if path[i]!=path_r[i]:
			correct=0
	if correct==1:
		grade=grade+1
		print("path is correct")
	else:
		print("error in path, expected ",path)
		print("got ",path_r)
else:
	print("error in path size")
	
	

	
	
#######################################################################
puzzle=[1,2,3,4,5,6,7,8,0]
depth=0
steps=1
path=[]


print("\n\rrunning test 4")
depth_r,steps_r,path_r=student_code.astar(puzzle)


if steps_r==steps:
	grade=grade+1
	print("number of nodes expanded passed")
else:
	print("error in number of nodes expanded expected ",steps, " but got ",steps_r)



if depth_r==depth:
	grade=grade+1
	print("depth passed")
else:
	print("error in depth")

correct=1
if len(path)==len(path_r):
	for i in range(len(path)):
		if path[i]!=path_r[i]:
			correct=0
	if correct==1:
		grade=grade+1
		print("path is correct")
	else:
		print("error in path, expected ",path)
		print("got ",path_r)
else:
	print("error in path size")
	
	
	
	
	
#######################################################################
puzzle=[8,6,7,0,5,4,2,3,1]
depth=29
steps=6704
path=[1, 2, 1, 0, 0, 3, 2, 3, 2, 1, 1, 0, 0, 3, 3, 2, 2, 1, 1, 0, 3, 0, 3, 2, 2, 1, 0, 1, 2]



print("\n\rrunning test 5")
depth_r,steps_r,path_r=student_code.astar(puzzle)


if steps_r==steps:
	grade=grade+1
	print("number of nodes expanded passed")
else:
	print("error in number of nodes expanded expected ",steps, " but got ",steps_r)



if depth_r==depth:
	grade=grade+1
	print("depth passed")
else:
	print("error in depth")

correct=1
if len(path)==len(path_r):
	for i in range(len(path)):
		if path[i]!=path_r[i]:
			correct=0
	if correct==1:
		grade=grade+1
		print("path is correct")
	else:
		print("error in path, expected ",path)
		print("got ",path_r)
else:
	print("error in path size")
	
	
	
	
#######################################################################
puzzle=[6,5,3,4,1,2,8,7,0]
depth=26
steps=5614
path=[3, 3, 0, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 3, 0, 0, 1, 2, 1, 2, 3, 0, 3, 2, 1, 1]



print("\n\rrunning test 6 ")
depth_r,steps_r,path_r=student_code.astar(puzzle)


if steps_r==steps:
	grade=grade+1
	print("number of nodes expanded passed")
else:
	print("error in number of nodes expanded expected ",steps, " but got ",steps_r)



if depth_r==depth:
	grade=grade+1
	print("depth passed")
else:
	print("error in depth")

correct=1
if len(path)==len(path_r):
	for i in range(len(path)):
		if path[i]!=path_r[i]:
			correct=0
	if correct==1:
		grade=grade+1
		print("path is correct")
	else:
		print("error in path, expected ",path)
		print("got ",path_r)
else:
	print("error in path size")
	

	
#######################################################################
puzzle=[8,6,7,2,5,4,3,0,1]#deepest solution possible
depth=31
steps=17165
path= [1, 0, 0, 3, 2, 2, 1, 0, 0, 3, 2, 3, 2, 1, 0, 3, 0, 1, 2, 2, 1, 0, 0, 3, 2, 3, 2, 1, 0, 1, 2]


print("\n\rrunning test 7 (this test has deepest solution possible for 3x3 sliding tile puzzle!!)")
depth_r,steps_r,path_r=student_code.astar(puzzle)


if steps_r==steps:
	grade=grade+1
	print("number of nodes expanded passed")
else:
	print("error in number of nodes expanded expected ",steps, " but got ",steps_r)



if depth_r==depth:
	grade=grade+1
	print("depth passed")
else:
	print("error in depth")

correct=1
if len(path)==len(path_r):
	for i in range(len(path)):
		if path[i]!=path_r[i]:
			correct=0
	if correct==1:
		grade=grade+1
		print("path is correct")
	else:
		print("error in path, expected ",path)
		print("got ",path_r)
else:
	print("error in path size")
	




print("\n\n\n\n----------------------------")
print("your program has passed ",grade," out of 21 tests")


