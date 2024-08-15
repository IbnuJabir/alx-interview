```markdown
# 0x00 Pascal's Triangle

This repository contains a Python implementation of Pascal's Triangle, a triangular array of the binomial coefficients. It is a well-known mathematical concept used in combinatorics, algebra, and probability.

## Table of Contents

- [Introduction](#introduction)
- [Pascal's Triangle](#pascals-triangle)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

Pascal's Triangle is a triangular arrangement of numbers where each number is the sum of the two numbers directly above it. This implementation provides a function to generate Pascal's Triangle up to a specified number of rows.

## Pascal's Triangle

The rows of Pascal's Triangle are conventionally enumerated starting with row zero at the top. The values in each row are calculated as the sum of the two values directly above, starting with `1` at the edges.

### Example
```

      1
     1 1
    1 2 1

1 3 3 1
1 4 6 4 1

````

## Usage

The script includes a function that generates Pascal's Triangle. To use the function:

1. Clone the repository:

```bash
git clone https://github.com/IbnuJabir/alx-interview.git
````

2. Navigate to the repository directory:

```bash
cd alx-interview/0x00-pascal_triangle
```

3. Run the Python script to generate Pascal's Triangle:

```bash
python3 0-pascal_triangle.py
```

### Function Description

- **`pascal_triangle(n)`**: Returns a list of lists of integers representing the first `n` rows of Pascal's Triangle.

### Example

```python
from pascal_triangle import pascal_triangle

# Generate the first 5 rows of Pascal's Triangle
rows = pascal_triangle(5)
for row in rows:
    print(row)
```

## Contributing

Contributions are welcome! If you have ideas for improvements or additional features, please submit a pull request.

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push them to your fork.
4. Open a pull request with a description of your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please contact:

- **Name:** Kedir Jabir
- **Email:** kedirjabir12@gmail.com
- **GitHub:** [IbnuJabir](https://github.com/IbnuJabir)

---

Thank you for your interest in Pascal's Triangle! We hope this implementation helps in your explorations of combinatorics and beyond.
