class Priority:
    def __init__(self):
        self.__name__ = "Priority"

    def execute(self, process_queue):
        print("\nExecuting Priority Scheduling Algorithm\n")
        
        # Sort processes by priority (lower value = higher priority), breaking ties by arrival time
        process_queue.sort(key=lambda p: (p.priority, p.arrival_time))
        
        current_time = 0  # Track the current time

        for process in process_queue:
            #print(f"---- Executing {process.name} ----")
            
            # If the process hasn't arrived yet, idle the CPU
            if process.arrival_time > current_time:
                #print(f"CPU idle from time {current_time} to {process.arrival_time}.")
                current_time = process.arrival_time
            
            # Calculate important times for each process
            process.start_time = current_time
            process.end_time = current_time + process.service_time
            process.response_time = process.start_time - process.arrival_time
            process.waiting_time = process.start_time - process.arrival_time
            process.turnaround_time = process.end_time - process.arrival_time
            
            # Advance the current time
            current_time = process.end_time
            
            # Display the process details
            # print(f"Priority: {process.priority}")
            # print(f"Start Time: {process.start_time}")
            # print(f"End Time: {process.end_time}")
            # print(f"Waiting Time: {process.waiting_time}")
            # print(f"Turnaround Time: {process.turnaround_time}")
            # print(f"Response Time: {process.response_time}")
            # print("-----------------------------")
        
        # Print the summary table after all processes are executed
        print("\nSummary of Process Execution:")
        print("Process\t\t\t\tArrival Time\tService Time\tPriority\tWaiting Time\tTurnaround Time\tResponse Time")
        for proc in process_queue:
            print(f"{proc.pid}\t\t\t\t{proc.arrival_time}\t\t{proc.service_time}\t\t{proc.priority}\t\t{proc.waiting_time}\t\t{proc.turnaround_time}\t\t{proc.response_time}")
        
        print("\nAll processes have been executed.\n")
