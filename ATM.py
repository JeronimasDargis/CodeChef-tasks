x, y = map(float, input().split())
if x % 5 == 0:
    if x+.5 <= y:
        y -= (x+.5)
print(y)


# x = 30
# y = 120.00

# if x % 5 == 0 and y - x - .5 > 0:
#     print(y - x - .5)
# else:
#     print(y)
