# 숫자를 엄청 크게 주거나 위치 교체 개수가 늘어나는 등 시간을 적게 줄 때를 대비한 풀이
# 말 그대로 규칙성을 파악해 구현한 풀이
# 좀 하드코딩(그래도 개선의 여지가 보임)
# 최댓값: 가장 높은 자릿수(가장 맨앞)에 가장 큰 숫자가 와야한다.
# 만약 가장 높은 자릿수에 가장 큰 숫자가 이미 와 있으면 다음 자릿수로 이동해서 판별 반복
# 최솟값은 전혀 반대 
# 다만 맨 앞엔 0이 오면 안 되는데, 이를 위해 맨 처음(cnt = 0) 판별 때 '0을 제외한 숫자열'을 따로 만들어
# 맨 앞이 최소인지 판별, 맞으면 교체하고 끝, 아니면 다음 자릿수로 넘기되 그 때부터 0을 포함한 판별 시작


import sys
sys.stdin = open("sample_input.txt", "r")

def find_min_index(lst):
    mn_idx = 0
    for n in range(len(lst)):
        if lst[mn_idx] >= lst[n]:
            mn_idx = n

    return mn_idx


def max_switch(lst):
    global max_string

    num = list(map(int, lst))

    if len(lst) == 0:
        return 0

    elif num[0] != max(num):
        mx_idx = 0
        for m in range(len(num)):
            if num[mx_idx] <= num[m]:
                mx_idx = m

        lst[0], lst[mx_idx] = lst[mx_idx], lst[0]

        while lst:
            max_string += lst.pop(0)
        return 0

    max_string += lst.pop(0)
    return max_switch(lst)

def min_switch(lst):
    global min_string
    global cnt

    num = list(map(int, lst))

    if len(lst) == 0:
        return 0

    elif num[0] != min(num):
        if cnt == 0:
            num_without_0 = list(map(int, string_without_0))
            if num_without_0[0] != min(num_without_0):
                min_idx = find_min_index(num_without_0)

                lst[0], lst[min_idx] = lst[min_idx], lst[0]

                while lst:
                    min_string += lst.pop(0)
                return 0

        else:
            mn_idx = find_min_index(num)

            lst[0], lst[mn_idx] = lst[mn_idx], lst[0]

            while lst:
                min_string += lst.pop(0)
            return 0

    cnt += 1
    min_string += lst.pop(0)
    return min_switch(lst)


T = int(input())

for tck in range(1, T+1):
    string1 = list(input())
    string2 = []
    for c in string1:
        string2.append(c)
    string_without_0 = []
    for w in string1:
        if w != '0':
            string_without_0.append(w)

    cnt = 0

    max_string = ''
    min_string = ''

    max_switch(string1)
    min_switch(string2)

    print(f'#{tck} {min_string} {max_string}')
