import sys

sys.stdin = open("input.txt", "r", encoding="UTF8")

for tck in range(1, 11):
    _ = int(input())
    p = input()
    t = input()

    M = len(p)
    N = len(t)

    i = 0   # p의 인덱스
    j = 0   # t의 인덱스

    cnt = 0

    while j < N:
        while i < M and j < N:
            if p[i] == t[j]:
                i += 1
                j += 1
            else:
                j = j - i + 1
                i = 0

        if i == M:
            cnt += 1

            j = j - i + 1
            i = 0

    print(f'#{tck} {cnt}')