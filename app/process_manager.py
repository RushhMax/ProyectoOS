import psutil
from datetime import datetime
from app.process import Process

class ProcessManager:
    def __init__(self):
        self.processes = []

    def start(self):
        """Inicializa el administrador de procesos."""
        self.get_real_processes()
        self.processes.sort(key=lambda x:(x.arrival_time, -x.priority))
    
    def get_processes(self):
        """Obtiene la lista de procesos."""
        return self.processes

    def get_real_processes(self):
        """Obtains a list of active system processes with extended information."""
        self.processes = []
        cont = 1
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent', 'username', 'status', 'create_time']):
            try:
                # Process information
                process_info = {
                    'pid': cont,                 # Process ID
                    'name': proc.info['name'],               # Process Name
                    'cpu': proc.cpu_percent(interval=0.1),   # CPU usage percentage (needs an interval)
                    'memory': proc.info['memory_percent'],   # Memory usage percentage
                    'user': proc.info['username'],           # Username running the process
                    'status': 'stopped',           # Process status (running, sleeping, etc.)
                    'start_time': datetime.fromtimestamp(proc.info['create_time']).strftime('%Y-%m-%d %H:%M:%S')  # Start time
                }
                # Create a Process object
                process = Process.from_proc_info(process_info)
                self.processes.append(process)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass  # Ignore processes that are inaccessible or no longer exist
            cont += 1

    def add_process(self, process):
        """Agrega un proceso a la lista de procesos activos."""
        self.processes.append(process)
        self.processes.sort(key=lambda x:(x.arrival_time, -x.priority))

    def delete_process(self, pid):
        """Elimina un proceso de la lista de procesos activos."""
        for proc in self.processes:
            if proc.pid == pid:
                self.processes.remove(proc)
                return True
        return False

    def display_processes(self):
        """Muestra información extendida de los procesos."""
        for proc in self.processes:
             proc.display_info()
