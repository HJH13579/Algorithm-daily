import sys
sys.stdin = open("s_input.txt", "r")

def num_insert(n):
    if n and n <= N:
        num_insert(n*2)
        lst.append(n)
        num_insert(n*2+1)


T = int(input())

for tck in range(1, T+1):
    N = int(input())

    lst = []
    num_insert(1)

    ch = [0]*(N+1)
    for x in range(1, N+1):
        for y in lst:
            if ch[y] == 0:
                ch[y] = x
                break

    print(f'#{tck} {ch[1]} {ch[N//2]}')