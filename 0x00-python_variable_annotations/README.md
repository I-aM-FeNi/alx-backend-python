### README.md

```markdown
# 0x00. Python - Variable Annotations

This project covers the basics of variable annotations in Python. The tasks involve writing type-annotated functions and variables, ensuring code style compliance, and using type checking tools.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Code should use the `pycodestyle` style (version 2.5.)
- All files must be executable
- The length of files will be tested using `wc`
- All modules should have documentation
- All classes should have documentation
- All functions (inside and outside a class) should have documentation
- Documentation should be a real sentence explaining the purpose of the module, class, or method

## Tasks

### 0. Basic annotations - add

Write a type-annotated function `add` that takes a float `a` and a float `b` as arguments and returns their sum as a float.

**File:** `0-add.py`

### 1. Basic annotations - concat

Write a type-annotated function `concat` that takes a string `str1` and a string `str2` as arguments and returns a concatenated string.

**File:** `1-concat.py`

### 2. Basic annotations - floor

Write a type-annotated function `floor` which takes a float `n` as argument and returns the floor of the float.

**File:** `2-floor.py`

### 3. Basic annotations - to string

Write a type-annotated function `to_str` that takes a float `n` as argument and returns the string representation of the float.

**File:** `3-to_str.py`

### 4. Define variables

Define and annotate the following variables with the specified values:
- `a`: an integer with a value of 1
- `pi`: a float with a value of 3.14
- `i_understand_annotations`: a boolean with a value of True
- `school`: a string with a value of "Holberton"

**File:** `4-define_variables.py`

### 5. Complex types - list of floats

Write a type-annotated function `sum_list` which takes a list `input_list` of floats as argument and returns their sum as a float.

**File:** `5-sum_list.py`

### 6. Complex types - mixed list

Write a type-annotated function `sum_mixed_list` which takes a list `mxd_lst` of integers and floats and returns their sum as a float.

**File:** `6-sum_mixed_list.py`

### 7. Complex types - string and int/float to tuple

Write a type-annotated function `to_kv` that takes a string `k` and an int OR float `v` as arguments and returns a tuple. The first element of the tuple is the string `k`. The second element is the square of the int/float `v` and should be annotated as a float.

**File:** `7-to_kv.py`

### 8. Complex types - functions

Write a type-annotated function `make_multiplier` that takes a float `multiplier` as argument and returns a function that multiplies a float by `multiplier`.

**File:** `8-make_multiplier.py`

### 9. Let's duck type an iterable object

Annotate the function `element_length` with the correct types.

**File:** `9-element_length.py`

### 10. Duck typing - first element of a sequence

Augment the function `safe_first_element` with the correct duck-typed annotations.

**File:** `100-safe_first_element.py`

### 11. More involved type annotations

Add type annotations to the function `safely_get_value`.

**File:** `101-safely_get_value.py`

### 12. Type Checking

Use `mypy` to validate the code and apply any necessary changes.

**File:** `102-type_checking.py`

## Usage

To run the scripts, ensure they are executable and use the following command:

```sh
./<script_name>.py
```

To check code style compliance, use:

```sh
pycodestyle <script_name>.py
```

To perform type checking, use:

```sh
mypy <script_name>.py
```

## Author

- [Malcolm Iheremelam](https://github.com/malcolms-anatomy)
```

