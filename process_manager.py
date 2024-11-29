import psutil
from datetime import datetime
from process import Process  # Asegúrate de que la ruta de importación sea correcta

class ProcessManager:
    def __init__(self):
        self.processes = []

    def get_processes(self):
        """Obtiene una lista de procesos activos en el sistema con información extendida."""
        self.processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent', 'username', 'status', 'create_time']):
            try:
                process_info = {
                    'pid': proc.info['pid'],                     # ID del proceso
                    'name': proc.info['name'],                   # Nombre del proceso
                    'cpu': proc.info['cpu_percent'],             # Uso de CPU (%)
                    'memory': proc.info['memory_percent'],       # Uso de memoria (%)
                    'user': proc.info['username'],               # Usuario que ejecuta el proceso
                    'status': proc.info['status'],               # Estado del proceso
                    'start_time': proc.info['create_time']       # Hora de creación del proceso
                }
                process = Process.from_proc_info(process_info)
                self.processes.append(process)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass  # Ignoramos los procesos que no se pueden acceder
        return self.processes

    def display_processes(self):
        """Muestra información extendida de los procesos activos."""
        for proc in self.processes:
            print(f"PID: {proc.pid} | Name: {proc.name} | CPU: {proc.cpu}% | "
                  f"Memory: {proc.memory}% | User: {proc.user} | Status: {proc.status} | "
                  f"Start Time: {datetime.fromtimestamp(proc.start_time).strftime('%Y-%m-%d %H:%M:%S')}")
