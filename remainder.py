t = int(input())

for case in range(t):
    a, b = map(int, input().split())
    remainder = a % b
    print(remainder)
