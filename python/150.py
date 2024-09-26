class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch.strip("-").isdigit():
                stack.append(int(ch))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if ch == "+":
                    stack.append(op1+op2)
                elif ch == "-":
                    stack.append(op1-op2)
                elif ch == "*":
                    stack.append(op1*op2)
                elif ch == "/":
                    stack.append(int(op1/op2))
        return stack[0]
