class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbor(code):
            neighbor = []
            for i in range(4):
                for j in (-1, 1):
                    neighbor.append(code[:i] + str((int(code[i])+j)%10) + code[i+1:])
            return neighbor

        deadSet = set(deadends)
        visited = set()
        dq = deque()
        dq.append(["0000", 0])

        while dq:
            code, step = dq.popleft()
            if code in visited or code in deadSet:
                continue
            if code == target:
                return step
            visited.add(code)
            for code1 in neighbor(code):
                if code1 in visited or code1 in deadSet:
                    continue
                else:
                    dq.append([code1, step+1])
        return -1
