from datetime import datetime

class CPU:
    def __init__(self, cpu_id):
        self.cpu_id = cpu_id
        self.queue = []  # Cola de procesos asignados
        self.completed_processes = []  # Procesos completados por este CPU


    def add_process(self, process):
        """Añade un proceso a la cola de esta CPU."""
        self.queue.append(process)

    def execute_processes_at_time(self, current_time):
        """Ejecuta los procesos asignados en función del tiempo actual."""
        if self.queue:
            process = self.queue[0]
            if process.remaining_time > 0 and process.arrival_time <= current_time:
                process.remaining_time -= 1
                if process.remaining_time == 0:
                    process.status = 'completed'
                    process.end_time = current_time
                    process.turnaround_time = current_time - process.arrival_time
                    process.waiting_time = process.turnaround_time - process.service_time
                    self.completed_processes.append(self.queue.pop(0))
