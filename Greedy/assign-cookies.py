class Solution:
    # Function to find the maximum number of content students
    def findContentChildren(self, student, cookie):
        # Sort both arrays to apply the greedy strategy
        student.sort()
        cookie.sort()

        studentIndex = 0
        cookieIndex = 0

        # Try to assign cookies until any one list is fully processed
        while studentIndex < len(student) and cookieIndex < len(cookie):
            # If the cookie satisfies the student's greed
            if cookie[cookieIndex] >= student[studentIndex]:
                studentIndex += 1
            # Move to next cookie in both cases
            cookieIndex += 1

        # Number of students satisfied is equal to studentIndex
        return studentIndex

# Main execution
student = [1, 2, 3]
cookie = [1, 1]

# Create Solution object
solver = Solution()

# Get the number of content students and print it
result = solver.findContentChildren(student, cookie)
print("Maximum number of content students:", result)
