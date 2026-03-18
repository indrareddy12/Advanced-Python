class Solution:
    # Function to find the minimum number of jumps using recursion
    def jump(self, nums):
        return self.min_jumps(nums, 0)

    def min_jumps(self, nums, position):
        # If current position is at or beyond the last index, return 0
        if position >= len(nums) - 1:
            return 0

        # If jump length is 0, we are stuck
        if nums[position] == 0:
            return float('inf')

        min_step = float('inf')

        # Try every possible jump from this position
        for jump in range(1, nums[position] + 1):
            sub_result = self.min_jumps(nums, position + jump)
            if sub_result != float('inf'):
                min_step = min(min_step, 1 + sub_result)

        return min_step

# Driver code
if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    sol = Solution()
    print("Minimum number of jumps:", sol.jump(nums))
