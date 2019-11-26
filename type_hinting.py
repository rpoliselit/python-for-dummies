"""
Python 3.5+
Type hinting in PyCharm.
"""

from typing import List

def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)

list_avg(123)
