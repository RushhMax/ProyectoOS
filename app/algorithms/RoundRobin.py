class RoundRobin:
    def __init__(self, processes):
        self.processes = processes
        self.quantum = 4
    
    def execute(self):
        time = 0
        queue = []
        visited = [False] * len(self.processes)

        while True:
            for i, process in enumerate(self.processes):
                if process.arrival_time <= time and not visited[i]:
                    queue.append(process)
                    visited[i] = True

            if not queue:
                if all(proc.remaining_time == 0 for proc in self.processes):
                    break

                time = time + 1
                continue

            current = queue.pop(0)

            if current.remaining_time > self.quantum:
                time = time + self.quantum
                current.remaining_time = current.remaining_time - self.quantum
                
                for i, proc in enumerate(self.processes):
                    if proc.arrival_time <= time and not visited[i]:
                        queue.append(proc)
                        visited[i] = True
                queue.append(current)

            else:
                time = time + current.remaining_time
                current.wait_time = time - current.service_time - current.arrival_time
                current.turnaround_time = current.service_time + current.wait_time
                current.remaining_time = 0
        
        return True