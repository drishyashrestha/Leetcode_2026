"""
2461. Maximum Sum of Distinct Subarrays With Length K


You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

The length of the subarray is k, and
All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15


Example 2:

Input: nums = [4,4,4], k = 3
Output: 0
"""


def max_sum_subarray(nums , k):

    i , j = 0, 0
    window_sum , best_sum = 0, 0
    freq = {}

    for j in range(len(nums)):
        window_sum += nums[j]
        freq[nums[j]] = freq.get(nums[j],0)+1

        # for duplicates
        while freq[nums[j]]>1:
            freq[nums[i]]-=1
            window_sum -= nums[i]
            i+=1
        # if window size is large
        while j-i+1>k:
            freq[nums[i]]-=1
            window_sum -= nums[i]
            i+=1

        if j-i+1 == k:
            best_sum = max(window_sum,best_sum)

    return best_sum

    




# print(max_sum_subarray([0,1,2,3,0,0],3))