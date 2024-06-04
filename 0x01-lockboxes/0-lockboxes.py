#!/usr/bin/python3
"""function that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """function that determines if all the boxes can be opened"""

    size = len(boxes)
    closed = set([0])
    stack = list(boxes[0])
    while stack:
        hints = stack.pop()
        if hints < size and hints not in closed:
            closed.add(hints)
            stack.extend(boxes[hints])
    return len(closed) == size
