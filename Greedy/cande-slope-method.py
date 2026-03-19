class Solution:
    #  Function to calculate the minimum number of candies 
    def candy(self, ratings):
        # Get number of children
        n = len(ratings)

        # Initially give 1 candy to each child
        candies = n

        # Start from second child
        i = 1

        while i < n:

            # Skip equal ratings
            if ratings[i] == ratings[i - 1]:
                i += 1
                continue

            # Initialize increasing slope counter
            peak = 0

            # Traverse strictly increasing ratings
            while i < n and ratings[i] > ratings[i - 1]:
                peak += 1
                candies += peak
                i += 1

            # Initialize decreasing slope counter
            valley = 0

            # Traverse strictly decreasing ratings
            while i < n and ratings[i] < ratings[i - 1]:
                valley += 1
                candies += valley
                i += 1

            # Remove overlapping candy at the peak
            candies -= min(peak, valley)

        # Return total candies required
        return candies


# Driver code
ratings = [1, 3, 6, 8, 9, 5, 3]
sol = Solution()
print("Minimum candies required:", sol.candy(ratings))
