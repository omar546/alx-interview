#!/usr/bin/python3
"""method to determine if all boxes are openable."""


def canUnlockAll(boxes):
    """it will take a list of lists and it's content will unlock others."""

    keys = [0]
    for k in keys:
        for boxK in boxes[k]:
            if boxK not in keys and boxK < len(boxes):
                keys.append(boxK)
    if len(keys) == len(boxes):
        return True
    return False
