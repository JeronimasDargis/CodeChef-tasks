t = int(input())

for case in range(t):
    result = 0
    n = int(input())
    for digit in str(n):
        result += int(digit)
    print(result)
