# Class to group the solution method
class Solution:
    
    # Function to count minimum platforms needed
    def countPlatforms(self, n, arr, dep):

        # Initialize answer to 1
        ans = 1

        # Loop over all arrival times
        for i in range(n):

            # Initialize count of overlapping intervals
            count = 1

            # Check overlap with every other train
            for j in range(i + 1, n):

                # Check if there is overlap between train i and j
                if (arr[i] >= arr[j] and arr[i] <= dep[j]) or \
                   (arr[j] >= arr[i] and arr[j] <= dep[i]):
                    count += 1

            # Update maximum platform count
            ans = max(ans, count)

        return ans


# Main execution
arr = [900, 945, 955, 1100, 1500, 1800]
dep = [920, 1200, 1130, 1150, 1900, 2000]
n = len(arr)

# Create object and call the function
obj = Solution()
print("Minimum number of Platforms required", obj.countPlatforms(n, arr, dep))
