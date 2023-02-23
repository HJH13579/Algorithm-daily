import sys
sys.stdin = open("s_input.txt", "r")

def preorder(n):
    if n:
        alst.append(n)
        preorder(ch1[n])
        preorder(ch2[n])


T = int(input())

for tck in range(1, T+1):
    E, N = map(int, input().split())

    lst = list(map(int, input().split()))

    mx = 0
    for x in lst:
        if mx < x:
            mx = x

    ch1 = [0]*(mx+1)
    ch2 = [0]*(mx+1)

    for i in range(0, len(lst), 2):
        p, c = lst[i], lst[i+1]

        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c

    alst = []
    preorder(N)

    cnt = 0
    for _ in alst:
        cnt += 1

    print(f'#{tck} {cnt}')