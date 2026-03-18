class Solution:
    // Function to find the minimum number of intervals to remove to make all intervals non-overlapping
    def eraseOverlapIntervals(self, intervals):
        
        # Total number of intervals
        n = len(intervals)
        
        # Track max valid non-overlapping subset
        max_valid = 0

        # Try all subsets using bitmasking
        for mask in range(1 << n):

            # Build current subset
            subset = []
            for i in range(n):
                if mask & (1 << i):
                    subset.append(intervals[i])

            # Sort the subset
            subset.sort()

            # Check if it is non-overlapping
            valid = True
            for i in range(1, len(subset)):
                if subset[i][0] < subset[i - 1][1]:
                    valid = False
                    break

            # Update max valid
            if valid:
                max_valid = max(max_valid, len(subset))

        # Return total - max valid
        return n - max_valid

# Driver code
if __name__ == "__main__":
    sol = Solution()
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    print("Minimum intervals to remove:", sol.eraseOverlapIntervals(intervals))
