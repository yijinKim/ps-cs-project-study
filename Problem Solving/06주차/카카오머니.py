# 424ms

import sys
input = sys.stdin.readline

n = int(input())
balance = 0
charge_unit = 0 #최소 충전 단위
MAXI = 10 ** 18
min_b = MAXI
available_value = True


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x
    

for _ in range(n):
    a, b = map(int, input().split())
    
    if balance + a < 0:  # 충전이 필요한 경우
        if b!= 0 and b < min_b:
            min_b = b
        charge_unit = gcd(b - balance - a, charge_unit)
        
        if charge_unit <= min_b and min_b != MAXI:
            available_value = False
            break
    else: #  balance + a >= 0  # 충전 필요 없이 계산됨.
        if balance + a != b: # 잔액이 맞지 않는 경우
            available_value = False
            break
    balance = b 


if available_value and charge_unit != 0:
    print(charge_unit)
elif available_value and charge_unit == 0:
    print(1)
else:
    print(-1)         