from typing import List


def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
    counter = 0
    for row in G:
        for cell in row:
            counter += cell

    return counter / (R * C)
