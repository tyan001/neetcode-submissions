class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            guess = nums[mid]

            if guess == target:
                return mid
            elif guess < target:
                low = mid + 1   # target must be to the right
            else:
                high = mid - 1  # target must be to the left

        return -1