#!/usr/bin/python3
"""
Defines a function that determines if a box containing a list
of lists can be opened using keys
"""


def canUnlockAll(boxes):
    """return trure if all boxes unlocked"""
    unlocked_boxes = [0]
    keys = list(boxes[0])

    while keys:
        key = keys.pop()
        if key < len(boxes) and key not in unlocked_boxes:
            unlocked_boxes.append(key)
            keys.extend(boxes[key])

    return len(unlocked_boxes) == len(boxes)