import sys
sys.stdin = open("s_input.txt", "r")

def quick_sort(n):
    pivot_idx = 0

    if n % 2 == 0:
        pivot_idx = n // 2
    else:
        pivot_idx = n // 2 + 1
    





T = int(input())

for tck in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    A = []

    quick_sort()

    print(f'#{tck} {cnt}')