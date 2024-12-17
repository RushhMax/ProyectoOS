from datetime import datetime

class CPU:
    def __init__(self, cpu_id, algorithm):
        self.cpu_id = cpu_id
        self.process = None
        self.algorithm = algorithm

    def assign_process(self, process):
        """Asigna un proceso a la CPU."""
        self.process = process

    def delete_process(self, pid):
        """Elimina un proceso de la cola de esta CPU."""
        for process in self.ready_processes:
            if process.pid == pid:
                self.ready_processes.remove(process)
                break

    def execute_processes(self):
        """Ejecuta los procesos asignados en función del tiempo actual."""
        self.algorithm.execute(self)
