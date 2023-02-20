import sys

sys.stdin = open("s_input.txt", "r", encoding="UTF8")

T = int(input())

for tck in range(1, T + 1):

    N = input()
    M = input()

    lst_N = list(set(N))

    lst_cnt = []

    for x in lst_N:
        cnt = 0
        for y in range(len(M)):
            if x == M[y]:
                cnt += 1
        lst_cnt.append(cnt)

    mx = 0
    for z in lst_cnt:
        if mx < z:
            mx = z

    print(f'#{tck} {mx}')