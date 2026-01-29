class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        distinct_val = set(nums)
        return not len(distinct_val)==len(nums)
