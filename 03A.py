input = open('input/03.txt', 'r')
myFile = input.readlines()
input = [x.replace('\n', '') for x in myFile]

testinput =     ['00100', 
				'11110', 
				'10110', 
				'10111', 
				'10101', 
				'01111', 
				'00111', 
				'11100', 
				'10000', 
				'11001', 
				'00010', 
				'01010']

#input = testinput

length = len(input[0])
length2 = len(input)
dict = {}

for i in range(length):
	dict[i] = ''

for count, value in enumerate(input):
	for i in range(length):
		dict[i] += value[i] 

gamma = ''
epsilon = ''

for i in range(length):
	string = dict[i]
	stringcount = string.count('1')
	if stringcount > length2/2:
		gamma += '1'
		epsilon += '0'
	if stringcount < length2/2:
		gamma += '0'
		epsilon += '1'

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)	
power = gamma*epsilon
	
print(str(gamma))
print(str(epsilon))

print(str(power))