T = int(input())

dic = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}    # 숫자: 이동방향 딕셔너리

for tck in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False]*N for _ in range(N)] # 이미 방문한 지역을 표시하기 위한 arr

    lst = []

    i = 0   # 시작 위치는 항상
    j = 0   # 왼쪽 맨 윗 칸에서 출발

    while visited[i][j] == False:   # 방문을 안 한 지역이면 (이미 방문을 한 지역까지 이동할 때까지 반복)
        for x in dic.keys():
            if arr[i][j] == x:  # 이동 방향 숫자

                if not lst: # lst이 빈 리스트이면(처음 시작)
                    lst.append(arr[i][j])   # 무조건 추가
                elif lst[-1] != arr[i][j]:  # lst가 비어있지 않고(IndexError) 리스트 마지막 요소가 추가할 요소와 같지 않다면,
                    lst.append(arr[i][j])   # 추가
                # 리스트 마지막 요소와 추가할 요소가 같다면 추가 X

                visited[i][j] = True    # 방문했다고 표시

                i = i + dic[x][0]   # 위치 이동
                j = j + dic[x][1]

    print(f'#{tck}', end= ' ')
    print(*lst)