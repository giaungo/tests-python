# README

### Requirements

- python 3

### Setup

```
python3.6 -m venv venv
pip install -r requirements.txt

```

#### Tests

```
python -m unittest discover tests -v

```

### Complexity Analysis

- Question 1: Flattern JSON

    Time complexity: O(N * M) (N: number of elements, M: number of nestest elements)

- Question 2: Data Store and Load

    Time complexity: O(N^2)

- Question 3: Find optimal path

    Time complexity: N * log(N)

- Note on Question 03

    Using Depth First Search to detect cyclic and avoid infinite loop caused by cycles
