import psutil

from app.core.CPU import CPU
from app.core.Dispatcher import Dispatcher
from app.core.Scheduler import Scheduler

class Simulation:
    def __init__(self, num_cpus):
        self.cpus = [CPU() for _ in range(num_cpus)]
        self.scheduler = Scheduler()
        self.dispatcher = Dispatcher()
    
    def run(self):
        while True:
            for cpu in self.cpus:
                process = self.scheduler.get_next_process()
                if process:
                    self.dispatcher.dispatch(cpu, process)
                    cpu.execute()