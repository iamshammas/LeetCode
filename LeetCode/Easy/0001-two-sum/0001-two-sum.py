class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if j==i:
                    continue
                if (nums[i]+nums[j])==target:
                    print(i,j)
                    res = [i,j]
                    break
        return res