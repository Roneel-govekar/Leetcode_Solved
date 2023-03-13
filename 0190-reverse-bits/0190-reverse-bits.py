class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n=bin(n)
        n=str(n)
        n=("0"*(32-len(n)+2))+n[2:]
        #print(n)
        n=list(n)
        n.reverse()
        #print(n)
        n=''.join(n)
        new=0
        for i in range(len(n)):
            new=int(int(n[i])*(2**(len(n)-i-1)))+new
           
        return new