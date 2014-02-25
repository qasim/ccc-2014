import sys

inputs = sys.stdin.readlines()
inputs = [int(x) for x in inputs]

tests = inputs[0]

combo = []

extra = 0

answers = []

for i in range(tests):
	_len = inputs[1 + extra]
	test = []
	for x in range(extra, _len + extra):
		test.append(inputs[x + 2])
	combo.append(test)
	extra = extra + _len + 1

for test in combo:
	before = test[:test.index(1)]
	after = test[test.index(1) + 1:]
	if after != []:
		after_sorted = after[:]
		after_sorted.sort()
		if after != after_sorted:
			answers.append('N')
			continue
		else:
			#perform other way search
			if before != []:
				if before[-1] > after[0]:
					answers.append('N')
				else:
					answers.append('Y')
			else:
				answers.append('N')
	else:
		if before != []:
			before_sorted = before[:]
			before_sorted.sort()
			before_sorted.reverse()
			if before_sorted == before:
				answers.append('N')
			else:
				answers.append('Y')
		else:
			answers.append('N')

sys.stdout.write('\n'.join(answers))
