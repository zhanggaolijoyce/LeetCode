class Solution:
    def isHappy(self, n: int) -> bool:
        def get_num(n):
            s = 0
            while n:
                n, r = divmod(n, 10)
                s += r* r
            return s
        record = set()
        while True:
            n = get_num(n)
            if n == 1:
                return True
            if n in record:
                return False
            record.add(n)
