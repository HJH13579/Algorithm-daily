import sys
sys.stdin = open("s_input.txt", "r")

# 이진법 변환 함수
def myBinary(num):
    if num == 0:
        return '0'
    elif num == 1:
        return '1'

    if num % 2 == 0:
        return myBinary(num // 2) + '0'
    else:
        return myBinary(num // 2) + '1'

# 무조건 4자리로 표현 == 부족한 부분만큼 '0'으로 채우는 함수
def make_it_four(str):
    if len(str) != 4:
        return '0'*(4-len(str)) + str
    else:
        return str

# 알파벳이 나타내는 숫자들을 딕셔너리로 형성
word_num = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

T = int(input())

for tck in range(1, T+1):
    N, string = map(str, input().split())

    ans = ''

    for x in string:
        if x.isdigit(): # 숫자이면
            ans += make_it_four(myBinary(int(x)))
        else:   # 문자이면(무조건 10 이상이므로 무조건 4자리)
            ans += myBinary(word_num[x])

    print(f'#{tck} {ans}')