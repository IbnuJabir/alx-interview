# 0x03. Log Parsing

## Description

This project is part of the ALX Software Engineering program, focusing on parsing and processing data streams in real-time using Python. The goal is to read from standard input (stdin), handle data in a specific format, and perform calculations based on the input data. The project involves developing a Python script that reads log data, computes metrics, and handles various edge cases.

## Project Information

- **Project Start Date:** August 26, 2024, 6:00 AM
- **Project End Date:** August 30, 2024, 6:00 AM
- **Checker Release Date:** August 27, 2024, 6:00 AM
- **Weight:** 1

## Concepts and Skills Used

- **File I/O in Python:** Reading from `sys.stdin` line by line.
- **Signal Handling:** Handling keyboard interruption (CTRL + C) using Python's `signal` module.
- **Data Processing:** Parsing strings, extracting specific data points, and aggregating data to compute summaries.
- **Regular Expressions:** Using regex to validate and parse log entries.
- **Dictionaries:** Counting occurrences of status codes and accumulating file sizes.
- **Exception Handling:** Managing exceptions during file reading and data processing.

## Requirements

- **Editors Allowed:** vi, vim, emacs
- **System:** Ubuntu 20.04 LTS
- **Python Version:** Python 3.4.3
- **Code Style:** PEP 8 (version 1.7.x)
- **File Permissions:** All files must be executable
- **Script Requirements:**
  - The first line of each script should be `#!/usr/bin/python3`.
  - Each script should end with a new line.
  - The length of the files will be tested using `wc`.

## Task

### 0. Log Parsing (Mandatory)

Write a Python script named `0-stats.py` that reads stdin line by line and computes metrics:

- **Input Format:** 
  ```
  <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
  ```
  If the format does not match this, the line should be skipped.

- **Output:**
  - After every 10 lines and/or on keyboard interruption (CTRL + C), print the following statistics:
    - **Total file size:** Sum of all file sizes from the input.
    - **Number of lines by status code:** Count occurrences of status codes 200, 301, 400, 401, 403, 404, 405, and 500. Status codes should be printed in ascending order.

### Example

```bash
$ ./0-generator.py | ./0-stats.py
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
...
```

When interrupted with CTRL + C:
```bash
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
```

## Resources

- **[Python Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)**
- **[Python Signal Handling](https://docs.python.org/3/library/signal.html)**
- **[Python Regular Expressions](https://docs.python.org/3/library/re.html)**
- **[Python Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)**
- **[Python Exceptions](https://docs.python.org/3/tutorial/errors.html)**

## Author

This project is done by [Kedir Jabir](mailto:kedirjabir12@gmail.com) as part of the ALX Software Engineering program.