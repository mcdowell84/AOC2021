input = open('input/01A.txt', 'r')
myFile = input.readlines()
input = [x.replace('\n', '') for x in myFile]
input = list(map(int, input))

testinput = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

# input = testinput


counter = 0
ni = len(input)
batch = []

for i in range(0, ni-2):
    sum = input[i] + input[i+1] + input[i+2]
    batch.append(sum)


nb = len(batch)


def checker(x):
    global counter
    line = int(batch[x])
    prev = int(batch[x-1])
    if line>prev:
        counter += 1

for i in range(1, nb):
    checker(i)

print(str(counter))
