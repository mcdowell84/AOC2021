import numpy as np
import math

input = open('input/04.txt', 'r')
myFile = input.readlines()
input = [x.replace('\n', '') for x in myFile]

balls = input[0]
balls = balls.split(",")					 
balls = list(map(int, balls))
input.pop(0)

testballs = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
# testballs = [7,4,9,5,11]
#balls = testballs


data = np.loadtxt(fname='input/04.txt',skiprows=2)

shape = np.shape(data)
#shadowboard = np.zeros(shape)

length = shape[0]
sections = int(length/5)
shadowboard = np.split(data, sections)

#sump = 1
#sumx = 1	
finallball = 1
 
for count, value in enumerate(balls):
	result = np.where(data==value)
	length = len(result[0])
	for i in range(length): # run over tuple
		y = result[0][i]
		x = result[1][i]
		board = math.floor(y/5)
		yo = y % 5 
		shadowboard[board][yo][x] = 0
		sump = np.sum(shadowboard[board][yo])
		if sump == 0:
			finalball = value
			break
		else:	
			sumx = np.sum(shadowboard[board], axis=1)
			if np.any(sumx == 0):
				finalball = value
				break
	if sump == 0:		
		break
	if np.any(sumx == 0):
		break

print('board=' + str(board))
print(shadowboard[board])
answer = sum(shadowboard[board])
answer= sum(answer)
print(answer*finalball)
print(finalball)



