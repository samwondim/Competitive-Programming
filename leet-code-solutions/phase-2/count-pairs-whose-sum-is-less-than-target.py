class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        answer = 0
        left, right = 0, len(nums) - 1
        nums.sort()
        
        while left < right:
            if nums[left] + nums[right] < target:
                answer += right - left
                left += 1
            else:
                right -= 1
                
        return answer