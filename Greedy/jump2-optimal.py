class Solution:
     #Function to compute the minimum number of jumps to reach the last index
    def jump(self, nums):
        # Initialize jump counter and bounds
        jumps = 0
        current_end = 0
        farthest = 0

        # Traverse through the array except the last element
        for i in range(len(nums) - 1):
            # Update the farthest index that can be reached from current index
            farthest = max(farthest, i + nums[i])

            # If we have reached the end of current range
            if i == current_end:
                # Increment jump counter
                jumps += 1

                # Move the range to the farthest position we can reach
                current_end = farthest

        # Return the minimum number of jumps
        return jumps
# Driver Code
if __name__ == "__main__":
    sol = Solution()
    nums = [2, 3, 1, 1, 4]
    print("Minimum jumps required:", sol.jump(nums))
