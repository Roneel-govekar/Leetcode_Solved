class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        array=[]
        roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for i in range(len(s)):
            print(s[i])
            array.append(roman[s[i]])
            if i+1<len(s):
                if roman[s[i]]<roman[s[i+1]]:
                    array.append(roman[s[i+1]]-roman[s[i]])
                    array.append(-roman[s[i+1]])
                    array.append(-roman[s[i]])
                    print(roman[s[i+1]])
                    
                    i=i+1
        print(array)
        summation=sum(array)
        return summation