class ShortestJobFirst:
    # Method to calculate average waiting time
    def calculate_average_wait_time(self, jobs):
        # Sort jobs in ascending order (Shortest Job First)
        jobs.sort()

        wait_time = 0   # Stores cumulative waiting time
        total_time = 0  # Tracks elapsed execution time
        n = len(jobs)   # Number of jobs

        # Iterate through each job
        for job in jobs:
            wait_time += total_time   # Add current total time to waiting time
            total_time += job         # Execute current job

        # Return the average waiting time
        return wait_time / n


# Driver code
if __name__ == "__main__":
    jobs = [4, 3, 7, 1, 2]
    print("Array Representing Job Durations:", jobs)

    sjf = ShortestJobFirst()
    ans = sjf.calculate_average_wait_time(jobs)

    print("Average waiting time:", ans)
