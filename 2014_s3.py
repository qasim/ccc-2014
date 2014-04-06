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

for x in combo:
	mtn = x[:]
	branch = []
	lake = []
	num = 1

	mtn.reverse()

	while num != len(x) + 1:
		if len(branch) > 0:
			if branch[-1] != num:
				if len(mtn) > 0:
					if mtn[0] != num:
						branch.append(mtn[0])
						mtn = mtn[1:]
					else:
						lake.append(mtn[0])
						mtn = mtn[1:]
						num = num + 1
				else:
					answers.append('N')
					break
			else:
				branch.reverse()
				lake.append(branch[0])
				branch = branch[1:]
				branch.reverse()
				num = num + 1
		else:
			if mtn[0] != num:
				branch.append(mtn[0])
				mtn = mtn[1:]
			else:
				lake.append(mtn[0])
				mtn = mtn[1:]
				num = num + 1
		if len(lake) == len(x):
			answers.append('Y')



sys.stdout.write('\n'.join(answers))
