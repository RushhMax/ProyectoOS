from app.process import Process

def fcfs(processes, cpus):
    """First Come First Serve: Asigna procesos a CPUs por orden."""
    cpu_count = len(cpus)
    for i, process in enumerate(processes):
        cpus[i % cpu_count].add_process(process)

def round_robin(processes, cpus, quantum):
    """Round Robin: Simula Round Robin con un quantum."""
    cpu_count = len(cpus)
    for i, process in enumerate(processes):
        process['quantum'] = quantum  # Asigna quantum a cada proceso
        cpus[i % cpu_count].add_process(process)
