import sys

sys.stdin = open("s_input.txt", "r")

T = int(input())

for tck in range(1, T + 1):
    D, A, B, F = map(int, input().split())

    distance = (D / (A + B)) * F

    print(f'#{tck} {distance}')