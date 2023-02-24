import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for tck in range(1, T+1):
    [x1, y1, x2, y2] = list(map(int, input().split()))
    N = int(input())
    lst_vertex = [(x1, y1), (x1, y2), (x2, y2), (x2, y1)]
    lst_dot = []
    for _ in range(N):
        x, y = map(int, input().split())
        lst_dot.append((x,y))

    cnt_outside = 0
    cnt_inside = 0
    cnt_side = 0

    for k in lst_dot:
        if x1 < k[0] < x2 and y1 < k[1] < y2:
            cnt_inside += 1
        elif ((x1 == k[0] or x2 == k[0]) and (y1 <= k[1] <= y2)) or ((y1 == k[1] or y2 == k[1]) and (x1 <= k[0] <= x2)):
            cnt_side += 1
        else:
            cnt_outside += 1

    print(f'#{tck} {cnt_inside} {cnt_side} {cnt_outside}')