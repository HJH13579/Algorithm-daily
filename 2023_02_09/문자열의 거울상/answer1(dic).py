import sys

sys.stdin = open("s_input.txt", "r")

dct = {'b':'d', 'd':'b','q':'p','p':'q'}

T = int(input())

for tck in range(1, T + 1):
    st = input()[::-1] # 앞뒤가 반대인 문자열

    alst = []
    for ch in st:
        alst.append(dct[ch])

    print(f'#{tck} {"".join(map(str,alst))}')
