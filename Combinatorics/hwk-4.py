import sys
import numpy as np

fatPrime = 1000000007


def partitions(i, n):
    if i > n:
        return 0
    elif n == 0 & i == 0:
        return 1
    elif n < 1:
        return 0
    elif i < 1:
        return 0
    elif alreadyCalculated[i][n] > 0:
        return alreadyCalculated[i][n]
    else:
        res = (partitions(i, n - i) + partitions(i - 1, n - 1)) % fatPrime
        alreadyCalculated[i][n] = res
        return res


global alreadyCalculated

if __name__ == "__main__":
    n, k = sys.stdin.readline().split(" ")

    n = int(n)
    k = int(k)

    alreadyCalculated = np.zeros((k + 1, n + 1))

    total = 1

    for i in range(k, 1, -1):
        total += partitions(i, n)
        total %= fatPrime

    print(total)
