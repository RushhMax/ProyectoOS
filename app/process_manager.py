import psutil
from datetime import datetime
from app.process import Process

class ProcessManager:
    def __init__(self):
        self.processes = []

    def get_processes(self):
        """Obtains a list of active system processes with extended information."""
        self.processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent', 'username', 'status', 'create_time']):
            try:
                # Process information
                process_info = {
                    'pid': proc.info['pid'],                 # Process ID
                    'name': proc.info['name'],               # Process Name
                    'cpu': proc.cpu_percent(interval=0.1),   # CPU usage percentage (needs an interval)
                    'memory': proc.info['memory_percent'],   # Memory usage percentage
                    'user': proc.info['username'],           # Username running the process
                    'status': proc.info['status'],           # Process status (running, sleeping, etc.)
                    'start_time': datetime.fromtimestamp(proc.info['create_time']).strftime('%Y-%m-%d %H:%M:%S')  # Start time
                }
                # Create a Process object
                process = Process.from_proc_info(process_info)
                self.processes.append(process)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass  # Ignore processes that are inaccessible or no longer exist
        return self.processes

    def add_process(self, process):
        """Agrega un proceso a la lista de procesos activos."""
        self.processes.append(process)

    def randomize_processes(self):
        """Simula la creación de procesos con información aleatoria."""
        for proc in self.processes:
            proc.randomize()

    def display_processes(self):
        """Muestra información extendida de los procesos."""
        for proc in self.processes:
             proc.display_info()
