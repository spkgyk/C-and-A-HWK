import sys


def ncr(n, r, p):
    # initialize numerator
    # and denominator
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den, p - 2, p)) % p


if __name__ == "__main__":
    n, k = sys.stdin.readline().split(" ")

    n = int(n)
    k = int(k)

    ans = ncr(n, k, 10**9 + 7)

    print(ans)
