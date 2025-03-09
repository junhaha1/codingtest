from sys import stdin

input = stdin.readline

n = int(input())
a = list(map(int, input().rstrip().split()))

dp = [1] * n

#1. DP 풀이 => 시간 복잡도 O(n^2)
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(dp)

#2 이분 탐색 풀이 => 시간 복잡도 O(n * log n)

def binary_serch(a, lis):
    start = 0
    end = len(lis) - 1

    while start < end:
        mid = (start + end) // 2
        if (lis[mid] == a) or (lis[mid - 1] < a < lis[mid]):
            return mid
        elif a < lis[mid]:
            end = mid - 1
        elif a > lis[mid]:
            start = mid + 1
    return start

lis = [a[0]]
for i in range(n):
    if lis[-1] < a[i]:
        lis.append(a[i])
    else:
        idx = binary_serch(a[i], lis)
        lis[idx] = a[i]

print(lis)
