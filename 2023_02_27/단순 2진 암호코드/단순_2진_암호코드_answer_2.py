# 확장성을 위한 갯수를 활용한 풀이
# 1과 0의 개수를 cnt해서 구분
# [1] st에서 0과 1의 개수를 cnt
# 사실 4개 중 뒤에 3개만 뽑아 써도 구별이 된다.
# 개수를 cnts에 저장

# '0'과 '1'이 바뀔 때의 cnt
# for i in range(len(st)):
#     if st[old] != st[i]:
#         cnt.append(i-old) # 연속된 갯수
#         old = i

# [2] 개수를 암호로 변환
# for i in range(1, len(cnts), 4): # 4자리
#     pwd.append(dct[cnts[i:i+3]])

dct = {'211': 0, '221': 1, '122': 2, '411': 3, '132': 4, '231': 5, '114': 6, '312': 7, '213': 8, '112': 9}


def solve(arr):
    for st in arr:
        if '1' in st:  # '1'이 있는 경우 처리
            cnts = []
            old = 0
            # [1] 0과 1의 연속한 개수 저장
            for i in range(len(st)):
                if st[old] != st[i]:
                    cnts.append(i - old)
                    old = i
            # print(cnts)

            # [2] 개수를 디코딩해서 암호로 변환/저장
            pwd = []
            for i in range(1, len(cnts), 4):
                pwd.append(dct["".join(map(str, cnts[i:i + 3]))])
            # print(pwd)

            # [3] 검증(짝수위치*3 + 홀수위치 가 10의 배수)
            if (sum(pwd[0:8:2]) * 3 + sum(pwd[1:8:2])) % 10 == 0:
                return sum(pwd[0:8:2]) + sum(pwd[1:8:2])
            return 0


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    ans = solve(arr)
    print(f'#{tc} {ans}')
