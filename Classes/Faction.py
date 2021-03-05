# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 18:02:54 2021

@author: sdelc
"""
from Classes.Shipgirl import Shipgirl
from Classes.ConstructionBay import ConstructionBay
class Faction:
    

    
    def __init__(self,name="nameless",bases=1,slaves=500):
        self.basecount=bases
        self.slavepop=slaves
        self.memberlist=[]
        self.attritiongrowth=0.00
        self.mooknumbers={}
        self.acbnumber=1
        self.baseprod=ConstructionBay()
        self.mookmags={}
        self.baseslavemag=5000
        self.factionname=name
        self.slave2mookratio=1/2
        for key in self.baseprod.production.keys():

            self.mooknumbers[key]=self.mooknumbers.get(key,self.baseprod.production[key]*self.baseprod.prodmultiplier*self.acbnumber)
        
        
    
    def addmember(self, bote: Shipgirl):#Accepts a Shipgirl type object
        self.memberlist.append(bote)

    def rmvmember(self, bote:Shipgirl):
        self.memberlist.pop(bote.name)
            
    def addweekmooks(self):
        for key in self.baseprod.production:
            if key in self.mooknumbers.keys():
                self.mooknumbers[key]+=self.baseprod.production[key]*self.baseprod.prodmultiplier*self.acbnumber
            else:
                self.mooknumbers[key]=self.mooknumbers.get(key,self.baseprod.production[key]*self.baseprod.prodmultiplier*self.acbnumber)
    
    def addspecificmooks(self,key,number):
        self.mooknumbers.get[key]+=number
    
    def rmvspecificmooks(self,key,number):
        self.mooknumbers.get[key]-=number
    
    def mooknum2mag(self,shiptype:str):
        mags=[]
        basemag=self.baseprod.magnumbers[shiptype]
        mags.append(basemag)
        for x in range(1,16):
            mags.append(mags[x-1]*2)
        mags.reverse()
        mooks=self.mooknumbers[shiptype]
        magquant=[]
        for num in mags:
            if mooks%mags[num]==mooks:
                magquant.append(0)
            else:
                magquant.append(1)
                mooks-=num
        magquant.reverse() #puts the mags in order of first value being the lowest mag
        return [magquant,mooks]
        
    def slavenum2mag(self):
        mags=[]
        basemag=self.baseslavemag
        mags.append(basemag)
        for x in range(1,16):
            mags.append(mags[x-1]*2)
        mags.reverse()
        mooks=self.slavepop
        magquant=[]
        for num in mags:
            if mooks%mags[num]==mooks:
                magquant.append(0)
            else:
                magquant.append(1)
                mooks-=num
        magquant.reverse() #puts the mags in order of first value being the lowest mag
        return [magquant,mooks]
    def addslaves(self,num):
        self.slavepop+=num
    def rmvslaves(self,num):
        self.slavepop-=num
    
    def addmookmags(self,numlist,shiptype:str,conveff=1): #numlist is a binary array with the mags being starting at position 0 and increasing, up to mag 16
        mags=[]
        basemag=self.baseprod.magnumbers[shiptype]
        mags.append(basemag)
        for x in range(1,16):
            mags.append(mags[x-1]*2)
        pos=0
        for mag in numlist:
            rawnum=mag*mags[pos]*conveff
            self.addspecificmooks(shiptype,rawnum)
            pos+=1
            
    def addslavemags(self,numlist): #numlist is a binary array with the mags being starting at position 0 and increasing, up to mag 16
        mags=[]
        basemag=self.baseslavemag
        mags.append(basemag)
        for x in range(1,16):
            mags.append(mags[x-1]*2)
        pos=0
        for mag in numlist:
            rawnum=mag*mags[pos]
            self.addslaves(rawnum)
            pos+=1
        
    def rmvmookmags(self,numlist,shiptype:str):
        mags=[]
        basemag=self.baseprod.magnumbers[shiptype]
        mags.append(basemag)
        for x in range(1,16):
            mags.append(mags[x-1]*2)
        pos=0
        for mag in numlist:
            rawnum=mag*mags[pos]
            self.rmvspecificmooks(shiptype,rawnum)
            pos+=1        

    def rmvslavemags(self,numlist): #numlist is a binary array with the mags being starting at position 0 and increasing, up to mag 16
        mags=[]
        basemag=self.baseslavemag
        mags.append(basemag)
        for x in range(1,16):
            mags.append(mags[x-1]*2)
        pos=0
        for mag in numlist:
            rawnum=mag*mags[pos]
            self.rmvslaves(rawnum)
            pos+=1

    def slave2mookconvert(self,numlist):
        self.rmvslavemags(numlist)
        for key in self.baseprod.production.keys():
             self.addmookmags(numlist,key,self.slave2mookratio)   
    



    
    
    