#input = open('input/02.txt', 'r')
#myFile = input.readlines()
#input = [x.replace('\n', '') for x in myFile]

testinput =     ['forward 5',
                'down 5',
                'forward 8',
                'up 3',
                'down 8',
                'forward 2']

input = testinput

aim = 0
hor = 0
dep = 0

for count, value in enumerate(input):
    if value[0] == 'f':
        hor += int(value[-1])
        dep += aim * int(value[-1])
    if value[0] == 'd':
        aim += int(value[-1])
    if value[0] == 'u':
        aim -= int(value[-1])

print(str(hor))
print(str(dep))
print(str(hor*dep))