# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 18:34:02 2021

@author: sdelc
"""

from Classes.Shipgirl import Shipgirl
from Classes.Faction import Faction
from Classes.ConstructionBay import ConstructionBay
from Classes.Weeks import AAQWeek
import pickle as pck

initialweek=AAQWeek()

testweek=AAQWeek()

initialweek.addfaction(Faction("Faction1",1,1))

print("Initialweek: This is supposed to change")
print(initialweek.factionlist)
print(initialweek)

print("Testweek: This is not supposed to have anything")
print(testweek.factionlist)
