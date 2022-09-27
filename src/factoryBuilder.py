#!/usr/bin/python3

from iron import IronMine

myMine = IronMine(2, 1, 75, 60)

print(myMine.get_inputs())
print(myMine.get_outputs())
print(myMine.get_power())
print(myMine.get_iron_per_min())