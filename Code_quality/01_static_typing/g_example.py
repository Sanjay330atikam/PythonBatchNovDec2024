"""
Purpose: static typing with mypy
"""

from typing import Dict, List, Tuple

# Traditonal Approach (no function just data objects)
my_data = ("Adam",10,4.5)
print(f"{my_data}")

# adiing Typing
my_data1 : Tuple[str,int,float]=("Adam",10,4.5)
print(f"{my_data1}")

# A list of integers
# Traditonal Approach
numbers = (1,2,3,4,589,30)
print(f"{numbers}")

#Adding Typing
numbers2 : List[int] = [1,2,3,4,59,30]
print(f"numbers2:{numbers2}")

# List io Tuuples-Allias
LattingVector = List[Tuple[float,float]]

points: LattingVector = [
    (25.934, -0.659),
    (-11.456, -166.56),
    (123.11,- 2345),
]
print(f"Points{points =}")
"""
python -m mypy g_example.py
Success: no issues found in 1 source file"""

#  A dictonary where keys are strings and values are int
name_count : Dict[str,int] = {"Adam": 32, "sam":23}

# A list that holds a dict that each hold a string key and value int
list_of_dicts : list[Dict[str,int]] = [{"key":1}, {"key":2}]

#output
"""
) $ python g_example.py
('Adam', 10, 4.5)
('Adam', 10, 4.5)
(1, 2, 3, 4, 589, 30)
numbers2:[1, 2, 3, 4, 59, 30]
Pointspoints =[(25.934, -0.659), (-11.456, -166.56), (123.11, -2345)]
"""
