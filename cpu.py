class CPU:
    def __init__(self, cpu_id):
        self.cpu_id = cpu_id
        self.queue = []

    def add_process(self, process):
        """Añade un proceso a la cola de esta CPU."""
        self.queue.append(process)

    def execute_processes(self):
        """Simula la ejecución de procesos."""
        for process in self.queue:
            print(f"CPU {self.cpu_id} ejecutando proceso {process['name']} (PID: {process['pid']})")
