
# `__name__` (A Special Variable) in Python

In Python, `__name__` is a special built-in variable that holds the name of the module currently being executed. It can have two values based on how the code is run:

1. **When the script is executed directly**:
    - The value of `__name__` is `"__main__"`.
    - This indicates that the script is the main program.

2. **When the script is imported as a module**:
    - The value of `__name__` will be the module's name, i.e., the name of the file without the `.py` extension.

## Example:

```python
def main():
    print("This is the main function")

if __name__ == "__main__":
    main()
```

- **When the script is run directly**: The `main()` function is executed because `__name__ == "__main__"`.
- **When imported**: The `main()` function won't execute unless it's explicitly called, since `__name__` will hold the module's name.

## Why is `__name__` useful?

- It allows the file to be used both as a standalone script and as a module in other programs.
- Developers often use this to separate the code meant for execution from reusable functions.

## Common Use Cases:

- Writing scripts that can either be executed directly or imported into other scripts.
- Ensuring that code (like test cases or example usage) is only executed when the file is run directly.
