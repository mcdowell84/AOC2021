input = open('input/03.txt', 'r')
myFile = input.readlines()
input = [x.replace('\n', '') for x in myFile]

mybackup = input

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
mybackup = input

length = len(input[0])
	
def verticalizer(pos, list): #create string from vertical of input
	string = ''
	for count, value in enumerate(list):
		string += value[pos]
	return string
	



def beancounter(string):	# count number of 1s, return if 0 or 1 is more common
	majority = len(string) / 2
	stringcount = string.count('1')
	if stringcount >= majority:
		bean = '1'
	if stringcount < majority:
		bean = '0'
	return bean
	
def beancounter2(string):	# CO2 version
	majority = len(string) / 2
	stringcount = string.count('0')
	if stringcount > majority:
		bean = '1'
	if stringcount <= majority:
		bean = '0'
	return bean
	


		
def destroyer(bean, pos, list): # only add approved items to newlist, return newlist
	newlist = []
	for count, value in enumerate(list):
		if value[pos] == bean:
			newlist.append(value)
	return newlist
	


# Oxygen
for u in range(length):
	string = verticalizer(u, input)
	bean = beancounter(string)
	input = destroyer(bean, u, input)
	if len(input) == 1:
		oxygen = input[0]
		break

# CO2
input = mybackup
		
for r in range(length):
	string = verticalizer(r, input)
	bean = beancounter2(string)
	input = destroyer(bean, r, input)
	if len(input) == 1:
		carbon = input[0]
		break


oxygen = int(oxygen, 2)	
carbon = int(carbon, 2)	
power = oxygen*carbon

print(oxygen)
print(carbon)
print(power)