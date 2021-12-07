import operator

input = open('input/07.txt', 'r')
input = input.read().split(',')
input = list(map(int, input))

testinput = [16,1,2,0,4,2,7,1,2,14]

#input = testinput
input.sort(reverse=True)
# print(input)
crabdict = {}
#for i in range():
#	fishdict[i] = 0

for count, value in enumerate(input):
	crabdict[value] = 0

for count, value in enumerate(input):
	crabdict[value] += 1

sorted_d = sorted(crabdict.items(), key=operator.itemgetter(1), reverse=True)
#print(sorted_d)

total = 0



def fuelcalc(goal):
	fuel = 0
	for o in range(len(sorted_d)):
		newfuel = 0
		tuple = sorted_d[o]
		pos = tuple[0]
		multi = tuple[1]
		difference = abs(pos-goal)
		for p in range(difference):
			newfuel += (p+1)
		newfuel = newfuel * multi
		fuel += newfuel
	return fuel
		
 

number = input[0]


best = 10000000000000000000

for i in range(number):
	total = 0
	total = fuelcalc(i)
	
	
	if total < best:
		best = total
		
print(best)
	
	
	


	