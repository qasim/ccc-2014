import sys

inputs = sys.stdin.readlines()
inputs = [x.rstrip() for x in inputs]

students = int(inputs[0])
first = inputs[1].split(' ')
second = inputs[2].split(' ')

pairs = []

for x in range(0, students):
	if(first[x] == second[x]):
		sys.stdout.write('bad')
		exit()
	pair = [first[x], second[x]]
	pair.sort()
	pairs.append(pair)

for x in pairs:
	temp = pairs[:]
	temp.remove(x)
	if x not in temp:
		sys.stdout.write('bad')
		exit()
	else:
		continue

sys.stdout.write('good')
