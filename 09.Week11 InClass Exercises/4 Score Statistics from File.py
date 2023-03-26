x = input('Enter score file: ')
y = open(x).read().splitlines()
file = [int(i) for i in y if i != '']
for i in range(len(file)):
    print(f'Student #{i+1} score: {file[i]}')
print(f'Average score is {sum(file)/len(file):.2f}')
print(f'Minimum score is {min(file)}')
print(f'Maximum score is {max(file)}')
