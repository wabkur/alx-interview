#!/usr/bin/python3
"""
    Lock boxes problem solution
"""


def canUnlockAll(boxes):
    """
        Returns truthy value if all boxes in array can opened
    """
    # check if boxes is empty
    if len(boxes) == 0:
        return False

    unlocked_set = set()
    unlocked_set.add(0)

    for index, val in enumerate(boxes):
        # check if the index box can not be unlocked
        if index not in unlocked_set:
            return False

        # add key indexes from unlocked box
        for elem in val:
            # go to each element index and update the set
            if elem < len(boxes) and elem > index:
                unlocked_set.update(boxes[elem])
        unlocked_set.update(val)

    return True
