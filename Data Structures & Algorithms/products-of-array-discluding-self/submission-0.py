class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output =[]
        left = 1
        right = 1
        stored_r = []
        stored_l = []

        for i in range(len(nums)):
            stored_l.append(left)
            left = left*nums[i]

        for i in range(len(nums) - 1, -1, -1):
            stored_r.append(right)
            right = right*nums[i]

        for i in range(len(nums)):
            output.append(stored_r[len(nums)-1-i]*stored_l[i])
        return(output)