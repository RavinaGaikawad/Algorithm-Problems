class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [0] * (n+1) 
        
        def climb(i, n, memo):
            if i > n:
                return 0
            
            if i == n:
                return 1
            
            if memo[i] > 0:
                return memo[i]
            
            memo[i] =  climb(i+1, n, memo) + climb(i+2, n, memo)

            return memo[i]
        
        return climb(0, n, memo)
