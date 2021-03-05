# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 13:18:09 2021

@author: sdelc
"""
from Classes.Shipgirl import Shipgirl
from Classes.Faction import Faction
from Classes.ConstructionBay import ConstructionBay

class AAQWeek:
    
    def __init__(self,week=1,factions={}):
        self.weeknum=week
        self.factionlist=factions
    
    def nextweek(self):
        
        
        #from this point on it will be progression to the next week
        for element in self.factionlist:
            
    
        
    