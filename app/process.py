import random

class Process:
    def __init__(self, pid, name, cpu, memory, user, status, start_time):
        self.pid = pid
        self.name = name
        self.cpu = cpu
        self.memory = memory
        self.user = user
        self.status = status
        self.start_time = start_time
        self.arrival_time = 0
        self.service_time = 0
        self.priority = 0

    def display_info(self):
        print(f'PID: {self.pid}, Name: {self.name}, CPU: {self.cpu}, Memory: {self.memory}, User: {self.user}, Status: {self.status}, Start Time: {self.start_time}, Arrival Time: {self.arrival_time}, Service Time: {self.service_time}, Priority: {self.priority}')

    def randomize(self):
        self.status = 'stopped'
        self.arrival_time = random.randint(0, 100)
        self.priority = random.randint(0, 100)

    @classmethod
    def from_proc_info(cls, proc_info):
        return cls(
            pid=proc_info['pid'],
            name=proc_info['name'],
            cpu=proc_info['cpu'],
            memory=proc_info['memory'],
            user=proc_info['user'],
            status=proc_info['status'],
            start_time=proc_info['start_time']
        )
