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
    keys = {0}
    for box in boxes:
        index = boxes.index(box)
        unlockable = unlockable and (index in keys)
        for key in box:
            if key < len(boxes):
                keys.add(key)
                for other_key in boxes[key]:
                    if other_key < len(boxes):
                        keys.add(other_key)
    return unlockable
