class Process:
    def __init__(self, pid, name, cpu, memory, user, status):
        self.pid = pid
        self.name = name
        self.cpu = cpu
        self.memory = memory
        self.user = user
        self.status = status
        self.arrival_time = 0
        self.service_time = 0
        self.priority = 0

    def display_info(self):
        print(f'PID: {self.pid}')
        print(f'Name: {self.name}')
        print(f'CPU: {self.cpu}%')
        print(f'Memory: {self.memory}%')
        print(f'User: {self.user}')
        print(f'Status: {self.status}')
        print(f'Arrival Time: {self.arrival_time}')
        print(f'Service Time: {self.service_time}')

    def randomize(self):
        self.status = 'stopped'
        self.arrival_time = random.randint(0, 100)
        self.priority = random.randint(0, 100)

    @classmethod
    def from_proc_info(cls, proc_info):
        return cls(
            pid=proc_info['pid'],
            name=proc_info['name'],
            cpu=proc_info['cpu_percent'],
            memory=proc_info['memory_percent'],
            user=proc_info['username'],
            status=proc_info['status']
        )