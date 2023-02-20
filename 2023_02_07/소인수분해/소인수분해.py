import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tck in range(1, T+1):
    N = int(input())

    lst1 = [a, b, c, d, e] = [0, 0, 0, 0, 0]
    lst2 = [2, 3, 5, 7, 11]

    for i in range(5):
        while(1):
            if N % lst2[i] == 0:
                lst1[i] += 1
                N //= lst2[i]
            else:
                break

    print(f'#{tck}', *lst1)
