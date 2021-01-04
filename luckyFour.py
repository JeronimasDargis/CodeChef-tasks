import functools
t = int(input())

for case in range(t):
    n = str(input())
    x = [int(i) for i in str(n)]

    numSum = functools.reduce(lambda a, b: a if a == 4 else b == 4, x)
    print(numSum)
