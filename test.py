from logorator.logger import Logger

@Logger(mode="normal")
def task(name):
    for i in range(3):
        dummy_function(name, i)

@Logger(mode="short")
def dummy_function(name, iteration):
    for i in range(3):
        inner(name, i)
    return f"Dummy function for {name} on iteration {iteration}"

@Logger(mode="normal")
def inner(name, iteration):
    return f"Inner function for {name} on iteration {iteration}"

task(name="some task")