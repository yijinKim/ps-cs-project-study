import sys
input = sys.stdin.readline

n = int(input())

prev_balance = 0   # 이전 잔액
MAXI = 9*(10**18)  # 최대값 상수변수
min_charge = 0     # 최소 충전 단위
value_flag = True  # 값 존재여부 flag
min_balance = MAXI # 잔액의 최소값


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

    
for _ in range(n):
    money, balance = map(int, input().split())

    if prev_balance + money < 0:
        if balance != 0 and balance < min_balance:
            min_balance = balance

        min_charge = gcd(balance-prev_balance-money, min_charge)

        if min_charge <= min_balance and min_balance != MAXI:
            value_flag = False
            break

    else: # prev_balance + money >= 0
        if prev_balance + money != balance:
            value_flag = False
            break
    prev_balance = balance

if value_flag and min_charge != 0:
    print(min_charge)
elif value_flag and min_charge == 0:
    print(1)
else:
    print(-1)