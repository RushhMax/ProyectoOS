class GlobalScheduler:
    def __init__(self, cpus):
        self.cpus = cpus  # Lista de CPUs

    def assign_processes(self, processes):
        # Distribuye procesos a CPUs (round-robin por ejemplo)
        for i, process in enumerate(processes):
            cpu_index = i % len(self.cpus)
            self.cpus[cpu_index].add_process(process)
