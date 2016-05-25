# https://leetcode.com/problems/longest-increasing-subsequence/
# 300. Longest Increasing Subsequence
# Given an unsorted array of integers, find the length of longest increasing subsequence.
# For example,
# Given [10, 9, 2, 5, 3, 7, 101, 18],
# The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.
# Your algorithm should run in O(n2) complexity.
# Follow up: Could you improve it to O(n log n) time complexity?
# 
# This Solution's time complexity is O(n log n).
# The main idea is use Binary Search.
# The relevant analysis can be found in my gitbook:
# 	https://railsgem.gitbooks.io/leetcode/content/300longest_increasing_subsequence.html
# 
# Written By Juno Chen 25/5/2016
def binarySearch(listB, number, length):
	begin = 0
	end = length -1
	while begin <= end:
		mid = begin + (end - begin) // 2
		if listB[mid] == number:
			return mid
		elif number > listB[mid]:
			begin = mid + 1
		else:
			end = mid - 1
	return begin

class Solution(object):

	def lengthOfLIS(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if len(nums) == 0 or nums is None:
			return 0
		B = []
		B.append(nums[0])
		for i in range(1, len(nums)):
			if nums[i] > B[-1]:
				B.append(nums[i])
			else:
				pos = binarySearch(B, nums[i], len(B))
				B[pos] = nums[i]
		return len(B)

s = Solution()
length = s.lengthOfLIS([])
print(length)