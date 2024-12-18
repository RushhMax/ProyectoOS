from app.core.Process import Process

class FCFS:
    def __init__(self):
        self.queue = []
    
    def execute(self, processes):
        processes.sort(key=lambda x: x.arrival_time)
        current_time = 0
        for process in processes:
            if process.arrival_time > current_time:
                current_time = process.arrival_time
            process.start_time = current_time
            process.end_time = current_time + process.service_time
            current_time = process.end_time
        return True
