def isvalid(s: str) -> bool:
    # 定义括号的配对关系
    bracket_map = {')': '(', '}': '{', ']': '['}
    # 创建一个栈，用于存放左括号
    stack = []

    for c in s:
        # 左括号入栈
        if c in '({[':
            stack.append(c)
        # 右括号，与栈顶元素进行比对
        else:
            if not stack or stack[-1] != bracket_map[c]:
                return False
            stack.pop()

    return not stack

s = '([)]'
isvalid(s)
