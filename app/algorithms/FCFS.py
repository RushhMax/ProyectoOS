from app.core.Process import Process

class FCFS:  
    def __init__(self):
        self.__name__ = "First-Come, First-Served"

    def execute(self, processes):
        print("\nExecuting FCFS Algorithm\n")
        
        # Sort processes by arrival time
        processes.sort(key=lambda x: x.arrival_time)
        
        current_time = 0  # Track current CPU time

        for process in processes:
            #print(f"---- Executing {process.name} ----")
            
            # If the process hasn't arrived yet, idle the CPU until its arrival time
            if process.arrival_time > current_time:
                #print(f"CPU idle from time {current_time} to {process.arrival_time}.")
                current_time = process.arrival_time
            
            # Calculate the important times for each process
            process.start_time = current_time
            process.end_time = current_time + process.service_time
            process.response_time = process.start_time - process.arrival_time
            process.waiting_time = process.start_time - process.arrival_time
            process.turnaround_time = process.end_time - process.arrival_time
            
            # Advance the current time
            current_time = process.end_time
            
            # Display process state
            # print(f"Start Time: {process.start_time}")
            # print(f"End Time: {process.end_time}")
            # print(f"Waiting Time: {process.waiting_time}")
            # print(f"Turnaround Time: {process.turnaround_time}")
            # print(f"Response Time: {process.response_time}")
            # print("-----------------------------")
        
        # Print the summary table after all processes are executed
        print("\nSummary of Process Execution:")
        print("Process\t\t\t\tArrival Time\tService Time\tWaiting Time\tTurnaround Time\tResponse Time")
        for proc in processes:
            print(f"{proc.pid}\t\t\t\t{proc.arrival_time}\t\t{proc.service_time}\t\t{proc.waiting_time}\t\t{proc.turnaround_time}\t\t{proc.response_time}")
        
        print("\nAll processes have been executed.\n")

        # Prepare a summary to return
        summary = []
        for proc in processes:
            summary.append({
                "status": "COMPLETED",
                "pid": proc.pid,
                "name": proc.name,
                "arrival_time": proc.arrival_time,
                "service_time": proc.service_time,
                "start_time": proc.start_time,
                "end_time": proc.end_time,
                "waiting_time": proc.waiting_time,
                "turnaround_time": proc.turnaround_time,
                "response_time": proc.response_time,
            })

        return summary
