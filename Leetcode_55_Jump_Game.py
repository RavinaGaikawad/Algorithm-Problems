class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest_right = 0
        for i, x in enumerate(nums):
            if i > farthest_right:
                return False

            farthest_right = max(farthest_right, i + x)

        return True

        '''
            T = O(N)
            S = O(1)
        '''
     
