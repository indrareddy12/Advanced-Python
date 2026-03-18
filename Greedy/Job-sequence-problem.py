# A class representing a Job with id, deadline, and profit
class Job:
    def __init__(self, id, dead, profit):
        # Job Id
        self.id = id      
        # Deadline of job
        self.dead = dead  
        # Profit if job is completed before or on deadline
        self.profit = profit  


def JobScheduling(arr, n):
    # Sort the jobs by profit in descending order
    arr.sort(key=lambda x: x.profit, reverse=True)

    # Find the maximum deadline among all jobs
    maxi = arr[0].dead
    for i in range(1, n):
        # Find the latest deadline
        maxi = max(maxi, arr[i].dead)  

    # Create an array to store the slots for the jobs
    slot = [-1] * (maxi + 1)

    countJobs = 0
    jobProfit = 0

    # Try to assign jobs to the slots
    for i in range(n):
        # Find a slot for the current job, starting from the job's deadline
        for j in range(arr[i].dead, 0, -1):
            # If the slot is available
            if slot[j] == -1:  
                # Assign the job to the slot
                slot[j] = i  
                # Increment the job count
                countJobs += 1  
                # Add the profit of the job
                jobProfit += arr[i].profit  
                break 

    # Return the number of jobs done and total profit
    return countJobs, jobProfit


# Driver code
if __name__ == "__main__":
    n = 4
    # Define the jobs with id, deadline, and profit
    arr = [Job(1, 4, 20), Job(2, 1, 10), Job(3, 2, 40), Job(4, 2, 30)]

    # Call the JobScheduling function
    ans = JobScheduling(arr, n)

    # Output the result
    print(ans[0], ans[1])
