"""
643. Maximum Average Subarray I

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000

"""

def findMaxAverage(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        window_sum =0
        max_sum =float('-inf')
        i,j= 0,0
        for j in range(len(nums)):
            window_sum += nums[j]
            
            while j-i+1 >k:
                window_sum-= nums[i]
                i+=1

            if j-i+1 ==k:
                max_sum = max(window_sum,max_sum)
        return max_sum/float(k)
    
# print(findMaxAverage([5],1))