class Solution():
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        i=0
        if len(flowerbed)>3:
            while n>0 and i<=len(flowerbed)-3:
                #print(flowerbed[i])
                if flowerbed[i]==0 and flowerbed[i+1]==0 and i==0:
                    flowerbed[i]=1
                    
                    n-=1
                elif flowerbed[i+1]==0 and flowerbed[i+2]==0 and i==len(flowerbed)-3:
                    flowerbed[i+2]=1
                    
                    n-=1
                elif flowerbed[i]==0 and flowerbed[i+2]==0 and flowerbed[i+1]==0:
                    flowerbed[i+1]=1
                    
                    n-=1



                i+=1
        elif len(flowerbed )==1:
            if flowerbed[0]==0:
                n=0
        elif len(flowerbed )==2 and flowerbed[0]==0 and flowerbed[1]==0 and n==1:
            n-=1
        elif len(flowerbed )==3 and flowerbed[0]==0 and flowerbed[1]==0 and flowerbed[2]==0  and n<3:
            n=0
        elif len(flowerbed )==3 and flowerbed[0]==1 and flowerbed[1]==0 and flowerbed[2]==0  and n<2:
            n-=1
        elif len(flowerbed )==3 and flowerbed[0]==0 and flowerbed[1]==0 and flowerbed[2]==1  and n<2:
            n-=1
            
            
            
            
        return n==0          