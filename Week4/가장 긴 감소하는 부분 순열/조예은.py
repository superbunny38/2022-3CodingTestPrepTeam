import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))


def BinarySearch(DP, n):
    left = 0
    right = len(DP)
    
    while(left < right):
        mid = (left + right) // 2
        if DP[mid] > n:
            left = mid + 1
        else:
            right = mid
    return left


if __name__ == '__main__':
    DP = list()
    
    for num in A:
        i = BinarySearch(DP, num)
        if i == len(DP):
            DP.append(num)
        else:
            DP[i] = num
    print(len(DP))