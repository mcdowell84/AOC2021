input = open('input/06.txt', 'r')
input = input.read().split(',')
input = list(map(int, input))

testinput = [3,4,3,1,2]
print(testinput)

#input = testinput

fishdict = {}
for i in range(9):
	fishdict[i] = 0

for count, value in enumerate(input):
	fishdict[value] += 1

def newtimer(fishdict):
	for i in range(0,9):
		fishdict[i-1] = fishdict[i]
	#print(fishdict)
	newborn = fishdict[-1]
	fishdict[6] += fishdict[-1]
	del fishdict[-1]
	fishdict[8] = newborn
	return fishdict
	
days = 256

for i in range(days):
	fishdict = newtimer(fishdict)			
	
values = fishdict.values()
total = sum(values)
print(total)