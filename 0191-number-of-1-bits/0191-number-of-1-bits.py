class Solution():
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        n=bin(n)
        n=str(n)
        print(n)
        for i in n:
            if i=="1":
                print()
                count+=1
        
        return count