# Class to hold solution logic
class Solution:
    # Function to get all meetings that can be scheduled
    def maxMeetings(self, start, end):
        # Store as (end, start, index)
        meetings = [(end[i], start[i], i + 1) for i in range(len(start))]

        # Sort by end time
        meetings.sort()

        result = []
        last_end = -1

        # Traverse sorted meetings
        for e, s, idx in meetings:
            # If meeting can be scheduled
            if s > last_end:  
                # Store index
                result.append(idx)  
                # Update last end time
                last_end = e  
        return result


# Main driver code
if __name__ == "__main__":
    start = [1, 3, 0, 5, 8, 5]
    end   = [2, 4, 6, 7, 9, 9]

    sol = Solution()
    res = sol.maxMeetings(start, end)
    print(res)
