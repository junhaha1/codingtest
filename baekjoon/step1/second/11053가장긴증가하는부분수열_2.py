from sys import stdin

input = stdin.readline
N = int(input())
nums = list(map(int, input().rstrip().split()))

dp = []

def binary_search(num):
    lo = 0
    hi = len(dp)

    while lo < hi:
        mid = (lo + hi) // 2
        if dp[mid] > num:
            hi = mid
        elif dp[mid] < num:
            lo = mid + 1
        else:
            return mid
    return lo

for num in nums:
    i = binary_search(num)
    if i == len(dp):
        dp.append(num)
    else:
        dp[i] = num
print(len(dp))