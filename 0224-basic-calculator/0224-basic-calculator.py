class Solution:
    precedence_stack = {'(': 0, '+': 2, '-': 2, '*': 4, '/': 4, 'neg': 5}
    precedence_input = {'(': 6, ')': 0, '+': 1, '-': 1, '*': 3, '/': 3, 'neg': 5}
    operators = set("+-*/")

    def transform(self, s):
        output, stack = [], ['(']
        s += ')'
        prev_char = '('
        has_num, num = False, 0

        for char in s:
            if char == ' ':
                continue

            if char.isdigit():
                has_num = True
                num = num * 10 + int(char)
                prev_char = char
                continue

            if has_num:
                output.append(num)
                has_num, num = False, 0

            if char == '-' and (prev_char == '(' or prev_char in self.operators):
                char = 'neg'

            while self.precedence_stack[stack[-1]] >= self.precedence_input[char]:
                popped = stack.pop()
                if popped != '(':
                    output.append(popped)
                else:
                    break

            if char != ')':
                stack.append(char)

            prev_char = char

        return output

    def evaluate_postfix(self, postfix):
        stack = []
        for token in postfix:
            if token not in self.precedence_input:
                stack.append(token)
            elif token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))  # Integer division
            elif token == 'neg':
                stack.append(-stack.pop())
        return stack[0]

    def calculate(self, s):
        postfix = self.transform(s)
        return self.evaluate_postfix(postfix)
