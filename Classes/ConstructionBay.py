# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 17:18:45 2021

@author: sdelc
"""

class ConstructionBay:
    magnumbers={"DD":600,"CL":300, "Transport":240,"CVL":100,"CA":40,"CLM":300,"BB":20,"CV":20,"SS":240,"BBM":20,"La":100,"CLT":300}

    def __init__(self):
        self.production={"DD":60,"CL":30,"Transport":24,"CVL":10,"CA":4,"BB":2,"CV":2,"SS":24,"La":10}
        self.prodmultiplier=1
        
    def addprodtype(self,shiptype:str):#Adds production to ACB from the selected shiptype, gotten from magnumbers
        self.production[shiptype]=self.production.get(shiptype,self.magnumbers[shiptype]/10)
    def addmagtype(self,shiptype:str,prodamount:int):#Only use to add a new type with the typical mag number
        self.magnumbers.get(shiptype,prodamount)
    def remmagtype(self,shiptype:str):
        self.magnumbers.pop(shiptype)
    def removetype(self,shiptype:str): 
        self.production.pop(shiptype)           
    def gettypes(self):
        return self.production.keys()
    def getmagtypes(self):
        return self.magnumbers.keys()
    def changeprod(self, thekey:str,newnumber:int):
        self.production[thekey]=newnumber
    def getbaseprod(self):
        mooknums=""
        for key in self.production:
            mooknums+=f"{key}: {self.production[key]}\n"
        return mooknums
            
        
    
        