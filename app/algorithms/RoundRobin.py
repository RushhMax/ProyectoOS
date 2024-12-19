class RoundRobin:
    def __init__(self, quantum):
        self.__name__ = "Round Robin"
        self.quantum = quantum

    def execute(self, process_queue):
        print("\nExecuting Round Robin Scheduling Algorithm\n")

        time = 0
        queue = []
        visited = [False] * len(process_queue)

        # Initialize attributes of each process
        for process in process_queue:
            process.start_time = None
            process.remaining_time = process.service_time
            process.waiting_time = 0
            process.turnaround_time = 0
            process.response_time = 0
            process.end_time = None

        while True:
            # Add processes that arrive at the current time to the queue
            for i, process in enumerate(process_queue):
                if process.arrival_time <= time and not visited[i]:
                    queue.append(process)
                    visited[i] = True
                    print(f"Process {process.name} entered the queue at time {time}.")

            if not queue:
                # If no processes are ready but some are incomplete, advance time
                if all(proc.remaining_time == 0 for proc in process_queue):
                    break
                time += 1
                continue

            current = queue.pop(0)

            # Execute the current process
            if current.remaining_time > self.quantum:
                # Process does not finish, executes for a quantum
                if current.start_time is None:
                    current.start_time = time
                    current.response_time = time - current.arrival_time

                time += self.quantum
                current.remaining_time -= self.quantum
                print(f"Executing {current.name} for {self.quantum} units. Remaining time: {current.remaining_time}")

                # Add new processes that arrived during the execution
                for i, proc in enumerate(process_queue):
                    if proc.arrival_time <= time and not visited[i]:
                        queue.append(proc)
                        visited[i] = True
                        print(f"Process {proc.name} entered the queue at time {time}.")

                # Reinsert the current process at the end of the queue
                queue.append(current)
            else:
                # Process finishes execution
                if current.start_time is None:
                    current.start_time = time
                    current.response_time = time - current.arrival_time

                time += current.remaining_time
                current.remaining_time = 0
                current.end_time = time
                current.waiting_time = current.end_time - current.service_time - current.arrival_time
                current.turnaround_time = current.end_time - current.arrival_time
                print(f"Process {current.name} completed at time {time}. Waiting time: {current.waiting_time}, Turnaround time: {current.turnaround_time}")

        # Print final summary
        print("\nSummary of Process Execution:")
        print("Process\tArrival Time\tService Time\tStart Time\tEnd Time\tWaiting Time\tTurnaround Time\tResponse Time")
        for proc in process_queue:
            print(f"{proc.name}\t\t{proc.arrival_time}\t\t{proc.service_time}\t\t{proc.start_time}\t\t{proc.end_time}\t\t{proc.waiting_time}\t\t{proc.turnaround_time}\t\t{proc.response_time}")

        # Prepare a detailed summary to return
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
                "response_time": proc.response_time,
            })

        return summary
