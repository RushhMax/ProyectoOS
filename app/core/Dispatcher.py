class Dispatcher:
    def __init__(self, scheduler):
        """
        Initializes the dispatcher with a scheduler.
        :param scheduler: An instance of the Scheduler class.
        """
        self.scheduler = scheduler

    def dispatch(self):
        """
        Dispatches the next process to the CPU for execution.
        """
        while not self.scheduler.is_empty():
            process = self.scheduler.get_next_process()
            print(f"Dispatching process {process}")
            process.execute()
