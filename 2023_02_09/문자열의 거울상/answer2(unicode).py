import sys

sys.stdin = open("s_input.txt", "r")

tbl = [0]*128
tbl[ord('b')]='d'
tbl[ord('d')]='b'
tbl[ord('p')]='q'
tbl[ord('q')]='p'

T = int(input())

for test_case in range(1, T + 1):
    st = input()[::-1]
    alst = []

    for ch in st:
        alst.append(tbl[ord(ch)])

    print(f'#{test_case} {"".join(map(str,alst))}')