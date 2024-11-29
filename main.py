from process_manager import ProcessManager
from cpu import CPU
from algorithms import fcfs, round_robin

def main():
    # Inicializamos la gestión de procesos
    manager = ProcessManager()
    processes = manager.get_processes()

    # Mostramos los procesos activos
    print("Procesos activos:")
    manager.display_processes()

    # Simulamos 4 CPUs
    cpus = [CPU(i) for i in range(4)]

    # Seleccionamos algoritmo
    print("\nAsignando procesos con FCFS:")
    fcfs(processes, cpus)

    # Ejecutamos los procesos en cada CPU
    for cpu in cpus:
        cpu.execute_processes()

if __name__ == "__main__":
    main()
