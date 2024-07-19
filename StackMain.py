from Stack import Stack

def main():
    '''This is a docstring'''
    with open('data.txt', 'r') as read_file:
        for line_number, line in enumerate(read_file):
            if line_number != 0:
                print("\n\n")
            print(f"infix: {line}", end='')
            postfix = in2post(line)
            print(f"postfix: {postfix}")
            eval = eval_postfix(postfix)
            print(eval)
            print(eval_postfix("1 +"))

def in2post(infix: str):
    '''This is a docstring'''
    infix = infix.replace(" ", "")
    postfix_stack = Stack()
    nums = ['0','1','2','3','4','5','6','7','8','9']
    operators = {'+':0,'-':0,'*':2,'/':2}
    ret = ''

    for char in infix:
        if char == "\n":
            continue
        if char == "(":
            postfix_stack.push(char)
        elif char in nums:
            ret += char
            ret += ' '
        elif char in operators:
            while not postfix_stack.is_empty() and postfix_stack.top() in operators and operators[postfix_stack.top()] >= operators[char]:
                ret += postfix_stack.pop()
                ret += ' '
            postfix_stack.push(char)
        elif char == ")":
            if postfix_stack.is_empty():
                raise SyntaxError("Invalid infix expression: Unmatched closing parenthesis")
            ret += postfix_stack.pop()
            ret += ' '
            while postfix_stack.top() != '(':
                if postfix_stack.is_empty():
                    raise SyntaxError("Invalid infix expression: Unmatched closing parenthesis")
                ret += postfix_stack.pop()
                ret += ' '
            postfix_stack.pop()  # Pop '('
        else:
            raise SyntaxError("Invalid character in infix expression")

    while not postfix_stack.is_empty():
        if postfix_stack.top() == '(':
            raise SyntaxError("Invalid infix expression: Unmatched opening parenthesis")
        ret += postfix_stack.pop()
        ret += ' '

    return ret[:-1]

def eval_postfix(postfix: str):
    operands = ['0','1','2','3','4','5','6','7','8','9']
    operators = ['+','-','*','/']
    eval_stack = Stack()
    for char in postfix:
        if char in operands:
            eval_stack.push(float(char))
        if char in operators and eval_stack.size() > 1:
            if eval_stack.size() < 2:
                raise SyntaxError
            op_2 = eval_stack.pop()
            op_1 = eval_stack.pop()
            eval_stack.push(calculate(op_1,op_2,char))
    if eval_stack.size() != 1:
        raise SyntaxError("Invalid postfix expression: Extra operands")
    return float(eval_stack.pop())

def calculate(op_1: float, op_2: float, operator: str):
    operation = {'+': op_1 + op_2,'-': op_1 - op_2, '*':op_1 * op_2, '/': op_1 / op_2}
    return operation[operator]



if __name__ == "__main__":
    main()
