import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tck in range(1, T+1):
    string = input()

    code = ''
    alst = []

    for x in string:
        # 16진수 -> 십진수
        if x.isdigit():
            n = ord(x) - ord('0')
        else:
            n = ord(x) - ord('A') + 10

        # 십진수 -> 이진수
        for pos in (3, 2, 1, 0):
            code += str((n >> pos) & 1)

    # 7bit씩 묶어 십진수 변환
    for y in range(0, len(code)-7, 7):
        m = 0
        for k in range(0, 7):
            m += int(code[y+k]) * (2 ** (6-k))

        alst.append(m)

    # 남은 bit 묶어서 십진수 변환
    N = len(code)
    M = len(code) % 7
    l = 0
    for z in range(M):
        l += int(code[(N-z) - 1]) * (2 ** z)
    alst.append(l)

    print(f'#{tck}', *alst)