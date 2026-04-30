class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        li =  set(nums)
        if (len(li) != len(nums)):
            return True

        return False