import sys
sys.stdin = open("s_input.txt", "r")

def parentheses(lst):

    cnt = 0
    for z in lst:
        if z == '+' or z == '-' or z == '*' or z == '/':
            cnt += 1

    grouped_lst = [0] * (len(lst) + 2 * cnt)

    for i in range(1, len(lst)-1):
        if lst[i] == '*' or lst[i] == '/':



    return cnt

T = int(input())

for tck in range(1, T + 1):

    formula_lst = list(input())

    # [1] 우선순위에 따라 괄호를 사용하여 다시 표현
    # 9+5*2+1+3*3*7*6
    # (((9+(5*2))+1)+(((3*3)*7)*6))

    print(f'#{tck} {parentheses(formula_lst)}')