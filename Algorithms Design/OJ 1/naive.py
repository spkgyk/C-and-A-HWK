import sys
import time


def cumsum(nums):
    l = []
    t = 0
    for x in nums:
        t += x
        l.append(t)
    return l


if __name__ == "__main__":
    # t = time.time()
    n, lower, upper = sys.stdin.readline().split(" ")
    nums = sys.stdin.readline().split(" ")

    # f = open("./test.txt", "r")
    # n, lower, upper = f.readline().split(' ')
    # nums = f.readline().split(' ')

    n = int(n)
    lower = int(lower)
    upper = int(upper)
    nums = [int(x) for x in nums]

    s = cumsum(nums)
    count = sum(map(lambda x: x >= lower and x <= upper, s))
    for i in range(n):
        s = [x - nums[i] for x in s[1:]]
        count += sum(map(lambda x: x >= lower and x <= upper, s))

    print(count)
    # print((time.time()-t))
