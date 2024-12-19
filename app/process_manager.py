import random
import psutil

from app.core.Process import Process
from app.core.CPU import CPU
from app.core.GlobalScheduler import GlobalScheduler
from app.algorithms.FCFS import FCFS
from app.algorithms.Priority import Priority
from app.algorithms.RoundRobin import RoundRobin
from app.algorithms.SJF import SJF

class ProcessManager:
    def __init__(self, num_processes=12):
        self.num_processes = num_processes
        self.processes = []
        self.cpus = []
        self.global_scheduler = None

    def generate_processes(self, num_processes=12):
        """Generar procesos aleatorios."""
        self.num_processes = num_processes
        for i in range(self.num_processes):
            _pid = self.get_next_pid()
            process = Process(
                pid=_pid,
                name=f"Process_{_pid}",
                arrival_time=random.randint(0, 15),
                service_time=random.randint(1, 20),
                priority=random.randint(1, 10),
                cpu=0,
                memory=random.randint(512, 4096),
                user="user",
                status="INDEFINIDO"
            )
            self.processes.append(process)
    
    def get_processes(self):
        """Obtener la lista de procesos."""
        return self.processes
    
    def get_next_pid(self):
        return self.processes[-1].pid + 1 if self.processes else 0

    def get_real_processes(self):
        #Obtains a list of active system processes with extended information.
        self.processes = []
        cont = 1
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent', 'username', 'status', 'create_time']):
            try:
                # Process information
                process_info = {
                    'pid': cont,                 # Process ID
                    'name': proc.info['name'],               # Process Name
                    'cpu': proc.cpu_percent(interval=None),   # CPU usage percentage (needs an interval)
                    'memory': proc.info['memory_percent'],   # Memory usage percentage
                    'user': proc.info['username'],           # Username running the process
                    'status': 'INDEFINIDO'          # Process status (running, sleeping, etc.)
                }
                # Create a Process object
                process = Process.from_proc_info(process_info)
                self.processes.append(process)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass  # Ignore processes that are inaccessible or no longer exist
            cont += 1
        self.num_processes = len(self.processes)


    def setup_cpus(self, cpu_algorithms):
        """Configurar CPUs con diferentes algoritmos de planificación personalizados"""
        
        self.cpus = []
        for cpu_id, algorithm in enumerate(cpu_algorithms):
            if algorithm == "fcfs":
                scheduler = FCFS()
            elif algorithm == "round_robin":
                scheduler = RoundRobin(quantum=4)
            elif algorithm == "sjf":
                scheduler = SJF()
            elif algorithm == "priority":
                scheduler = Priority()
            else:
                raise ValueError(f"Algoritmo {algorithm} no reconocido para la CPU {cpu_id}")

            print(f"CPU {cpu_id}: {algorithm}")
            self.cpus.append(CPU(cpu_id=cpu_id, scheduler=scheduler))
        
        """self.cpus = [
            CPU(cpu_id=0, scheduler=FCFS()),
            CPU(cpu_id=1, scheduler=RoundRobin(quantum=4)),
            CPU(cpu_id=2, scheduler=SJF()),
            CPU(cpu_id=3, scheduler=Priority())
        ]"""

    def assign_processes(self):
        """Asignar procesos a CPUs usando el planificador global."""
        self.global_scheduler = GlobalScheduler(self.cpus)
        self.global_scheduler.assign_processes(self.processes)

    def run_simulation(self):
        """Ejecutar la simulación en cada CPU."""
        print("---- Simulación de Procesos ----")
        for cpu in self.cpus:
            cpu.execute()

    def display_processes(self):
        """Mostrar los procesos generados."""
        print("---- Procesos Generados ----")
        for process in self.processes:
            process.display_info()

    def simulate(self):
        """Método principal para ejecutar todo."""
        self.generate_processes()
        #self.get_real_processes()
        self.display_processes()
        self.setup_cpus()
        self.assign_processes()
        self.run_simulation()
    
    def add_process(self, process):
        """Agregar un nuevo proceso al sistema."""
        process.display_info()
        self.processes.append(process)
        print(f"Proceso {process.name} agregado correctamente.")

    def delete_process(self, pid):
        """Eliminar un proceso del sistema por su PID."""
        process_to_remove = next((proc for proc in self.processes if proc.pid == pid), None)
        if process_to_remove:
            self.processes.remove(process_to_remove)
            print(f"Proceso con PID {pid} eliminado correctamente.")

            # También eliminar de las colas de los CPUs
            for cpu in self.cpus:
                cpu.delete_process(pid)
        else:
            print(f"Proceso con PID {pid} no encontrado.")


"""
from app.process import Process
from app.cpu import CPU
from app.algorithms import fcfs, round_robin, sjf

class ProcessManager:
    def __init__(self):
        self.processes = []
        self.cpus = [CPU(i) for i in range(4)]
        self.completed_processes = []

    def start(self):
        #Inicializa el administrador de procesos.
        self.get_real_processes()
        self.processes.sort(key=lambda x:(x.arrival_time, -x.priority))
        self.distribute_processes()

    def distribute_processes(self):
        #istribuye los procesos iniciales para equilibrar la carga entre los CPUs.
        for process in self.processes:
            # Encuentra el CPU con la menor carga (suma de tiempos de servicio de los procesos en la cola)
            least_loaded_cpu = min(self.cpus, key=lambda cpu: sum(p.service_time for p in cpu.ready_processes))
            least_loaded_cpu.add_process(process)

    
    def get_processes(self):
        #Obtiene la lista de procesos.
        return self.processes

    def get_real_processes(self):
        #Obtains a list of active system processes with extended information.
        self.processes = []
        cont = 1
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent', 'username', 'status', 'create_time']):
            try:
                # Process information
                process_info = {
                    'pid': cont,                 # Process ID
                    'name': proc.info['name'],               # Process Name
                    'cpu': proc.cpu_percent(interval=None),   # CPU usage percentage (needs an interval)
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


    def assign_processes(self, algorithm):
        #Asigna procesos a las CPUs usando un algoritmo específico.
        if algorithm == "fcfs":
            fcfs(self.processes, self.cpus)
        elif algorithm == "round_robin":
            round_robin(self.processes, self.cpus)
        elif algorithm == "sjf":
            sjf(self.processes, self.cpus)

    def track_completed_processes(self):
        #Rastrea los procesos completados en cada CPU.
        for cpu in self.cpus:
            self.completed_processes.extend(cpu.completed_processes)

    def display_processes(self):
        #Muestra información extendida de los procesos.
        for proc in self.processes:
             proc.display_info()
"""