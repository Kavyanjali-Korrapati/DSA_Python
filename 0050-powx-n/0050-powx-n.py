class Solution(object):
    def myPow(self, x, n):
        exp=abs(n)
        result=1.0
        base=x

        while exp > 0:
            if exp%2 ==1:
                result*=base
            base *= base
            exp//=2
        if n<0:
            result= 1.0 / result
        return result