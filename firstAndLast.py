t = int(input())

for case in range(t):
    n = str(input())
    x = [int(i) for i in str(n)]

    numSum = x[0] + x[len(x) - 1]
    print(numSum)
