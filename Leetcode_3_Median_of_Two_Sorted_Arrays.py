class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x = len(nums1)
        y = len(nums2)

        if x > y:
            return self.findMedianSortedArrays(nums2, nums1)

        low = 0
        high = x

        while low <= high:
            px = (low + high) // 2
            py = ((x + y + 1) // 2) - px

            maxLeftX = float('-inf') if px == 0 else nums1[px - 1]
            minRightX = float('inf') if px == x else nums1[px]

            maxLeftY = float('-inf') if py == 0 else nums2[py - 1]
            minRightY = float('inf') if py == y else nums2[py]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (x + y) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:
                high = px - 1
            else:
                low = px + 1

  '''
    T = O(log min(m,n))
    S = O(1)
  '''
  
