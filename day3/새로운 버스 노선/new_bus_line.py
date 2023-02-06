import sys

sys.stdin = open("s_bus2in.txt", "r")

T = int(input())

for tck in range(1, T + 1):
    N = int(input())

    mx = 0
    station = [0] * 1001    # 1000이 아니라 1001이다. 1번~1000번이 필요한데 첫번째는 0으로 할당되므로 1001까지 생성

    for i in range(N):
        C, A, B = map(int, input().split())

        station[A] += 1
        station[B] += 1

        if C == 1:
            for j in range(A + 1, B):
                station[j] += 1

        if C == 2:
            if A % 2 == 0:
                for x in range(A + 1, B):
                    if x % 2 == 0:
                        station[x] += 1
            if A % 2 == 1:
                for y in range(A + 1, B):
                    if y % 2 == 1:
                        station[y] += 1

        if C == 3:
            if A % 2 == 0:
                for m in range(A + 1, B):
                    if m % 4 == 0:
                        station[m] += 1
            if A % 2 == 1:
                for n in range(A + 1, B):
                    if (n % 3 == 0) and (n % 10 != 0):
                        station[n] += 1

    for i in range(1001):
        if mx < station[i]:
            mx = station[i]

    print(f'#{tck} {mx}')