import random

class Process:
    def __init__(self, pid, name, cpu, memory, user, status, start_time):
        self.pid = pid # process id
        self.name = name # process name
        self.cpu = cpu # cpu usage 
        self.memory = memory # memory usage
        self.user = user # user name
        self.status = status # process status
        self.start_time = start_time # process start time
        self.arrival_time = 0 # process arrival time
        self.service_time = 0 # process service time (burst time)
        self.priority = 0 # process priority
        self.wait_time = 0 # process wait time (response time)
        self.turnaround_time = 0 # process turnaround time (completion time)
        self.response_time = 0 # process response time (wait time + service time)


    def display_info(self):
        print(f'PID: {self.pid}, Name: {self.name}, CPU: {self.cpu}, Memory: {self.memory}, User: {self.user}, Status: {self.status}, Start Time: {self.start_time}, Arrival Time: {self.arrival_time}, Service Time: {self.service_time}, Priority: {self.priority}')
    
    def display_important_info(self):
        print(f'PID: {self.pid}, Name: {self.name}, Status: {self.status}, Arrival Time: {self.arrival_time}, Service Time: {self.service_time}, Priority: {self.priority}')

    def display_times(self):
        print(f'PID: {self.pid}, Wait Time: {self.wait_time}, Turnaround Time: {self.turnaround_time}, Response Time: {self.response_time}')

    def randomize(self):
        self.status = 'stopped'
        self.arrival_time = random.randint(0, 15)
        self.priority = random.randint(0, 10)
        self.service_time = random.randint(1, 20)

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
