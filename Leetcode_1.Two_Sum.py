class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict_nums = {}
        
        for idx, num in enumerate(nums):
            dict_nums[num] = idx
        
        for idx, num in enumerate(nums):
            if target - num in dict_nums and idx != dict_nums[target - num]:
                return [idx, dict_nums[target - num]]
            
            
    """
    T = O(N)
    S = O(N)
    """
