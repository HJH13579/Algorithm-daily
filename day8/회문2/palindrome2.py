import sys

sys.stdin = open("input.txt", "r", encoding="UTF8")

def palindrome(ar1, ar2):
    ans = 1

    for x in range(100, 0, -1):
        for i in range(100):
            for j in range(100 - x + 1):
                # RunTime Error
                # if ar1[i][j:j + x] == ar1[i][j:j + x][::-1] or ar2[i][j:j + x] == ar2[i][j:j + x][::-1]:

                for y in range(x // 2):
                    if ar1[i][j + y] == ar1[i][x - (j+y)] or ar2[i][j + y] == ar2[i][x - (j+y)]:
                        ans = x
                        return ans

for tck in range(1, 11):

    _ = int(input())

    arr = [list(input()) for _ in range(100)]
    arr_t = list(map(list, zip(*arr)))

    result = palindrome(arr, arr_t)

    print(f'#{tck} {result}')