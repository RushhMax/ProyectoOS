class FCFS:
    def __init__(self, processes):
        self.queue = processes
    
    def execute(self):
        processes = self.queue
        processes.sort(key=lambda x: x.arrival_time)
        current_time = 0
        for process in processes:
            if process.arrival_time > current_time:
                current_time = process.arrival_time
            process.start_time = current_time
            process.end_time = current_time + process.burst_time
            current_time = process.end_time
        return true
