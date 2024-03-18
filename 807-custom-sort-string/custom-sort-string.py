class Solution:
    def customSortString(self, order: str, s: str) -> str:
        sum=""
        sum2=""
        for i in order:
            for j in s:
                if j == i:
                    sum+=j
        for i in s:
            if i not in sum:
                sum2+=i
        sum2 = ''.join(sorted(sum2))
        sum=sum+sum2
        return sum