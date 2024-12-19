import random

class Process:
    def __init__(self, pid, name, arrival_time, service_time, priority, cpu=0, memory=0, user='root', status='INDEFINIDO'):
        self.pid = pid
        self.name = name
        self.cpu = cpu
        self.memory = memory
        self.user = user
        self.status = status
        self.arrival_time = arrival_time
        self.service_time = service_time
        self.priority = priority
        self.start_time = None
        self.waiting_time = None 
        self.turnaround_time = None
        self.response_time = None
        self.remaining_time = service_time  # Nuevo atributo para tiempo restante

    @classmethod
    def from_proc_info(cls, proc_info):
        return cls(
            pid=proc_info['pid'],
            name=proc_info['name'],
            arrival_time=random.randint(0, 15),
            service_time=random.randint(1, 20),
            priority=random.randint(0, 10),
            cpu=proc_info['cpu'],
            memory=proc_info['memory'],
            user=proc_info['user'],
            status=proc_info['status'],
        )

    def randomize(self, pid):
        self.pid = pid
        self.status = "INDEFINIDO"
        self.arrival_time = random.randint(0, 15)
        self.priority = random.randint(0, 10)
        self.service_time = random.randint(1, 20)
        self.remaining_time = self.service_time  # Reiniciar el tiempo restante al azar
        self.start_time = 0

    def display_info(self):
        print(f'PID: {self.pid}, Name: {self.name}, CPU: {self.cpu}, Memory: {self.memory}, User: {self.user}, Status: {self.status}, Start Time: {self.start_time}, Arrival Time: {self.arrival_time}, Service Time: {self.service_time}, Priority: {self.priority}, Remaining Time: {self.remaining_time}')
    
    def display_important_info(self):
        print(f'PID: {self.pid}, Name: {self.name}, Status: {self.status}, Arrival Time: {self.arrival_time}, Service Time: {self.service_time}, Priority: {self.priority}, Remaining Time: {self.remaining_time}')

    def display_times(self):
        print(f'PID: {self.pid}, Wait Time: {self.waiting_time}, Turnaround Time: {self.turnaround_time}, Response Time: {self.response_time}')
