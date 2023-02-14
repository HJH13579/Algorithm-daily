import sys
sys.stdin = open("s_input.txt", "r")

for tck in range(1, 11):
    _, N = map(int, input().split())
    lst = list(map(int, input().split()))

    for i in range(len(lst)):
