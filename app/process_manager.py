import psutil
from datetime import datetime
from app.process import Process

class ProcessManager:
    def __init__(self):
        self.processes = []

    def start(self):
        """Inicializa el administrador de procesos."""
        self.get_real_processes()
        self.randomize_processes()
        self.processes.sort(key=lambda x:(x.arrival_time, -x.priority))
    
    def get_processes(self):
        """Obtiene la lista de procesos."""
        return self.processes

    def get_real_processes(self):
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


    def add_process(self, process):
        """Agrega un proceso a la lista de procesos activos."""
        self.processes.append(process)

    def add_process_random(self):
        """Agrega un proceso con información aleatoria a la lista de procesos activos."""
        pid = len(self.processes) + 1 
        name = f'Random Process {pid}'
        cpu = round(100 * (pid % 10) / 10, 2)
        memory = round(100 * (pid % 5) / 5, 2)
        user = 'random'
        status = 'running'
        start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        process = Process(pid=pid, name=name, cpu=cpu, memory=memory, user=user, status=status, start_time=start_time)
        process.randomize()
        self.processes.append(process)

    def delete_process(self, pid):
        """Elimina un proceso de la lista de procesos activos."""
        for proc in self.processes:
            if proc.pid == pid:
                self.processes.remove(proc)
                return True
        return False

    def randomize_processes(self):
        """Simula la creación de procesos con información aleatoria."""
        for proc in self.processes:
            proc.randomize()

    def display_processes(self):
        """Muestra información extendida de los procesos."""
        for proc in self.processes:
             proc.display_info()
