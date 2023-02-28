import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())

for tck in range(1, T+1):

    ans_lst = ['']*(15*5)

    for m in range(5):
        lst = list(input())

        for x in range(len(lst)):
            ans_lst[m + 5*x] = lst[x]

    print(f'#{tck} {"".join(ans_lst)}')