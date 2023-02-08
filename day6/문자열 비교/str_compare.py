import sys

sys.stdin = open("s_input.txt", "r")

T = int(input())

for tck in range(1, T + 1):

    str1 = input()
    str2 = input()

    result = 0

    for i in range(len(str2) - len(str1) + 1):
        if str2[i:i+len(str1)] == str1:
            result = 1
            break

    print(f'#{tck} {result}')

