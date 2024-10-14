## README.md

#### Step 1: Create the `README.md` file
```sh
touch README.md
```

#### Step 2: Write the content for `README.md`

# Python Async Project

This project demonstrates the use of asynchronous programming in Python using the `asyncio` module. The tasks involve creating asynchronous functions and coroutines, measuring execution time, and working with `asyncio.Task`.

## Requirements
- Python 3.7
- Ubuntu 18.04 LTS
- `pycodestyle` style (version 2.5.x)

## Tasks

### Task 0: The basics of async
Write an asynchronous coroutine `wait_random` that takes an integer argument `max_delay` (default value 10) and waits for a random delay between 0 and `max_delay` seconds before returning the delay.

### Task 1: Let's execute multiple coroutines at the same time with async
Write an async routine `wait_n` that takes two integer arguments `n` and `max_delay`. It spawns `wait_random` `n` times with the specified `max_delay` and returns the list of delays in ascending order.

### Task 2: Measure the runtime
Write a function `measure_time` that takes integers `n` and `max_delay` as arguments and measures the total execution time for `wait_n(n, max_delay)`, returning the average time per coroutine.

### Task 3: Tasks
Write a function `task_wait_random` that takes an integer `max_delay` and returns an `asyncio.Task` that wraps the `wait_random` coroutine.

### Task 4: Tasks
Write an async routine `task_wait_n` that takes two integer arguments `n` and `max_delay`. It spawns `task_wait_random` `n` times with the specified `max_delay` and returns the list of delays in ascending order.

## How to Run the Test Scripts

1. **Task 0:**
    ```sh
    chmod +x 0-main.py
    ./0-main.py
    ```

2. **Task 1:**
    ```sh
    chmod +x 1-main.py
    ./1-main.py
    ```

3. **Task 2:**
    ```sh
    chmod +x 2-main.py
    ./2-main.py
    ```

4. **Task 3:**
    ```sh
    chmod +x 3-main.py
    ./3-main.py
    ```

5. **Task 4:**
    ```sh
    chmod +x 4-main.py
    ./4-main.py
    ```

## Repository Structure
```
alx-backend-python/
├── 0x01-python_async_function/
│   ├── 0-basic_async_syntax.py
│   ├── 1-concurrent_coroutines.py
│   ├── 2-measure_runtime.py
│   ├── 3-tasks.py
│   ├── 4-tasks.py
│   ├── 0-main.py
│   ├── 1-main.py
│   ├── 2-main.py
│   ├── 3-main.py
│   ├── 4-main.py
│   └── README.md
```

## License
This project is licensed under the MIT License.
```
