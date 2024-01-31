class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        ls = [0]*l

        q = deque()
        for i in range(l-1, -1, -1):
            if not q:
                q.append((temperatures[i], i))
                continue

            while q and temperatures[i] >= q[0][0]:
                q.popleft()

            if not q:
                q.append((temperatures[i], i))
            else:
                ls[i] = q[0][1]-i
                q.appendleft((temperatures[i], i))
        return ls
