stack = [0] * 100
top = -1
susik = '6528-*2/+'
for x in susik:
    if x not in '+-/*':
        top += 1
        stack[top] = int(x)
    else:
        op2 = stack[top]
        top -= 1
        op1 = stack[top]
        top -= 1
        if x == '+':  # op1+op2
            stack[top] =  op1 + op2
        elif x == '-':
            stack[top] = op1 - op2
        elif x == '*':
            stack[top] = op1 * op2
        elif x == '/':
            stack[top] = op1 // op2

print(stack[top])

# ---------------------------------------------------
# input : (6+5*(2-8)/2)
stack = [0] * 100
top = -1
icp = {'(' : 3, '*' : 2, '/' : 2, '+' : 1, '-' : 1}
isp = {'(' : 0, '*' : 2, '/' : 2, '+' : 1, '-' : 1}
fx = '(6+5*(2-8)/2)'
susik = ''
for x in fx:
    # 하나씩 읽어오기
    # 피연산자 vs 연산자
    # 피연산자라면 출력
    if x not in '(+-*/)':
        susik += x
    elif x == ')':           # '('까지 pop()
        while stack[top] != '(': # peek
            susik += stack[top]
            top -= 1
        top -= 1             # '(' 버리는 동작
    else:        # '(+-*/'
        if top == -1 or isp[stack[top]] < icp[x]: # 토큰의 우선순위가 더 높으면
            top += 1
            stack[top] = x
        elif isp[stack[top]] >= icp[x]:
            while top > -1 and isp[stack[top]] >= icp[x]:
                susik += stack[top]
                top -= 1
            top += 1    # push
            stack[top] = x



# -------------------------------------------------------

exp = '(6+5*(2-8)/2)'
stack = []
post_exp = ''
# 우선 순위를 비교하기 위한 딕셔너리 생성, ()가 없다면 1개만 만들면 됨.
icp = {'(' : 3, '*' : 2, '/' : 2, '+' : 1, '-' : 1}
isp = {'(' : 0, '*' : 2, '/' : 2, '+' : 1, '-' : 1}

for c in exp:
    # 하나씩 읽어오기
    # 피연산자라면 출력
    # 연산자라면 우선순위에 따라서 스택에 넣거나 출력
    if c in '(+-*/)':  # 연산자
        if c == ')':
            while stack[-1] != '(':
                post_exp += stack.pop()
            stack.pop()    # 여는 괄호 버리기
            continue       # 다음 토큰 읽어오기

        if not stack:
            stack.append(c)

        # 스택의 top 연산자 보다 우선 순위가 높으면 그냥 넣기
        elif isp[stack[-1]] < icp[c]:     # stack[-1]의 우선순위보다 c의 우선순위가 높으면
            stack.append(c)
        else:
            # 같거나 높으면 스택에 있는 거 다 뺌
            # 나보다 우선순위가 낮은 게 스택에 들어있으면 들어감. 그 때까지 계속 뺌
            while stack and isp[stack[-1]] >= icp[c]:
                post_exp += stack.pop()
            stack.append(c)
    else:
        post_exp += c

while stack:  # 스택에 남아있는 연산자 출력
    post_exp += stack.pop()

print(post_exp)