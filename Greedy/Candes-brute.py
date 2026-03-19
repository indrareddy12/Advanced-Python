class Solution:
    # Function to calculate the minimum number of candies 
    def candy(self, ratings):
        # Total number of children
        n = len(ratings)
        
        # Array to keep track of candies given to each child, initialized to 1
        candies = [1] * n
        
        # Repeat until no updates occur
        updated = True
        while updated:
            updated = False
            
            # Left to right pass to fix increasing ratings
            for i in range(1, n):
                if ratings[i] > ratings[i - 1] and candies[i] <= candies[i - 1]:
                    candies[i] = candies[i - 1] + 1
                    updated = True

            # Right to left pass to fix decreasing ratings
            for i in range(n - 2, -1, -1):
                if ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                    candies[i] = candies[i + 1] + 1
                    updated = True

        # Return total candies required
        return sum(candies)

# Driver code
if __name__ == "__main__":
    obj = Solution()
    ratings = [1, 0, 5]
    print("Minimum candies required:", obj.candy(ratings))
