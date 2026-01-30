class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_z_index = 0
        for num in nums:
            if num !=0:
                nums[non_z_index]=num
                non_z_index +=1
            
        while non_z_index<len(nums):
            nums[non_z_index]=0
            non_z_index +=1
