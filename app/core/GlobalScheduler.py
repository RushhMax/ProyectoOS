class GlobalScheduler:
    def __init__(self, cpus):
        self.cpus = cpus  # Lista de CPUs

    def assign_processes(self, processes):
        # Distribuye procesos a CPUs (round-robin por ejemplo)
        print("\nAsignando procesos a CPUs\n")
        print(len(self.cpus))

        for i, process in enumerate(processes):
            process.status = "READY"
            cpu_index = i % len(self.cpus)
            self.cpus[cpu_index].add_process(process)
