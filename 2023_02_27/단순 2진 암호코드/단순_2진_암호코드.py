import sys
sys.stdin = open("s_input.txt", "r")

# 7개의 암호코드(문자열)를 숫자로 변환하는 딕셔너리
code_dic = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}


# 암호코드 시작점 찾기
def find_start(arr, N, M):
    for y in range(N):
        for x in range(0, M - 7):
            string = ''
            for n in range(0, 7):
                if arr[y][x + n] == 0:
                    string += '0'
                else:
                    string += '1'

            for v in list(code_dic.keys()):
                if v == string:
                    return y, x


# 7개 단위로 숫자를 문자열로 변환하여 암호코드를 숫자로 변환하는 함수
def decoding(start_idx_i, start_idx_j, arr):
    try:
        lst = []
        for x in range(start_idx_j, start_idx_j+56, 7):
            secret_code = ''
            for n in range(0, 7):
                if arr[start_idx_i][x+n] == 0:
                    secret_code += '0'
                else:
                    secret_code += '1'

            lst.append(code_dic[secret_code])

        # return lst

        # 암호코드 숫자들의 합
        sum_lst = 0
        for k in lst:
            sum_lst += k

        sum_odd = 0
        sum_even = 0

        for y in range(len(lst)-1):
            if y % 2 == 0:
                sum_odd += lst[y]
            else:
                sum_even += lst[y]

        decode_num = (sum_odd * 3 + sum_even + lst[len(lst)-1]) % 10

        if decode_num == 0:
            return sum_lst
        else:
            return 0

    except KeyError:
        return 0


T = int(input())

for tck in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input())) for _ in range(N)]

    if find_start(arr, N, M) == None:
        ans = 0

    else:
        start_idx_i, start_idx_j = find_start(arr, N, M)

        # alst = decoding(start_idx_i, start_idx_j, arr)

        ans = decoding(start_idx_i, start_idx_j, arr)

    print(f'#{tck} {ans}')