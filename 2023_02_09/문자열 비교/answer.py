import sys

sys.stdin = open("s_input.txt", "r")

T = int(input())

for tck in range(1, T + 1):

    str1 = input()
    str2 = input()

    ans = 0

    if str1 in str2:
        ans = 1

    print(f'#{tck} {ans}')