#!/usr/bin/python3
"""lockbox check"""

from typing import List


def canUnlockAll(bs: List[List[int]]) -> bool:
    """lockbox checker"""
    if bs:
        num = len(bs)
        visited = [False] * num
        keys = [0]

        while keys:
            box = keys.pop()
            visited[box] = True

            for key in bs[box]:
                if key < num and not visited[key]:
                    keys.append(key)

        return all(visited)
    else:
        return False
