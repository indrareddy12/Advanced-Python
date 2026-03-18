class Solution:
     // Function to find the minimum number of intervals to remove to make all intervals non-overlapping
    def eraseOverlapIntervals(self, intervals):
        # Sort intervals by their end time (greedy strategy)
        intervals.sort(key=lambda x: x[1])

        # Counter for intervals to remove
        count = 0

        # Track the end time of last accepted interval
        prev_end = intervals[0][1]

        # Traverse the rest of intervals
        for i in range(1, len(intervals)):

            # If current interval overlaps with previous
            if intervals[i][0] < prev_end:
                # Increment removal count
                count += 1
            else:
                # Update previous end to current interval's end
                prev_end = intervals[i][1]

        # Return number of intervals removed
        return count

# Driver code
if __name__ == "__main__":
    sol = Solution()

    # Sample input
    intervals = [[1, 3], [2, 4], [3, 5], [1, 2]]

    # Print result
    print("Minimum number of intervals to remove:", sol.eraseOverlapIntervals(intervals))
