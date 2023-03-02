import sys
sys.stdin = open("input.txt", "r")

code_dic = {'001101': 0, '010011': 1, '111011': 2, '110001': 3, '100011': 4, '110111': 5, '001011': 6, '111101': 7, '011001': 8, '101111': 9}

def sixteen_to_two_digit(string):
    # 십진수 변환
    code = ''
    for x in string:
        if x.isdigit():
            n = ord(x) - ord('0')
        else:
            n = ord(x) - ord('A') + 10

    # 십진수를 이진수로 변환
        for pos in (3, 2, 1, 0):
            code += str((n >> pos) & 1)

    return code

def decoding(code):
    alst = []

    idx = 0
    for y in range(len(code)-1, -1, -1):
        if code[y] == '1':
            idx = y
            break

    for z in range(idx-5, -1, -6):
        decode = ''
        for m in range(6):
            decode += code[z+m]

        for k in code_dic.keys():
            if k == decode:
                alst.append(code_dic[k])

    return list(reversed(alst))

T = int(input())

for tck in range(1, T+1):
    string = input()

    ans = decoding(sixteen_to_two_digit(string))

    print(f'#{tck}', *ans)