import sys
sys.stdin = open("s_input.txt", "r")

pri_operator = {'+': 1, '*': 2} # 연산자 간의 우선순위 지정(딕셔너리 형식)

T = int(input())

for tck in range(1, T + 1):
    input_string = input()

    changed_string = ''
    stk = []

    # 숫자가 나오면 그대로 changed_sting에 추가
    # 연산자가 나오면 stack에 push/pop -> 우선순위 고려

    for i in range(len(input_string)):
        if input_string[i].isdigit():   # 숫자일 때
            changed_string += input_string[i]
        else:   # 연산자일 때
            if not stk: # stack가 비어있을 때
                stk.append(input_string[i])
            else:   # stack에 연산자가 있을 때
                if pri_operator[input_string[i]] > pri_operator[stk[-1]]:   # stack의 top이 연산자보다 우선순위가 낮을 경우
                    stk.append(input_string[i]) # 그냥 push
                else:
                    while stk and pri_operator[input_string[i]] <= pri_operator[stk[-1]]:   # stack에 연산자 있는 경우 & stack의 top이 연산자보다 우선순위가 높거나 같을 경우 (같은 연산자여도 앞에 나온 것이 더 우선순위가 높기 때문에)
                        changed_string += stk.pop() # 우선 순위가 낮은게 나올 때까지 pop하여 방정식에 추가
                    stk.append(input_string[i]) # 나오면 push

    while stk:  # 모든 조건 수행 후 stack에 연산자가 남아있으면
        changed_string += stk.pop() # 남김 없이 모두 방정식에 추가

    print(f'#{tck} {changed_string}')