class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        d = {
            "+": lambda x,y: x+y,
            "-": lambda x,y: x-y,
            '*': lambda x,y: x*y,
            "/": lambda x,y: int(x/y),
        }
        for ele in tokens:
            if ele == "+" or ele == "-" or ele == "*" or ele == "/":
                op2 = stack.pop()
                op1 = stack.pop()
                res = d[ele](op1,op2)
                stack.append(res)
            else:
                stack.append(int(ele))
        return stack[0]
