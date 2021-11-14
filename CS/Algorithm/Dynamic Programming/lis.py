#Solution : dp
array = [2,11,4,55,7,9,13,3]
dp = [0] * len(array)

for i in range(len(array)):
    dp[i] = 1
    for j in range(len(array)):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))

# Solution: binary search
import bisect

x = len(arr)
# arr = list(map(int, input().split()))

dp = [arr[0]]

for i in range(x):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        idx = bisect.bisect_left(dp, arr[i])
        dp[idx] = arr[i]

print(len(dp))