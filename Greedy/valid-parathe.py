class Solution:

    # Recursive function to check if the parenthesis string is valid
    def isValid(self, s, index, open_count):

        # If open parentheses count becomes negative, it's invalid
        if open_count < 0:
            return False

        # If we reach the end of the string, check if all opens are closed
        if index == len(s):
            return open_count == 0

        # Get the current character
        c = s[index]

        # If it's an opening bracket '(', increase open count
        if c == '(':
            return self.isValid(s, index + 1, open_count + 1)

        # If it's a closing bracket ')', decrease open count
        elif c == ')':
            return self.isValid(s, index + 1, open_count - 1)

        # If it's '*', try all three options:
        # 1. Treat '*' as empty string
        # 2. Treat '*' as '('
        # 3. Treat '*' as ')'
        else:
            return (self.isValid(s, index + 1, open_count) or
                    self.isValid(s, index + 1, open_count + 1) or
                    self.isValid(s, index + 1, open_count - 1))

# Driver code
if __name__ == "__main__":
    # Prompt the user for input
    s = input("Enter the string: ")

    # Create Solution object and call the recursive function
    sol = Solution()
    if sol.isValid(s, 0, 0):
        print("Valid parenthesis string")
    else:
        print("Invalid parenthesis string")
