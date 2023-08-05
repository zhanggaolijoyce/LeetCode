class Solution:
    def isValid(self, s:str) -> bool:
        stack = []
        left = ["(", "[", "{"]
        right = [")", "]", "}"]
        for i in s:
            if i in left:
                stack.append(i)
            else:
                if stack != [] and left[right.index(i)] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if stack == []:
            return True
        return False
