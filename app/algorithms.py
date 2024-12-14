from app.process import Process

def sort_by_arrival_time(processes):
    """Ordena los procesos por tiempo de llegada."""
    return sorted(processes, key=lambda x: x.arrival_time)

def fcfs(processes, cpus):
    """First Come First Serve: Simula FCFS en múltiples CPUs."""
    processes = sort_by_arrival_time(processes)
    current_cpu = 0
    print("Simulando FCFS")

    for process in processes:
        cpus[current_cpu].add_process(process)
        current_cpu = (current_cpu + 1) % len(cpus)

def round_robin(processes, cpus, quantum=4):
    """Round Robin con soporte para tiempos de llegada y ejecución en múltiples CPUs."""
    # Inicializar colas de los CPUs
    for process in processes:
        least_loaded_cpu = min(cpus, key=lambda cpu: len(cpu.queue))
        least_loaded_cpu.add_process(process)

    # Simulación del tiempo
    time = 0
    while any(cpu.queue for cpu in cpus):  # Mientras haya procesos en las colas de los CPUs
        for cpu in cpus:
            if not cpu.queue:
                continue
            process = cpu.queue.pop(0)
            if process.remaining_time > quantum:
                process.remaining_time -= quantum
                time += quantum
                cpu.queue.append(process)  # Regresar a la cola del CPU
            else:
                time += process.remaining_time
                process.remaining_time = 0
                process.status = 'completed'
                process.end_time = time
                process.turnaround_time = time - process.arrival_time
                process.waiting_time = process.turnaround_time - process.service_time
                cpu.completed_processes.append(process)


def sjf(processes, cpus):
    """Shortest Job First (No Preventivo) con soporte para tiempos de llegada en múltiples CPUs."""
    # Inicializar colas de los CPUs
    for process in processes:
        least_loaded_cpu = min(cpus, key=lambda cpu: len(cpu.queue))
        least_loaded_cpu.add_process(process)

    # Simulación del tiempo
    time = 0
    while any(cpu.queue for cpu in cpus):  # Mientras haya procesos en las colas de los CPUs
        for cpu in cpus:
            available_processes = [p for p in cpu.queue if p.arrival_time <= time and p.status != 'completed']
            if not available_processes:
                continue
            current_process = min(available_processes, key=lambda p: p.service_time)
            cpu.queue.remove(current_process)  # Remover de la cola
            time += current_process.service_time
            current_process.status = 'completed'
            current_process.end_time = time
            current_process.turnaround_time = time - current_process.arrival_time
            current_process.waiting_time = current_process.turnaround_time - current_process.service_time
            cpu.completed_processes.append(current_process)

