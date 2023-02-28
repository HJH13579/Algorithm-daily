import sys
sys.stdin = open("input.txt", "r")

for tck in range(1, 11):
    _ = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]

    cnt = 0

    # 열 단위 검사
    # 시작은 무조건 1, 끝은 무조건 2
    # '12' 이렇게 올 때마다 cnt +1
    # stack 최적화 문제
    # 빈 스택일 때만 1이 나오면 push
    # 빈 스택이 아닐 때(1이 있을 때)만 2가 나오면 pop(빈 스택 만들어주기) & cnt +1
    # 이러면 나머지 모든 case들은 무시된다.
    for j in range(100):
        stk = []    # 열이 바뀔 때마다 stack 초기화

        for i in range(100):
            if not stk:
                if arr[i][j] == 1:
                    stk.append(1)
            else:
                if arr[i][j] == 2:
                    stk.pop()
                    cnt += 1

    print(f'#{tck} {cnt}')