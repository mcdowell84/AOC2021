input = open('input/06.txt', 'r')
input = input.read().split(',')
input = list(map(int, input))

testinput = [3,4,3,1,2]
print(testinput)

# input = testinput

def timer(input):
	newborn = 0
	for count, value in enumerate(input):
		if input[count] == 0:
			newborn += 1
		input[count] -= 1
		if input[count] < 0:
			input[count] = 6
	for i in range(newborn):
		input.append(8)
	return input	
days = 80

for i in range(days):
	input = timer(input)			
	
print(len(input))