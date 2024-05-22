import time


class Logger():
    """
    This is a class that defines Logger object.
    Attributes
    logfile_name: str
        name of log file
    """
    count_alerts = 0
    count_warnings = 0

    def __init__(self, logfile_name=None):
        """Constructs all necessary attributes for the Logger object."""
        self.time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        self.time_str_file = time.strftime("%Y-%m-%d-%H-%M-%S", time.gmtime())
        self.start_time = time.time()
        if logfile_name is None:
            logfile_name = (f"{self.time_str_file}.log")
        self.logfile_name = logfile_name

        with open(self.logfile_name, 'w') as freading:
            print('\n')

    def show_log_banner(self, message) -> str:
        """
        This method shows banner-message into terminal and logs it into a file.
        """
        with open(self.logfile_name, 'a') as freading:
            freading.write('='*80)
            freading.write("\n")
            freading.write(f'{self.time_str}:{message}')
            freading.write("\n")
            freading.write('='*80)
            freading.write("\n")
        print('='*80)
        print(f'{self.time_str}:{message}')
        print('='*80)

    def show_log_header(self, message) -> str:
        """
        This method shows header-message into terminal and logs it into a file.
        """
        with open(self.logfile_name, 'a') as freading:
            freading.write(f'{self.time_str}:{message}')
            freading.write("\n")
            freading.write('-'*80)
            freading.write("\n")

        print(f'{self.time_str}:{message}')
        print('-'*80)

    def log_banner(self, message) -> str:
        """This method logs banner-messages into a file."""
        with open(self.logfile_name, 'a') as freading:
            freading.write('='*80)
            freading.write("\n")
            freading.write(f'{self.time_str}:{message}')
            freading.write("\n")
            freading.write('='*80)
            freading.write("\n")

    def log_header(self, message) -> str:
        """This method logs header-messages into a file."""
        with open(self.logfile_name, 'a') as freading:
            freading.write(f'{self.time_str}:{message}')
            freading.write("\n")
            freading.write('-'*80)
            freading.write("\n")

    def show_log_init(self, message) -> str:
        """
        This method shows initialization messages into terminal and logs it
        into a file.
        """
        with open(self.logfile_name, 'a') as freading:
            freading.write(f"{self.time_str}:{'[INIT]'}{message}")
            freading.write("\n")
        print(f"{self.time_str}:{'[INIT]'}{message}")

    def show_log_action(self, message) -> str:
        """
        This method shows action messages into terminal and logs it into a
        file.
        """
        with open(self.logfile_name, 'a') as freading:
            freading.write(f"{self.time_str}:{'[ACTION]'}{message}")
            freading.write("\n")
        print(f"{self.time_str}:{'[ACTION]'}{message}")

    def show_log_warning(self, message) -> str:
        """
        This method shows warning messages into terminal and logs it into a
        file.
        """
        with open(self.logfile_name, 'a') as freading:
            freading.write(f"{self.time_str}:{'[WARNING]'}{message}")
            freading.write("\n")
        print(f"{self.time_str}:{'[WARNING]'}{message}")
        self.count_warnings += 1

    def show_log_alert(self, message) -> str:
        """
        This method shows alert messages into terminal and logs it into a
        file.
        """
        with open(self.logfile_name, 'a') as freading:
            freading.write(f"{self.time_str}:{'[ALERT]'}{message}")
            freading.write("\n")
        print(f"{self.time_str}:{'[ALERT]'}{message}")
        self.count_alerts += 1

    def show_log_info(self, message) -> str:
        """
        This method shows info messages into terminal and logs it into a
        file.
        """
        with open(self.logfile_name, 'a') as freading:
            freading.write(f"{self.time_str}:{'[INFO]'}{message}")
            freading.write("\n")
        print(f"{self.time_str}:{'[INFO]'}{message}")

    def log_init(self, message) -> str:
        """This method logs initialization messages into a file."""
        with open(self.logfile_name, 'a') as freading:
            freading.write(f"{self.time_str}:{'[INIT]'}{message}")
            freading.write("\n")

    def log_action(self, message) -> str:
        """This method logs action messages into a file."""
        with open(self.logfile_name, 'a') as freading:
            freading.write(f"{self.time_str}:{'[ACTION]'}{message}")
            freading.write("\n")

    def log_warning(self, message) -> str:
        """This method logs warning messages into a file."""
        with open(self.logfile_name, 'a') as freading:
            freading.write(f"{self.time_str}:'[WARNING]'{message}")
            freading.write("\n")
        self.count_warnings += 1

    def log_alert(self, message) -> str:
        """This method logs alert messages into a file."""
        with open(self.logfile_name, 'a') as freading:
            freading.write(f"{self.time_str}:{'[ALERT]'}{message}")
            freading.write("\n")
        self.count_alerts += 1

    def log_info(self, message) -> str:
        """This method logs info messages into a file."""
        with open(self.logfile_name, 'a') as freading:
            freading.write(f"{self.time_str}:{'[INFO]'}{message}")
            freading.write("\n")

    def report(self) -> None:
        """This method summarizes and reports all the activities."""
        finish_time = time.time()

        with open(self.logfile_name, 'a') as freading:
            freading.write(f"{self.time_str}:")
            freading.write("\n")
            freading.write(f"{self.time_str}:{'='*60}")
            freading.write("\n")
            freading.write(f"{self.time_str}:{'Total alerts:'} {self.count_alerts}")
            freading.write("\n")
            freading.write(f"{self.time_str}:{'Total warning:'} {self.count_warnings}")
            freading.write("\n")
            elapsed_time_sec = finish_time - self.start_time
            freading.write(f"{self.time_str}:Time spent: {elapsed_time_sec:.4f}")

        print(f"{self.time_str}:")
        print(f"{self.time_str}:{'='*60}")
        print(f"{self.time_str}:{'Total alerts:'} {self.count_alerts}")
        print(f"{self.time_str}:{'Total warning:'} {self.count_warnings}")
        print(f"{self.time_str}:Time spent:{elapsed_time_sec:.4f}")
