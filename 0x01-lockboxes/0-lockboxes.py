#!/usr/bin/env python3
"""lockbox check"""

from typing import List


def canUnlockAll(bs: List[List[int]]) -> bool:
    """lockbox checker"""
    if not bs:
        return False

    n = len(bs)
    visited = [False] * n
    keys = [0]

    while keys:
        box = keys.pop()
        visited[box] = True

        for key in bs[box]:
            if key < n and not visited[key]:
                keys.append(key)

    return all(visited)
