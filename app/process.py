import random

class Process:
    def __init__(self, pid, name, arrival_time, service_time, priority, cpu=0, memory=0, user='root', status='stopped', start_time=0, wait_time=0, turnaround_time=0, response_time=0):
        self.pid = pid
        self.name = name
        self.cpu = cpu
        self.memory = memory
        self.user = user
        self.status = status
        self.start_time = start_time
        self.arrival_time = arrival_time
        self.service_time = service_time
        self.priority = priority
        self.wait_time = wait_time
        self.turnaround_time = turnaround_time
        self.response_time = response_time

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
            start_time=proc_info['start_time']
        )

    def randomize(self, pid):
        self.pid = pid
        self.status = 'stopped'
        self.arrival_time = random.randint(0, 15)
        self.priority = random.randint(0, 10)
        self.service_time = random.randint(1, 20)

    def display_info(self):
        print(f'PID: {self.pid}, Name: {self.name}, CPU: {self.cpu}, Memory: {self.memory}, User: {self.user}, Status: {self.status}, Start Time: {self.start_time}, Arrival Time: {self.arrival_time}, Service Time: {self.service_time}, Priority: {self.priority}')
    
    def display_important_info(self):
        print(f'PID: {self.pid}, Name: {self.name}, Status: {self.status}, Arrival Time: {self.arrival_time}, Service Time: {self.service_time}, Priority: {self.priority}')

    def display_times(self):
        print(f'PID: {self.pid}, Wait Time: {self.wait_time}, Turnaround Time: {self.turnaround_time}, Response Time: {self.response_time}')


