from app.process import Process

def sort_by_arrival_time(processes):
    """Ordena los procesos por tiempo de llegada."""
    return sorted(processes, key=lambda x: x.arrival_time)

def simulate_fcfs_logic(processes):
    processes.sort(key=lambda x: x['pid'])
    current_time = 0
    for process in processes:
        process['start_time'] = current_time
        process['completion_time'] = current_time + process['burst_time']
        current_time += process['burst_time']
    return processes

def fcfs(processes):
    """First Come First Serve: Simula FCFS."""
    processes = sort_by_arrival_time(processes)  
    print("Simulando FCFS")
    print("Procesos: ", len(processes))
    current_time = 0
    for process in processes:
        process.display_important_info()
        current_time += process.service_time
        print(f"Tiempo actual: {current_time}")

def round_robin(processes, quantum):
    """Round Robin: Simula Round Robin con un quantum."""
