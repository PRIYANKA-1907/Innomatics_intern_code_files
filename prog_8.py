class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        j = 0
        ans = []
        for i in range(0, len(nums), 1):
            j = nums[i] + j
            print(j)
            ans.append(j)
        return ans
