import sys

# import os
# import time
from itertools import accumulate


def adaptedMerge(fullList, lowerIndex, midIndex, upperIndex):
    count = 0

    # split the list into two parts
    leftSplit = fullList[lowerIndex:midIndex]
    rightSplit = fullList[midIndex:upperIndex]

    rightSplitLength = len(rightSplit)

    # we calculate the number of range sums <= to the upper bound with j, and the number of
    # range sums that VIOLATE the lower bound with i.
    i = j = 0

    # for each element in the left split, we subtract each element from the right split.
    # since the fullList contains the cumulative sum, it is equivalent to getting the range
    # sum from position 'a' in the leftSPlit to position 'b' in the rightSplit. We then check
    # the result is within the specified bounds.
    for elementInLeftSplit in leftSplit:

        # since we are using < and <= operators and leftSplit and rightSplit are in ascending
        # order, once either i or j = rightSplitLength, subtracting even larger values in
        # leftSplit from the values in rightSplit will not change the result of the < and <=
        # tests. Hence once both i and j reach rightSplitLength we can assume they stay the same
        # for all subsequent iterations. This allows us to compare all the elements in both lists
        # in O(n) time rather than O(n^2) time.
        while i < rightSplitLength and rightSplit[i] - elementInLeftSplit < lower:
            i += 1
        while j < rightSplitLength and rightSplit[j] - elementInLeftSplit <= upper:
            j += 1

        # subtract i from j to get the number of range sums for each iteration
        # (inclusion exclusion principle)
        count += j - i

    # merge two ordered lists in O(n) time
    leftSplit.append(float("inf"))
    rightSplit.append(float("inf"))
    i = j = 0
    for k in range(lowerIndex, upperIndex):
        if leftSplit[i] <= rightSplit[j]:
            fullList[k] = leftSplit[i]
            i += 1
        else:
            fullList[k] = rightSplit[j]
            j += 1

    return count


def adaptedMergeSort(fullList, lowerIndex, upperIndex):
    midIndex = (lowerIndex + upperIndex) // 2

    # if lowerIndex=midIndex then leftSplit in the 'merge' method will be fullList[k:k]
    # which is the empty list, rather than the kth element. So we have to deal with this
    # case separately
    if lowerIndex < midIndex:
        # add the range sums from the two splits separately
        count = adaptedMergeSort(fullList, lowerIndex, midIndex) + adaptedMergeSort(fullList, midIndex, upperIndex)

        # add the range sums over both splits not included in the previous step
        count += adaptedMerge(fullList, lowerIndex, midIndex, upperIndex)
        return count

    # 1 if in the bounds, 0 otherwise
    return int(lower <= fullList[lowerIndex] <= upper)


if __name__ == "__main__":
    n, lower, upper = sys.stdin.readline().split(" ")
    nums = sys.stdin.readline().split(" ")

    # test.txt contains a large test I ran using a naive version to check my results
    # f = open(os.path.dirname(os.path.abspath(__file__))+"\\test.txt", "r")
    # n, lower, upper = f.readline().split(' ')
    # nums = f.readline().split(' ')

    n = int(n)
    lower = int(lower)
    upper = int(upper)
    nums = map(int, nums)

    # t = time.time()

    # get the cumulative sum of the list
    cumulativeNums = list(accumulate(nums))

    # get the number of range sums
    count = adaptedMergeSort(cumulativeNums, 0, n)

    # print((time.time()-t))
    print(count)
