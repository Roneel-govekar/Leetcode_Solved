class Solution():
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        
        n=[i for i in score]
        #n=score.copy()
       
        score.sort(reverse=True)
        ans=[]
        for i in n:
            index=score.index(i)
            print(index)
            if index==0:
                ans.append("Gold Medal")
            elif index==1:
                ans.append("Silver Medal")
            elif index==2:
                ans.append("Bronze Medal")
            else:
                ans.append(str(index+1))
        
        return ans