"""
49. Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:


"""




from collections import defaultdict

def groupanagrams(strs):
    """
        :type strs: List[str]
        :rtype: List[List[str]]
    """
    anagrams  = defaultdict(list)
    for word in strs:
        key = "".join(sorted(word))
        anagrams[key].append(word)
    return list(anagrams.values())

# print(groupanagrams([""]))
# big O (n *m log m) time complexity to better to O(n*m)



# Optimized version with freq map and tuple
def groupanagrams_optimized(strs):
    res =  defaultdict(list) #mapping charcount to list of Anagrams
    for s in strs:
        count = [0]* 26 # a ... z
        for c in s:
            count[ord(c)-ord("a")] +=1
        key = tuple(count)
        res[key].append(s)
    return res.values()



