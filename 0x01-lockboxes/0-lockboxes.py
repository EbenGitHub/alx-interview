#!/usr/bin/python3
"""
    0-lockboxes.py: canUnlockAll()
"""


def canUnlockAll(boxes):
    """
        checks if the boxes are unlockable or not
        Args:
            boxes (list): boxes which may have keys to other boxes
        Returns: boolean
    """
    unlockable = True
    for box in boxes:
        keys = [0]
        index = boxes.index(box)
        for i in range(len(boxes)):
            if index != i:
                for key in boxes[i]:
                    keys.append(key)
        unlockable = unlockable and (index in keys)
    return unlockable
