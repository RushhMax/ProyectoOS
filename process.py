class Process:
    def __init__(self, pid, name, cpu, memory, user, status, start_time):
        self.pid = pid
        self.name = name
        self.cpu = cpu
        self.memory = memory
        self.user = user
        self.status = status
        self.start_time = start_time

    @classmethod
    def from_proc_info(cls, proc_info):
        return cls(
            pid=proc_info['pid'],
            name=proc_info['name'],
            cpu=proc_info['cpu_percent'],
            memory=proc_info['memory_percent'],
            user=proc_info['username'],
            status=proc_info['status'],
            start_time=proc_info['create_time']
        )