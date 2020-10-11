t = int(input())
numbers = ''


for case in range(t):
    n = str(input())
    numbers += n


digits = [int(x) for x in str(numbers)]
digits.sort()

for digit in str(digits):
    print(digit)
