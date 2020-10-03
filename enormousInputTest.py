n, k = map(int, input().split())
answer = int
for case in range(n):
    t = int(input())
    if t % k == 0:
        answer += 1
print(answer)
