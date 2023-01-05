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
    for box in boxes:
        keys = []
        for i in range(len(boxes)):
            if boxes.index(box) != i:
                for key in boxes[i]:
                    keys.append(key)
        unlockable = True and (boxes.index(box) in keys)
    return unlockable
