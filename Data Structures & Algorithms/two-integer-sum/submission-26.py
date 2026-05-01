class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        paired = []

        for i in range(len(nums)):
            paired.append( (nums[i], i) )

        copy = sorted(paired)

        left = 0
        right = len (nums) - 1

        while ( True ):
            if ( copy[left][0] + copy[right][0] == target  ):
                break
            elif (copy[left][0] + copy[right][0] > target):
                right -= 1
            elif ( copy[left][0] + copy[right][0] < target):
                left += 1
        return sorted([copy[left][1], copy[right][1]])
    

            
