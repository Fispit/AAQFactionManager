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
    
    def addfaction(self, fact:Faction):#accepts a faction type object
        self.factionlist[fact.factionname]=self.factionlist.get(fact.factionname,fact)

    def rmvfaction(self, fact:Faction):
        self.memberlist.pop(fact.factionname)
        
    def transfermember(self, donor,receiver,botename):  #inputs are all strings
        self.factionlist[receiver].addmember(self.factionlist[donor].memberlist[botename])
        self.factionlist[donor].rmvmember(self.factionlist[donor].memberlist[botename])
    
    def transferallmembers(self,donor,receiver):
        for botename in self.factionlist[donor].memberlist.keys():
            self.factionlist[receiver].addmember(self.factionlist[donor].memberlist[botename])
            self.factionlist[donor].rmvmember(self.factionlist[donor].memberlist[botename])
        
    
    def transfermooks(self,donor,receiver,shiptype, number):#transfers specific amount of mooks from one faction to another
        self.factionlist[receiver].addspecificmooks(shiptype,number)
        self.factionlist[donor].rmvspecificmooks(shiptype,number)
                
    def transferallmooks(self,donor, receiver): #normally used when a faction is absorbed, maybe on something else just in case     
        for shiptype in self.factionlist[donor].mooknumbers.keys():
            self.factionlist[receiver].addspecificmooks(shiptype,self.factionlist[donor].mooknumbers[shiptype])
            self.factionlist[donor].rmvspecificmooks(shiptype,self.factionlist[donor].mooknumbers[shiptype])

    def transferslaves(self,donor, receiver, number):
        self.factionlist[receiver].addslaves(number)
        self.factionlist[donor].rmvslaves(number)
        
    def transferallslaves(self,donor,receiver):
        self.factionlist[receiver].addslaves(self.factionlist[donor].slavepop)
        self.factionlist[donor].rmvslaves(self.factionlist[donor].slavepop)
        
    
    
    
    
    
    
    
    
    def nextweek(self):
        #save the current week before anything else.
        
        #end save here
        self.weeknum+=1
        #from this point on it will be progression to the next week
        for key in self.factionlist:
            self.factionlist[key].addweekmooks()
            self.factionlist[key].slavegrowth()
            
    
        
    