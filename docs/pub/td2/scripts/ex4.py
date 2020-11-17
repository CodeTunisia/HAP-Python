# a) Triangle
n=5
for i in range(n):
    for j in range(i):
        print ('*', end=" ")
    print('')

# b) Pyramide
n=5
for i in range(n):
    for j in range(i):
        print ('*', end=" ")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('*', end=" ")
    print('')