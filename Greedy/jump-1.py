class JumpGame:
    # Function to determine if you can reach the last index
    def can_jump(self, nums):
        max_index = 0  # The farthest index we can currently reach

        # Traverse the array
        for i in range(len(nums)):
            if i > max_index:
                return False  # Cannot proceed further

            # Update farthest reachable index
            max_index = max(max_index, i + nums[i])

        # If loop completes, we can reach the last index
        return True


# Driver code
if __name__ == "__main__":
    nums = [4, 3, 7, 1, 2]
    print("Array representing maximum jump from each index:", nums)

    game = JumpGame()
    ans = game.can_jump(nums)

    if ans:
        print("It is possible to reach the last index.")
    else:
        print("It is not possible to reach the last ind
