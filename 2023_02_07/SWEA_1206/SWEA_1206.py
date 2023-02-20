import sys

sys.stdin = open("s_input.txt", "r")

for task in range(1, 11):

    try:
        N = int(input())
        M = list(map(int, input().split()))

        building = {}  # 건물의 위치(x축)를 key로, 건물의 높이(y축)를 value로 하는 딕셔너리

        for x in range(N):
            building[x] = M[x]  # x번째 빌딩은 M[x]층

        sum_light_floor = 0

        for n in range(2, N - 2):  # n-2, n-1, n, n+1, n+2 로 좌우 2칸까지 빌딩과 높이 비교
            if building[n] <= building[n - 2] or building[n] <= building[n - 1] or building[n] <= building[n + 1] or \
                    building[n] <= building[n + 2]:  # n번째 빌딩 좌우 2칸까지 어느 하나라도 더 높으면 조망층 0개
                pass
            else:
                lst_light_floor = [building[n] - building[n - 2], building[n] - building[n - 1],
                                    building[n] - building[n + 1],
                                    building[n] - building[n + 2]]  # 가장 작은 값이 조망층 개수, sorting

                min_floor = 255

                for floor_num in lst_light_floor:
                    if min_floor > floor_num:
                        min_floor = floor_num

                sum_light_floor = sum_light_floor + min_floor  # 조망층 합

        print(f'#{task} {sum_light_floor}')

    except EOFError:
        break