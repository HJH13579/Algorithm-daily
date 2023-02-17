import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())

for tck in range(1, T+1):

    lst = list(input())

    cnt = 0

    if lst[0] == '1':
        cnt = 1
    else:
        cnt = 0

    for i in range(len(lst)-1):
        if lst[i] != lst[i+1]:
            cnt += 1

    print(f'#{tck} {cnt}')