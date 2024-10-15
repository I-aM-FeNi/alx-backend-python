### README.md

# 0x02. Python - Async Comprehension

## Description
This project contains tasks related to asynchronous programming in Python, specifically focusing on async comprehensions. The tasks involve creating coroutines that generate random numbers asynchronously, using async comprehensions to collect these numbers, and measuring the runtime of parallel executions.

## Requirements
- Python 3.7
- Ubuntu 18.04 LTS
- `pycodestyle` style (version 2.5.x)

## Project Structure
```
alx-backend-python/
└── 0x02-python_async_comprehension/
    ├── 0-async_generator.py
    ├── 0-main.py
    ├── 1-async_comprehension.py
    ├── 1-main.py
    ├── 2-measure_runtime.py
    ├── 2-main.py
    └── README.md
```

## Tasks

### 0. Async Generator
Write a coroutine called `async_generator` that takes no arguments. The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the random module.

**File:** `0-async_generator.py`

**Test File:** `0-main.py`
```sh
./0-main.py
```

### 1. Async Comprehensions
Import `async_generator` from the previous task and then write a coroutine called `async_comprehension` that takes no arguments. The coroutine will collect 10 random numbers using an async comprehension over `async_generator`, then return the 10 random numbers.

**File:** `1-async_comprehension.py`

**Test File:** `1-main.py`
```sh
./1-main.py
```

### 2. Run time for four parallel comprehensions
Import `async_comprehension` from the previous file and write a `measure_runtime` coroutine that will execute `async_comprehension` four times in parallel using `asyncio.gather`. `measure_runtime` should measure the total runtime and return it.

**File:** `2-measure_runtime.py`

**Test File:** `2-main.py`
```sh
./2-main.py
```

## Usage
To run the test scripts, navigate to the project directory and execute the respective test files. Ensure the scripts are executable:
```sh
chmod +x 0-main.py 1-main.py 2-main.py
```

Then run the test scripts:
```sh
./0-main.py
./1-main.py
./2-main.py
```

## Documentation
All modules and functions are documented. You can view the documentation by running:
```sh
python3 -c 'print(__import__("module_name").__doc__)'
python3 -c 'print(__import__("module_name").function_name.__doc__)'
```

## Style Guide
This project follows the `pycodestyle` style guide (version 2.5.x). Ensure your code adheres to this style.

## License
This project is licensed under the MIT License.
```
