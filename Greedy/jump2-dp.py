class Solution:
    // Function to compute the minimum number of jumps to reach the last index
    def jump(self, nums):
        # Length of input array
        n = len(nums)

        # Initialize DP array with infinity
        dp = [float('inf')] * n

        # It takes 0 jumps to reach the starting index
        dp[0] = 0

        # Traverse the array
        for i in range(n):
            for j in range(1, nums[i] + 1):
                if i + j < n:
                    # Update dp[jump position] with min jumps
                    dp[i + j] = min(dp[i + j], dp[i] + 1)

        # Return min jumps to reach end
        return dp[n - 1]

# Driver code
sol = Solution()
nums = [2, 3, 1, 1, 4]
print("Minimum jumps:", sol.jump(nums))
