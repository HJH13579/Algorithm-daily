import sys
sys.stdin = open("s_input.txt", "r")

# 7개의 암호코드(문자열)를 숫자로 변환하는 딕셔너리
code_dic = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}


# 암호코드 시작점 찾기
# 시작점보다 끝점을 찾자
# 시작점의 경우 암호가 이어지지 않을 경우나 다른 코드로 인식이 될 가능성
# 0001011//1100011// 01011101100110010111011011101101110110011001 (x)
# 0 001011110001101011101100110010111011011101101110110011001 애초에 매칭되는 코드가 없고..
# 00 //0101111 // 0001101 // 0111011 // 00110010111011011101101110110011001 (쭉 이어짐 )
# 반면 끝점은 어쩌피 모든 암호코드는 1로 끝나니 1에서부터 거꾸로 7개씩 묶는 것이 더 나을 것
# 맨 끝점에서 행 방향으로 -55하면 시작점
def find_start(arr, N, M):
    for y in range(N):
        for x in range(M-1, -1, -1):
            if arr[y][x] == 1:
                return y, x-55


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

        # 암호코드 검증
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