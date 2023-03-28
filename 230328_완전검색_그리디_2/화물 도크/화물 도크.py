import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())

for tck in range(1, T+1):
    N = int(input())
    lst = []
    for _ in range(N):
        s, e = map(int, input().split())
        lst


    print(f'#{tck} {lst}')
