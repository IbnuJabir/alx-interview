#!/usr/bin/python3
"""
Solution to the lockboxes problem.
"""

def canUnlockAll(boxes):
    """
    Determines whether a series of locked boxes can be opened
    based on keys that can be attained.
    Solution to the lockboxes problem
    """
    keys = set([0])
    queue = [0]
    
    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key < len(boxes) and key not in keys:
                keys.add(key)
                queue.append(key)
    
    return len(keys) == len(boxes)
