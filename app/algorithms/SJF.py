class SJF:
    def __init__(self):
        self.__name__ = "Shortest Job First (SJF)"

    def execute(self, process_queue):
        print("\nExecuting Shortest Job First (SJF) Scheduling Algorithm\n")
        
        # Sort processes by burst time (shortest job first)
        scheduled_processes = sorted(process_queue, key=lambda p: p.service_time)

        current_time = 0  # Track current time

        for proc in scheduled_processes:
            # If the process arrives after the current time, idle the CPU
            if proc.arrival_time > current_time:
                #print(f"CPU idle from time {current_time} to {proc.arrival_time}")
                current_time = proc.arrival_time

            # Execute the process
            #print(f"---- Executing {proc.name} ----")
            #print(f"Start Time: {current_time}")
            #print(f"Burst Time: {proc.service_time}")
            #print(f"End Time: {current_time + proc.service_time}")
            
            # Calculate important times for the process
            proc.start_time = current_time
            proc.end_time = current_time + proc.service_time
            proc.turnaround_time = proc.end_time - proc.arrival_time
            proc.waiting_time = proc.turnaround_time - proc.service_time
            
            # Advance the current time
            current_time = proc.end_time
            
            # Process completion info
            #print(f"Process {proc.name} completed at time {proc.end_time}")
            #print("-----------------------------")

        # Print the summary table after all processes are executed
        print("\nSummary of Process Execution:")
        print("Process\t\t\t\tArrival Time\tService Time\tWaiting Time\tTurnaround Time")
        for proc in scheduled_processes:
            print(f"{proc.pid}\t\t\t\t{proc.arrival_time}\t\t{proc.service_time}\t\t{proc.waiting_time}\t\t{proc.turnaround_time}")
        
        print("\nAll processes have been executed.\n")
