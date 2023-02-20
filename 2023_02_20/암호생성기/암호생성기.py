import sys
sys.stdin = open("input.txt", "r")

def code_maker(lst):
    while 1:
        for x in range(1, 6):
            lst.append(lst[0]-x)
            del lst[0]

            if lst[-1] <= 0:
                lst[-1] = 0
                return lst

for tck in range(1, 11):
    _ = int(input())

    lst = list(map(int, input().split()))

    alst = code_maker(lst)

    print(f'#{tck}', *alst)