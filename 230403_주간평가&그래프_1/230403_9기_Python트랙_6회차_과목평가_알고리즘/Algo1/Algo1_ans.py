# [1] 한 개의 변수(bits)에 저장
# [2] bit 단위로 체크
# bits(input(), 16)
# [3] 연속 개수 cnt -> max 갱신 (cnt, ans = 0)

import sys
sys.stdin = open("algo1_sample_in.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    bits = int(input(),16)

    cnt = ans = 0
    for i in range(4*N):
        if bits & (1<<i):
            cnt += 1
            ans = max(ans, cnt)
        else:
            cnt=0

    print(f'#{test_case} {ans}')