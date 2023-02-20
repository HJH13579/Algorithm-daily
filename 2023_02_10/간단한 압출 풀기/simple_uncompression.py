import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tck in range(1, T + 1):

    N = int(input())

    dct = {}

    for _ in range(N):
        C, k = map(str, input().split())

        K = int(k)

        dct[C] = K

    string = ''

    for x in dct.keys():
        string += x * dct[x]

    print(f'#{tck}')

    while len(string) > 10:
        ans = ''

        for i in range(10):
           ans += string[i]
        print(ans)
        string = string[10:]

    print(string)

