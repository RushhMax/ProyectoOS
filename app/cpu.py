from datetime import datetime

class CPU:
    def __init__(self, cpu_id):
        self.cpu_id = cpu_id
        self.ready_processes = []  # Cola de procesos asignados
        self.completed_processes = []  # Procesos completados por este CPU
        self.running_process = []
        self.errored_processes = []
        self.algorithms = ['fcfs', 'sjf', 'priority', 'round_robin']

    def add_process(self, process):
        """Añade un proceso a la cola de esta CPU."""
        self.ready_processes.append(process)

    def delete_process(self, pid):
        """Elimina un proceso de la cola de esta CPU."""
        for process in self.ready_processes:
            if process.pid == pid:
                self.ready_processes.remove(process)
                break

    def sort_processes(self):
        """Ordena los procesos en la cola de acuerdo con el tiempo de llegada y la prioridad."""
        self.ready_processes.sort(key=lambda x:(x.arrival_time, -x.priority))

    def execute_processes(self, current_time):
        """Ejecuta los procesos asignados en función del tiempo actual."""
        self.sort_processes()
        if self.ready_processes:
            process = self.ready_processes[0]
            if process.remaining_time > 0 and process.arrival_time <= current_time:
                process.remaining_time -= 1
                if process.remaining_time == 0:
                    process.status = 'completed'
                    process.end_time = current_time
                    process.turnaround_time = current_time - process.arrival_time
                    process.waiting_time = process.turnaround_time - process.service_time
                    self.completed_processes.append(self.ready_processes.pop(0))
