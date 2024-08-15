```markdown
# 0x01 Lockboxes

This repository contains a Python script that solves the Lockboxes problem. The goal of the problem is to determine if all the boxes in a given list can be opened with the available keys.

## Table of Contents

- [Introduction](#introduction)
- [Problem Statement](#problem-statement)
- [Solution Overview](#solution-overview)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

The Lockboxes problem is a classic programming challenge that involves understanding graph traversal and search algorithms. This problem helps in developing problem-solving skills and understanding data structures such as lists, sets, and stacks or queues.

## Problem Statement

You are given `n` number of locked boxes, each numbered from `0` to `n-1`. Each box may contain keys to other boxes. Your task is to write a function `canUnlockAll(boxes)` that returns `True` if all boxes can be opened, otherwise `False`.

### Constraints

- A key with the same number as a box opens that box.
- All keys will be positive integers.
- The first box (`boxes[0]`) is always unlocked.

## Solution Overview

The provided solution uses a graph traversal approach to explore all the boxes and their corresponding keys. It maintains a set of keys to keep track of which boxes can be opened and iteratively checks each box using the keys it contains.

## Usage

To use the function in this repository:

1. Clone the repository:

```bash
git clone https://github.com/IbnuJabir/alx-interview.git
````

Navigate to the specific project directory to view the problem statement and work on the solution:

```bash
cd alx-interview/0x01-lockboxes
```

3. Run the script to test the function with the provided test cases:

```bash
python3 main_0.py
```

### Function Description

- **`canUnlockAll(boxes)`**: Accepts a list of lists `boxes`, where each inner list represents the keys contained in that box. It returns `True` if all boxes can be opened, otherwise `False`.

### Example

```python
from lockboxes import canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Output: True
```

## Contributing

Contributions are welcome! If you have improvements or additional test cases, feel free to submit a pull request.

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push them to your fork.
4. Open a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please contact:

- **Name:** Kedir Jabir
- **Email:** kedirjabir12@gmail.com
- **GitHub:** [IbnuJabir](https://github.com/IbnuJabir)

---

Thank you for exploring the Lockboxes problem! We hope this implementation assists you in understanding graph algorithms and problem-solving techniques.
```