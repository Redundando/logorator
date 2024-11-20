import threading
from logorator.logger import Logger

@Logger(override_function_name="uiuiui")
def task(name):
    for i in range(3):
        Logger.note(f"Task {name} iteration {i}")
        dummy_function(name, i)

@Logger()
def dummy_function(name, iteration):
    return f"Dummy function for {name} on iteration {iteration}"

# Run tasks in parallel threads
threads = [
    threading.Thread(target=task, args=(f"Thread-{i}",))
    for i in range(2)
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
