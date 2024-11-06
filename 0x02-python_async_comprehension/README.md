# alx-backend-python
# Python Async Comprehension

This project focuses on asynchronous programming in Python, specifically using async comprehensions. The goal is to understand how to use async comprehensions to handle asynchronous iterators and generators efficiently.

## Learning Objectives

- Understand the basics of asynchronous programming in Python
- Learn how to use `async` and `await` keywords
- Implement asynchronous comprehensions
- Handle asynchronous iterators and generators

## Requirements

- Python 3.7 or higher
- `asyncio` module

## Project Structure

- `0-async_generator.py`: Contains a coroutine called `async_generator` that loops 10 times, each time asynchronously waits 1 second, then yields a random number between 0 and 10.
- `1-async_comprehension.py`: Contains a coroutine called `async_comprehension` that collects 10 random numbers using an async comprehending over `async_generator`, then returns the 10 random numbers.
- `2-measure_runtime.py`: Contains a coroutine called `measure_runtime` that executes `async_comprehension` four times in parallel using `asyncio.gather` and measures the total runtime.

## Usage

To run the scripts, use the following commands:

```sh
python3 0-async_generator.py
python3 1-async_comprehension.py
python3 2-measure_runtime.py
```

## Author

Muktr

## License

This project is licensed under the MIT License.