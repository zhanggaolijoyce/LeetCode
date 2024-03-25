class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for s, e in intervals[1:]:
            s1, e1 = res[-1]
            if s1<=s<=e1:
                m1 = min(s1, s)
                m2 = max(e1, e)
                res[-1] = [m1, m2]
            else:
                res.append([s, e])

        return res
