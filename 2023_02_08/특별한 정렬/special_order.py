import sys

sys.stdin = open("s_input.txt", "r")

T = int(input())

def selectionsort(lst, n):
    for i in range(n - 1):
        min_idx = i

        for j in range(i+1, n):
            if lst[min_idx] > lst[j]:
                min_idx = j

        lst[i], lst[min_idx] = lst[min_idx], lst[i]

    return lst

for tck in range(1, T+1):

    N = int(input())

    arr = list(map(int, input().split()))

    new_arr = [0] * 10

    for x in range(5):
        new_arr[2 * x] = selectionsort(arr, N)[(N - 1) - x]
        new_arr[2 * x + 1] = selectionsort(arr, N)[(x)]

    print(f'#{tck}', *new_arr)