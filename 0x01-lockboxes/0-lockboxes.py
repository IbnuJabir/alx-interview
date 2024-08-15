#!/usr/bin/python3
"""
Solution to the lockboxes problem.
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened with the keys available.
    
    Parameters:
    boxes (list of list of int): A list where each sublist contains the keys available in that particular box.
    
    Returns: bool: True if all boxes can be opened, False otherwise.
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
