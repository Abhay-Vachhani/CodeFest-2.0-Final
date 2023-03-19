inputFileName = 'big_input.txt'
inputFileName = 'small_input.txt'
outputFileName = inputFileName.replace('input', 'output')
with open(outputFileName, 'w') as fp:
    pass
with open(inputFileName, 'r') as fp:
    data = fp.readlines()

n = int(data[0])
data = data[1:]
x = data[::2]
y = data[1::2]
for case in range(n):
    xCase, yCase = [int(i) for i in x[case].split()], [int(i) for i in y[case].split()]
    stool = 0
    z = []
    for i in yCase:
        s = i - stool
        if s > 0:
            z += [10 if i % 2 == 0 else 20 for i in range(s)]
            stool += s
    with open(outputFileName, 'a') as fp:
        fp.write(f'Case #{case + 1} : {yCase[len(yCase) // 2]} {sum(z) // xCase[0] * 2}\n')