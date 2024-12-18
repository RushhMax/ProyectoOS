from queue import Queue
from .algorithms.FCFS import FCFS
from .algorithms.RoundRobin import RoundRobin
from .algorithms.SJF import SJF

class Scheduler:
    def __init__(self, algorithm_type, quantum=None):
        """
        Initializes the scheduler with the selected algorithm type.
        :param algorithm_type: The scheduling algorithm to use (e.g., "FCFS", "RoundRobin", "SJF").
        :param quantum: The time quantum for Round Robin (optional).
        """
        self.algorithm_type = algorithm_type
        self.ready_queue = Queue()  # Queue of processes that are ready to run
        self.algorithm = self._choose_algorithm(algorithm_type, quantum)

    def _choose_algorithm(self, algorithm_type, quantum):
        """
        Selects the scheduling algorithm based on the given type.
        :param algorithm_type: Type of scheduling algorithm.
        :param quantum: Time quantum for Round Robin.
        :return: An instance of the corresponding scheduling algorithm.
        """
        if algorithm_type == "FCFS":
            return FCFS(self.ready_queue)
        elif algorithm_type == "RoundRobin":
            return RoundRobin(self.ready_queue, quantum)
        elif algorithm_type == "SJF":
            return SJF(self.ready_queue)
        else:
            raise ValueError(f"Unsupported algorithm type: {algorithm_type}")

    def add_process(self, process):
        """
        Adds a process to the ready queue.
        :param process: A process object to be added.
        """
        self.ready_queue.put(process)

    def get_next_process(self):
        """
        Gets the next process based on the selected scheduling algorithm.
        :return: The next process to execute.
        """
        return self.algorithm.schedule()

    def is_empty(self):
        """
        Checks if there are processes in the ready queue.
        :return: True if the ready queue is empty, False otherwise.
        """
        return self.ready_queue.empty()

    def execute(self):
        """
        Executes the processes based on the selected scheduling algorithm.
        """
        print(f"Starting execution with {self.algorithm_type} algorithm.")
        while not self.is_empty():
            process = self.get_next_process()
            print(f"Executing {process}")
            # Simulate execution of the process
            process.execute()
