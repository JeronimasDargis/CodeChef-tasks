n = [412, 1203, 2456, 5631]
result = []


def digitSumDifference(numsToCompare):
    for number in numsToCompare:
        diff = sum(map(lambda x: x if x % 2 == 0 else -
                       x, [int(i) for i in str(number)]))
        result.append(diff)

    print(result)


digitSumDifference(n)
