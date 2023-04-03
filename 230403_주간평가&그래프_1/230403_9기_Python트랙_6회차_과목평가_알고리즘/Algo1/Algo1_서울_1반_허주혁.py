import sys
sys.stdin = open("algo1_sample_in.txt", "r")

num_dic = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15, 'G':16}

# 16진수를 4비트 2진수로 변환 함수
def two_bit(num):
    two_bit_num = ''

    while len(two_bit_num) != 4:
        two_bit_num += str(num % 2)
        num //= 2

    return two_bit_num[::-1]

# 연속된 1의 개수의 최대값
def num_of_one(string):
    mx = 0
    cnt = 0
    for z in string:
        if z == '1':
           cnt += 1
        else:
            if mx < cnt:
                mx = cnt
            cnt = 0

    if mx < cnt:
        mx = cnt

    return mx

T = int(input())

for tck in range(1, T+1):
    N = int(input())
    string = input()

    two_bit_num = ''
    # 문자열을 숫자로 변환
    for x in string:
        if x in num_dic.keys():
            two_bit_num += two_bit(num_dic[x])
        else:
            two_bit_num += two_bit(int(x))

    # 연속된 1의 개수의 최대값
    ans = num_of_one(two_bit_num)

    print(f'#{tck} {ans}')

