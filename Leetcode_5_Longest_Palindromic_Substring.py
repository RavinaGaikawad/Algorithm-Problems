class Solution:
	def longestPalindrome(self, s: str) -> str:
		def expanAroundCenter(s, left, right):
			substring = ''
			max_length = 0

			while left >= 0 and right < len(s) and s[left] == s[right]:
				if right - left + 1 > max_length:
					max_length = right - left + 1
					substring = s[left: right+1]
				left -= 1
				right += 1

			return substring

		result = ''
		for i in range(len(s)):
			odd = expanAroundCenter(s, i, i)
			even = expanAroundCenter(s, i, i+1)

			if len(odd) > len(result):
				result = odd
			if len(even) > len(result):
				result = even

		return result
		
    '''
      T = O(N^2)
      S = O(1)
    '''
    
