class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        [ 4*3*2, 1*4*3, 1*2*4, 1*2*3]

        example:
        [1, 2, 3, 4]
        '''

        l = [1] * len(nums)
        
        cur = 1
        # prefix for loop
        for i in range(len(nums) - 1):
            cur *= nums[i]
            l[i+1] *= cur
        
        cur = 1
        # suffix for loop
        for i in range(len(nums) - 1, 0, -1):
            cur *= nums[i]
            l[i-1] *= cur
        
        return(l)
