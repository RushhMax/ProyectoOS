
class CPU:
    def __init__(self, cpu_id, scheduler):
        self.cpu_id = cpu_id
        self.scheduler = scheduler  # Algoritmo de planificación (FIFO, Round Robin, etc.)
        self.process_queue = []  # Cola de procesos

    def add_process(self, process):
        """Asigna un proceso a la CPU."""
        self.process_queue.append(process)

    def execute(self):
        print(f"---- CPU {self.cpu_id}: {self.scheduler.__name__.replace('_', ' ')} ----")
        self.scheduler.execute(self.process_queue)
        # scheduled_processes = self.scheduler(self.process_queue) #Orden de procesos a ser ejecutados
        # for proc in scheduled_processes:
        #     print(proc)

    """
    def delete_process(self, pid):
        #Elimina un proceso de la cola de esta CPU.
        for process in self.processes:
            if process.pid == pid:
                self.processes.remove(process)
                break
    """
    def delete_process(self, pid):
        #Eliminar un proceso de la cola de esta CPU.
        for process in self.process_queue:
            if process.pid == pid:
                self.process_queue.remove(process)
                print(f"Proceso con PID {pid} eliminado de la CPU {self.cpu_id}.")
                return
        #print(f"Proceso con PID {pid} no encontrado en la CPU {self.cpu_id}.")
    
