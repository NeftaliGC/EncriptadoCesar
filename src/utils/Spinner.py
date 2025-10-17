import sys
import threading
from functools import wraps

class Spinner:
    def __init__(self, message: str = "Processing"):
        self.message = message
        self.spinner_cycle = ['|', '/', '-', '\\']
        self.stop_running = False
        self.thread = threading.Thread(target=self.spin)

    def spin(self):
        idx = 0
        while not self.stop_running:
            sys.stdout.write(f"\r{self.message} {self.spinner_cycle[idx % len(self.spinner_cycle)]}")
            sys.stdout.flush()
            idx += 1
            threading.Event().wait(0.1)
        sys.stdout.write("\r" + " " * (len(self.message) + 2) + "\r")
        sys.stdout.flush()

    def start(self):
        self.stop_running = False
        self.thread.start()

    def stop(self):
        self.stop_running = True
        self.thread.join()

def with_spinner(message="Processing"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            spinner = Spinner(message)
            spinner.start()
            try:
                result = func(*args, **kwargs)
            finally:
                spinner.stop()
            return result
        return wrapper
    return decorator