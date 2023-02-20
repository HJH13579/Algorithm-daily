import sys
sys.stdin = open("s_input.txt", "r")

def paper_glue(n):
    if n == 1:
        return 1

    if n % 2 == 0:
        return 3 ** (n // 2)
    else:
        return 2 * paper_glue(n-2) + paper_glue(n-1)

T = int(input())

for tck in range(1, T + 1):
    N = int(input())

    n = N // 10

    print(f'#{tck} {paper_glue(n)}')

