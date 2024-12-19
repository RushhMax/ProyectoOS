class SJF:
    def __init__(self):
        self.__name__ = "Shortest Job First (SJF)"

    def execute(self, process_queue):
        print("\nExecuting Shortest Job First (SJF) Scheduling Algorithm\n")
        
        # Sort processes by burst time (shortest job first), breaking ties by arrival time
        process_queue.sort(key=lambda p: (p.service_time, p.arrival_time))

        current_time = 0  # Track current time

        for proc in process_queue:
            # If the process arrives after the current time, idle the CPU
            if proc.arrival_time > current_time:
                current_time = proc.arrival_time

            # Calculate important times for the process
            proc.start_time = current_time
            proc.end_time = current_time + proc.service_time
            proc.turnaround_time = proc.end_time - proc.arrival_time
            proc.waiting_time = proc.turnaround_time - proc.service_time
            
            # Advance the current time
            current_time = proc.end_time

            # Print process details
            print(f"Process {proc.pid} executed:\n"
                  f"Start Time: {proc.start_time}, End Time: {proc.end_time},\n"
                  f"Waiting Time: {proc.waiting_time}, Turnaround Time: {proc.turnaround_time}")
        
        # Prepare a summary to return
        summary = []
        for proc in process_queue:
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
            })

        return summary
