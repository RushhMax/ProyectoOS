from app.core.Process import Process

class Priority:
    def __init__(self):
        self.__name__ = "Priority"

    def execute(self, processes):
        print("\nExecuting Priority Scheduling Algorithm\n")

        # Sort processes by priority (lower value = higher priority), breaking ties by arrival time
        processes.sort(key=lambda p: (p.priority, p.arrival_time))

        current_time = 0  # Track the current time

        for process in processes:
            # If the process hasn't arrived yet, idle the CPU
            if process.arrival_time > current_time:
                current_time = process.arrival_time

            # Calculate important times for each process
            process.start_time = current_time
            process.end_time = current_time + process.service_time
            process.response_time = process.start_time - process.arrival_time
            process.waiting_time = process.start_time - process.arrival_time
            process.turnaround_time = process.end_time - process.arrival_time

            # Advance the current time
            current_time = process.end_time

        # Print the summary table after all processes are executed
        print("\nSummary of Process Execution:")
        print("Process\t\tArrival Time\tService Time\tPriority\tWaiting Time\tTurnaround Time\tResponse Time")
        for proc in processes:
            print(f"{proc.pid}\t\t{proc.arrival_time}\t\t{proc.service_time}\t\t{proc.priority}\t\t{proc.waiting_time}\t\t{proc.turnaround_time}\t\t{proc.response_time}")

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
                "priority": proc.priority,
                "start_time": proc.start_time,
                "end_time": proc.end_time,
                "waiting_time": proc.waiting_time,
                "turnaround_time": proc.turnaround_time,
                "response_time": proc.response_time,
            })

        return summary
