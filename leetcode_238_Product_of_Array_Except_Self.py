class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        for i in range(1, n):
            ans[i] = ans[i-1] * nums[i-1]

        rightproduct = 1

        for i in range(n-1, -1, -1):
            ans[i] = ans[i] * rightproduct

            rightproduct *= nums[i]

        return ans
        
     """
      T = O(N)
      S = O(N)
     """
    
