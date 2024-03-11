class Solution(object):
    def reverse(self, x):
        flag = False
        x = str(x)
        INT32_MIN = -2**31
        INT32_MAX = 2**31-1
        if x[0]== '-':
            x = x[1:]
            flag = True
        sum=''
        n = len(x)
        for i in range(n-1,-1,-1):
            sum=sum+x[i]
        if flag:
            sum=int(sum)
            sum=-sum
        else:
            sum = int(sum)
        
        if sum > INT32_MAX or sum < INT32_MIN:
            return 0
        return sum        