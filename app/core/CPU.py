from datetime import datetime

from app.core.Process import Process

class CPU:
    def __init__(self, cpu_id, algorithm, processes):
        self.cpu_id = cpu_id
        self.processes = processes
        self.algorithm = algorithm

    def add_process(self, Process):
        """Asigna un proceso a la CPU."""
        self.process.append(Process)

    def delete_process(self, pid):
        """Elimina un proceso de la cola de esta CPU."""
        for process in self.processes:
            if process.pid == pid:
                self.processes.remove(process)
                break

    def execute_processes(self):
        """Ejecuta los procesos asignados en función del tiempo actual."""
        self.algorithm.execute(self.processes)
