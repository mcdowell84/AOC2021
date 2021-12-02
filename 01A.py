input = open('input/01A.txt', 'r')
myFile = input.readlines()
input = [x.replace('\n', '') for x in myFile]

testinput = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

# input = testinput

counter = 0
ni = len(input)

def checker(x):
    global counter
    line = int(input[x])
    prev = int(input[x-1])
    if line>prev:
        counter += 1

for i in range(1, ni):
    checker(i)

print(str(counter))
