class RoundRobin:
    def __init__(self, quantum):
        self.__name__ = "Round Robin"
        self.quantum = quantum

    def execute(self, process_queue):
        print("\nExecuting Round Robin Scheduling Algorithm\n")

        time = 0
        queue = []
        visited = [False] * len(process_queue)

        # Inicializar atributos de cada proceso
        for process in process_queue:
            process.start_time = None
            process.remaining_time = process.service_time
            process.wait_time = 0
            process.turnaround_time = 0
            process.response_time = 0

        while True:
            # Agregar procesos que llegan al tiempo actual a la cola
            for i, process in enumerate(process_queue):
                if process.arrival_time <= time and not visited[i]:
                    queue.append(process)
                    visited[i] = True
                    print(f"Process {process.name} entered the queue at time {time}.")

            if not queue:
                # Si no hay procesos listos pero queda alguno por completar, avanzamos el tiempo
                if all(proc.remaining_time == 0 for proc in process_queue):
                    break
                time += 1
                continue

            current = queue.pop(0)

            # Ejecutar el proceso con la lógica ajustada
            if current.remaining_time > self.quantum:
                # Proceso no finaliza, se ejecuta por un quantum
                time += self.quantum
                current.remaining_time -= self.quantum
                print(f"Executing {current.name} for {self.quantum} units. Remaining time: {current.remaining_time}")

                # Agregar nuevos procesos que hayan llegado durante la ejecución
                for i, proc in enumerate(process_queue):
                    if proc.arrival_time <= time and not visited[i]:
                        queue.append(proc)
                        visited[i] = True
                        print(f"Process {proc.name} entered the queue at time {time}.")

                # Reinsertar el proceso actual al final de la cola
                queue.append(current)
            else:
                # Proceso finaliza
                time += current.remaining_time
                current.remaining_time = 0
                current.wait_time = time - current.service_time - current.arrival_time
                current.turnaround_time = current.service_time + current.wait_time
                print(f"Process {current.name} completed at time {time}. Waiting time: {current.wait_time}, Turnaround time: {current.turnaround_time}")

        # Imprimir resumen final
        print("\nSummary of Process Execution:")
        print("Process\tArrival Time\tService Time\tWaiting Time\tTurnaround Time")
        for proc in process_queue:
            print(f"{proc.name}\t\t{proc.arrival_time}\t\t{proc.service_time}\t\t{proc.wait_time}\t\t{proc.turnaround_time}")
        print("\nAll processes have been executed.\n")
