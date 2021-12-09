# 반례 모음: https://bingorithm.tistory.com/13

'''
시간초과
'''
'''
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
lst = list(map(int, input().split()))
minLen = len(lst)

for num in lst:
    if num>=s:
        minLen = 1
        break

l, r = 0, 1
while l < r:
    # print(lst[l:r+1], sum(lst[l:r+1]))
    
    if sum(lst[l:r+1])>= s:
        minLen = min(minLen, r-l+1)
        # print('minLen: ',minLen)
        l += 1
    else:
        r += 1
print(minLen)         
'''

'''
solution2 144ㅡms
'''
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
lst = list(map(int, input().split()))

def solve(s, lst):
    minLen = 100001
    total = 0
    l, r = 0, 0
    while True:
        if total >= s:
            minLen = min(minLen, r-l)
            total -= lst[l]
            l += 1     
        elif r == n:
            break
        else:
            total += lst[r]
            r += 1
    if minLen == 100001:
        return 0
    else:
        return minLen



print(solve(s, lst))

'''
부분합 참조 해설
https://claude-u.tistory.com/393
''' 
N, S = map(int, input().split())
A = list(map(int, input().split()))

#먼저 0~n까지의 합을 구해줌
sum_A = [0] * (N + 1)
for i in range(1, N + 1):
    sum_A[i] = sum_A[i-1] + A[i-1]  
    
#투포인터 설정
answer = 1000001
start = 0
end = 1

#알고리즘 실행
while start != N:
    if sum_A[end] - sum_A[start] >= S:
        if end - start< answer:
            answer = end - start
        start += 1
        
    else:
        if end != N:
            end += 1
        else:
            start += 1

#답이 없을 경우 & 있을 경우
if answer != 1000001:
    print(answer)
else:
    print(0)