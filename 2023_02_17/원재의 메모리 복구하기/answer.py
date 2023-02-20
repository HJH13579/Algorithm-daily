# 항상 0으로 채워져서 시작하기 때문에, 맨 앞에 칸 하나를 더 만들어서 초기값 0 할당
# 앞의 값과 다른 경우 ans += 1

import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    st = '0' + input()
    ans = 0
    for i in range(1, len(st)):
        if st[i - 1] != st[i]:
            ans += 1

    print(f'#{test_case} {ans}')