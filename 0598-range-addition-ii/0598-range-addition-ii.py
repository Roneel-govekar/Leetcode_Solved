class Solution():
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if ops:
            prei=[i[0] for i in ops ]
            prej=[i[1] for i in ops ]
            return min(prei)*min(prej)
        else:
            return m*n