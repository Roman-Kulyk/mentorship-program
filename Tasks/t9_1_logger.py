import time


time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
time_str_file = time.strftime("%Y-%m-%d-%H-%M-%S", time.gmtime())
start_time = time.time()


class Logger():
    """
    This is a class that defines Logger object.
    Attributes
    logfile_name: str
        name of log file
    """

    def __init__(self, logfile_name=(f"{time_str_file}.log")):
        """Constructs all necessary attributes for the Logger object."""
        self.logfile_name = logfile_name

    def show_log_banner(self, message) -> str:
        """
        This method shows banner-message into terminal and logs it into a file.
        """
        with open(self.logfile_name, 'a') as freading:
            freading.write('='*80)
            freading.write("\n")
            freading.write(f'{time_str}:{message}')
            freading.write("\n")
            freading.write('='*80)
            freading.write("\n")
        print('='*80)
        print(f'{time_str}:{message}')
        print('='*80)

    def show_log_header(self, message) -> str:
        """
        This method shows header-message into terminal and logs it into a file.
        """
        with open(self.logfile_name, 'a') as freading:
            freading.write(f'{time_str}:{message}')
            freading.write("\n")
            freading.write('-'*80)
            freading.write("\n")

        print(f'{time_str}:{message}')
        print('-'*80)

    def log_banner(self, message) -> str:
        """This method logs banner-messages into a file."""
        with open(self.logfile_name, 'a') as freading:
            freading.write('='*80)
            freading.write("\n")
            freading.write(f'{time_str}:{message}')
            freading.write("\n")
            freading.write('='*80)
            freading.write("\n")

    def log_header(self, message) -> str:
        """This method logs header-messages into a file."""
        with open(self.logfile_name, 'a') as freading:
            freading.write(f'{time_str}:{message}')
            freading.write("\n")
            freading.write('-'*80)
            freading.write("\n")

    def show_log_init(self, message) -> str:
        """
        This method shows initialization messages into terminal and logs it
        into a file.
        """
        with open(self.logfile_name, 'a') as freading:
            freading.write(f"{time_str}:{'[INIT]'}{message}")
            freading.write("\n")
        print(f"{time_str}:{'[INIT]'}{message}")

    def show_log_action(self, message) -> str:
        """
        This method shows action messages into terminal and logs it into a
        file.
        """
        with open(self.logfile_name, 'a') as freading:
            freading.write(f"{time_str}:{'[ACTION]'}{message}")
            freading.write("\n")
        print(f"{time_str}:{'[ACTION]'}{message}")

    def show_log_warning(self, message) -> str:
        """
        This method shows warning messages into terminal and logs it into a
        file.
        """
        with open(self.logfile_name, 'a') as freading:
            freading.write(f"{time_str}:{'[WARNING]'}{message}")
            freading.write("\n")
        print(f"{time_str}:{'[WARNING]'}{message}")

    def show_log_alert(self, message) -> str:
        """
        This method shows alert messages into terminal and logs it into a
        file.
        """
        with open(self.logfile_name, 'a') as freading:
            freading.write(f"{time_str}:{'[ALERT]'}{message}")
            freading.write("\n")
        print(f"{time_str}:{'[ALERT]'}{message}")

    def show_log_info(self, message) -> str:
        """
        This method shows info messages into terminal and logs it into a
        file.
        """
        with open(self.logfile_name, 'a') as freading:
            freading.write(f"{time_str}:{'[INFO]'}{message}")
            freading.write("\n")
        print(f"{time_str}:{'[INFO]'}{message}")

    def log_init(self, message) -> str:
        """This method logs initialization messages into a file."""
        with open(self.logfile_name, 'a') as freading:
            freading.write(f"{time_str}:{'[INIT]'}{message}")
            freading.write("\n")

    def log_action(self, message) -> str:
        """This method logs action messages into a file."""
        with open(self.logfile_name, 'a') as freading:
            freading.write(f"{time_str}:{'[ACTION]'}{message}")
            freading.write("\n")

    def log_warning(self, message) -> str:
        """This method logs warning messages into a file."""
        with open(self.logfile_name, 'a') as freading:
            freading.write(f"{time_str}:'[WARNING]'{message}")
            freading.write("\n")

    def log_alert(self, message) -> str:
        """This method logs alert messages into a file."""
        with open(self.logfile_name, 'a') as freading:
            freading.write(f"{time_str}:{'[ALERT]'}{message}")
            freading.write("\n")

    def log_info(self, message) -> str:
        """This method logs info messages into a file."""
        with open(self.logfile_name, 'a') as freading:
            freading.write(f"{time_str}:{'[INFO]'}{message}")
            freading.write("\n")

    def report(self) -> None:
        """This method summarizes and reports all the activities."""

        with open(self.logfile_name, 'r') as freading:
            warning_value = 0
            alert_value = 0
            lines = freading.readlines()
            for i in lines:
                if '[WARNING]' in i:
                    warning_value += 1
            for i in lines:
                if '[ALERT]' in i:
                    alert_value += 1

            if self.logfile_name == (f"{time_str_file}.log"):
                with open(self.logfile_name, 'a') as freading:
                    freading.write(f"{time_str}:")
                    freading.write("\n")
                    freading.write(f"{time_str}:{'='*60}")
                    freading.write("\n")
                    freading.write(f"{time_str}:{'Total alerts:'} {alert_value}")
                    freading.write("\n")
                    freading.write(f"{time_str}:{'Total warning:'} {warning_value}")
                    freading.write("\n")
                    elapsed_time_sec = finish_time - start_time
                    freading.write(f"{time_str}:Time spent: {elapsed_time_sec:.4f}")

            else:
                with open(self.logfile_name, 'w') as freading:
                    freading.write(f"{time_str}:")
                    freading.write("\n")
                    freading.write(f"{time_str}:{'='*60}")
                    freading.write("\n")
                    freading.write(f"{time_str}:{'Total alerts:'} {alert_value}")
                    freading.write("\n")
                    freading.write(f"{time_str}:{'Total warning:'} {warning_value}")
                    freading.write("\n")
                    elapsed_time_sec = finish_time - start_time
                    freading.write(f"{time_str}:Time spent: {elapsed_time_sec:.4f}")

                print(f"{time_str}:")
                print(f"{time_str}:{'='*60}")
                print(f"{time_str}:{'Total alerts:'} {alert_value}")
                print(f"{time_str}:{'Total warning:'} {warning_value}")
                print(f"{time_str}:Time spent:{elapsed_time_sec:.4f}")


time.sleep(2)
finish_time = time.time()


logger_1 = Logger()  # Generates file with name 2024-05-18-04-32.log

logger_1.show_log_banner("Hello Joe!")
logger_1.show_log_header("Good Bye Joe!")

logger_1.log_banner("Hello R2D2!")
logger_1.log_header("Goodbye R2D2!'")
# What is the correct way to put string on the second line?
logger_1.show_log_init("This initialization message is generated by " +\
                       "show_log_init method")
logger_1.show_log_action("This action message is generated by " +\
                         "show_log_action method")
logger_1.show_log_warning("This warning message is generated by " +\
                          "show_log_warning method")
logger_1.show_log_alert("This alert message is generated by " +\
                        "show_log_alert method")
logger_1.show_log_info("This info message is generated by " +\
                       "show_log_info method")

logger_1.log_init("This initialization message is generated by "\
                  "log_init method")
logger_1.log_action("This action message is generated by "\
                    "log_action method")
logger_1.log_warning("This warning message is generated by "\
                     "log_warning method")
logger_1.log_alert("This alert message is generated by "\
                   "log_alert method")
logger_1.log_info("This info message is generated by "\
                  "log_info method")
logger_1.report()
print()
logger_2 = Logger('my_logfile.log')  # Generates file with name my_logfile.log
logger_2.log_info("This info message is generated by "\
                  "log_info method")
logger_2.report()
