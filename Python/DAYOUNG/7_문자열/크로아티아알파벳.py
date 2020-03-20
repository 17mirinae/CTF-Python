string = input()
alpa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=','z=']

for i in alpa:
    string = string.replace(i, '1')

print(len(string))