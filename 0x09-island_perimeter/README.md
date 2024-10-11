# 0x09. Island Perimeter

## Description
This project involves calculating the perimeter of an island in a grid. The grid is represented by a 2D list of integers, where `0` represents water and `1` represents land. You will need to create a Python function `def island_perimeter(grid):` that returns the perimeter of the island based on certain conditions. The task focuses on understanding how to navigate 2D arrays (matrices), applying conditional logic to determine the perimeter, and counting techniques to calculate the edges that contribute to the island’s perimeter.

## Learning Objectives
- Understand and work with 2D arrays (matrices) in Python.
- Apply conditional logic to determine perimeter contributions based on land and water cells.
- Use Python programming skills (loops, conditionals, and arrays) to solve geometric problems.
- Reinforce algorithmic thinking by breaking down the problem into smaller tasks.

## Requirements
- All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using **python3 (version 3.4.3)**.
- All Python files should end with a new line.
- The first line of all Python files should be `#!/usr/bin/python3`.
- A `README.md` file at the root of the project folder is mandatory.
- Code must follow the **PEP 8 style guide** (version 1.7).
- You are not allowed to import any module.
- All functions must be documented.
- Files must be executable.

## Function Prototype
```python
def island_perimeter(grid):
    """
    Calculates the perimeter of an island in the given grid.
    """
```

### Function Details:
- **Input**: 
  - `grid`: A 2D list of integers where:
    - `0` represents water.
    - `1` represents land.
    - Cells are connected horizontally and vertically.
    - The grid is completely surrounded by water.
    - Only one island exists, and there are no lakes.
- **Output**:
  - The function returns an integer representing the perimeter of the island.

### Example
```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

print(island_perimeter(grid))
```
**Output**:
```
12
```

## Repository Information
- **GitHub repository**: [alx-interview](https://github.com/IbnuJabir/alx-interview)
- **Directory**: `0x09-island_perimeter`
- **File**: `0-island_perimeter.py`

## Resources
- **Python Official Documentation**: Understanding nested lists and how to work with 2D arrays in Python.
- **GeeksforGeeks**: Guides on multi-dimensional arrays in Python.
- **TutorialsPoint**: Basics of Python lists, how to access and manipulate lists.
- **YouTube Tutorials**: Python 2D arrays and lists.

## Author
- **Kedir Jabir**  
- **Email**: kedirjabir12@gmail.com

--- 

This `README.md` outlines the steps and key details of the **Island Perimeter** project.
