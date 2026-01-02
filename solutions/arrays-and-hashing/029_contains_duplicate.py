
"""
219. Contains Duplicate II
Given an integer array nums and an integer k, return true if there are two distinct indices i and j
in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""

def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        last_seen = {}

        for i in range(len(nums)):
            if nums[i] in last_seen:
                if i - last_seen[nums[i]] <= k:
                    return True
            last_seen[nums[i]] = i

        return False