import sys
sys.stdin = open("s_input.txt", "r")

def rock_scissor_paper(a, b):
    if [a, b] == [1, 2] or [2, 3] or [3, 1]:
        return b
    else:
        return a

def grouping(lst):
    global grouped_lst
    cnt = 0

    for x in grouped_lst:
        if len(x) == 2:
            cnt +=1

    if cnt == len(lst) // 2:
        return grouped_lst

    else:
        left_lst = []
        right_lst = []

        for _ in range()






T = int(input())

for tck in range(1, T+1):
    N = int(input())

    lst = list(map(int, input().split()))

    grouped_lst = []


    print(f'#{tck} {ans}')