# https://algo.monster/problems/fill_the_truck
from typing import List

def fillTheTruck(num: int, boxes: List[int], unitSize: int, unitsPerBox: List[int], truckSize: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    res = 0
    boxes_left = truckSize
    s_unitsperbox = sorted([(u, i) for i, u in enumerate(unitsPerBox)], reverse=True)
    # we iterate from the boxes having largest number of units in a greedy manner.
    for units, i in s_unitsperbox:
        if boxes_left <= boxes[i]:
            res += boxes_left * units
            break
        else:
            res += boxes[i] * units
            boxes_left -= boxes[i]
    return res

print(fillTheTruck(3, [1, 2, 3], 3, [3, 2, 1], 3))


          