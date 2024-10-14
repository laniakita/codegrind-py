from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)
        nums.sort()
        mid = (n-1) // 2
        # ::2 == odds, 1::2 == evens
        nums[::2], nums[1::2] = nums[mid::-1], nums[:mid:-1]
        print(nums)

Solution().wiggleSort([1,5,1,1,6,4])        
