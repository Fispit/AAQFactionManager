# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 16:42:51 2021

@author: sdelc
"""

class Shipgirl:

    
    aval_types=["SS","DD","CL","CA","CVL","BB","CV","Installation","Other"]

    def __init__(self,name,shiptype):
        self.name=name
        self.notes="None"
        self.affiliation="Undefined"
        if shiptype in self.aval_types:
            self.shiptype=shiptype
        else:
            self.shiptype="Other"
        
    