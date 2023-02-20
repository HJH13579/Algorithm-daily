import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())

for tck in range(1, T + 1):

    lst = list(map(str, input().split()))

    stk = []

    # error 조건
    # [1] pop을 할 stack 개수 부족(2개 미만) & 모두 완료 했을 때 stack에 데이터가 남아있을 때
    # [2] stack할 개수 부족 == 연산자 >> 숫자 & stack에 데이터가 남아돈다 == 연산자 << 숫자
    #     결국 숫자 갯수가 연산자 개수보다 항상 1개 더 많아야 한다. 그 외의 모든 경우 error

    cnt_digit = 0

    cnt_operator = -1

    for y in lst:
        if y.isdigit():
            cnt_digit += 1
        else:
            cnt_operator += 1

    if cnt_digit != cnt_operator + 1:
        result = 'error'

    # 숫자 개수 == 연산자 개수 + 1 일 때
    else:
        for x in lst:

            if x.isdigit(): # 숫자일 경우
                stk.append(x)   # stack에 push

            else:   # 숫자가 아닌 경우 = 연산자인 경우

                if x == '.':    #
                    result = stk.pop()
                    # break # 조건에선 코드가 항상 '.'로 끝난다는 조건을 줬지만, 만약 . 이후에도 있을 수 있을 경우 break 필요

                else:   # pop할 stack 순서 주의! op1이 항상 앞에, op2가 항상 뒤에 올 숫자다!
                    op2 = int(stk.pop())
                    op1 = int(stk.pop())
                    op3 = 0

                    if x == '+':
                        op3 = op1 + op2
                    elif x == '-':
                        op3 = op1 - op2
                    elif x == '*':
                        op3 = op1 * op2
                    elif x == '/':
                        op3 = op1 // op2

                    stk.append(op3)

    print(f'#{tck} {result}')