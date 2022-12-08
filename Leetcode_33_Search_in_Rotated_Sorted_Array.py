class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if target == nums[0]:
                return 0

        low = 0
        high = len(nums) - 1

        while low <= high:

            mid = (low + high) // 2

            if target == nums[mid]:
                return mid
            elif nums[mid] >= nums[low]:
                if target >= nums[low] and target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if target > nums[mid] and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

      """
        T = O(log N)
        S = O(1)
      """
      
