from venv import logger

from logorator.logger import Logger
import asyncio

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

@Logger()
async def as_func(n=42):
    await asyncio.sleep(1)
    return n


@Logger()
async def main():
    tasks = []
    for i in range(5):
        tasks.append(as_func())
    await asyncio.gather(*tasks)

asyncio.run(main())