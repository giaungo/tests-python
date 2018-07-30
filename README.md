# README

### Requirements

- python 3

### Setup

```
python3.6 -m venv .venv
pip install -r requirements.txt

```

#### Tests

```
python -m unittest discover tests -v

```

### Complexity Analysis

- Question 1: Flattern JSON

    Time complexity: O(NM) (N: number of elements, M: number of nestest elements)

    Space complexity: 0(N) (N: number of elements)

- Question 2: Data Store and Load

    Time complexity: O(NM) (N: number of items, M: number of key value pairs)

    Space complexity: O(N) (N: number of items)

- Question 3: Find optimal path

    Time complexity: O(EV) (E: number of edges, V: number of vertices)

    Space complexity: O(V) (V: number of vertices)

- Note on Question 03

    Using Depth First Search to detect cyclic and avoid infinite loop caused by cycles
