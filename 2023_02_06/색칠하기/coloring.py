import sys

sys.stdin = open("s_input.txt", "r")

T = int(input())

for tck in range(1, T+1):

    N = int(input())

    arr = list(int, input().split())

    # 색 입력을 표시, 겹치는 처리 (+= color)
    # R(1), B(2) 모두 색칠 시 '3' 출력


    # 전체를 순회하며 '== 3' 인 값의 개수 cnt

    print(f'#{tck} {count_num}')







# 같은 색인 영역이 겹칠 수 있다면?
# 여러번 칠해진다
# color 값 1, 2, 3, 4, 5
# table