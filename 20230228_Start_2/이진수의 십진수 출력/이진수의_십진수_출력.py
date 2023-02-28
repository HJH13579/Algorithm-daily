import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tck in range(1, T+1):
    lst = list(map(int, input()))

    alst = []

    num = 0
    for x in range(len(lst)):
        y = x % 7
        num += lst[x] * (2 ** (6 - y))

        if y == 6:
            alst.append(num)
            num = 0

    print(f'#{tck}', *alst)