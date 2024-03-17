import sys

if __name__ == "__main__":
    n, M = map(int, sys.stdin.readline().split(" "))
    words = sys.stdin.readline().strip().split(" ")
    lengths = list(map(len, words))

    total_costs = [0] * n
    for i in range(n - 2, -1, -1):
        current_length = -1
        total_costs[i] = sys.maxsize
        for j in range(i, n):
            current_length += lengths[j] + 1

            if current_length > M:
                break
            elif j == n - 1:
                cost = 0
            else:
                cost = (M - current_length) ** 3 + total_costs[j + 1]

            if cost < total_costs[i]:
                total_costs[i] = cost

    print(total_costs[0])
