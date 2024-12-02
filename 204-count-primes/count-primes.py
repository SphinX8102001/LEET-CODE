class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        ListOfPrimes = [True for i in range(n)]
        if len(ListOfPrimes)>=1:
            ListOfPrimes[0] = False
            if len(ListOfPrimes)>=2:
                ListOfPrimes[1] = False
        p = 2
        while (p * p <= n):
            if (ListOfPrimes[p] == True):
                for i in range(p * p, n, p):
                    ListOfPrimes[i] = False
            p += 1
        # return ListOfPrimes
        count = 0 
        for i in ListOfPrimes:
            if i == True:   
                count +=1
        return count        