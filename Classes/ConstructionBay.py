# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 17:18:45 2021

@author: sdelc
"""

class ConstructionBay:

    def __init__(self):
        self.production={"DD":60,"CL":30, "Transport":24,"CVL":10,"CA":4,"CLM":30,"BB":2,"CV":2,"SS":24,"BBM":2,"La":10}
        self.magnumbers={"DD":600,"CL":300, "Transport":240,"CVL":100,"CA":40,"CLM":300,"BB":20,"CV":20,"SS":240,"BBM":20,"La":100}
        self.prodmultiplier=1
    def addtype(self,shiptype:str,prodamount:int):#Only use to add a new type with the typical mag number
        self.production.get(shiptype,prodamount/10)    
        self.magnumbers.get(shiptype,prodamount)
    def removetype(self,shiptype:str): 
        self.production.pop(shiptype)   
            
    def gettypes(self):
        return self.production.keys()
    def changeprod(self, thekey:str,newnumber:int):
        self.production[thekey]=newnumber
        