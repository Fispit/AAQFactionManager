# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 18:02:54 2021

@author: sdelc
"""
from Classes.Shipgirl import Shipgirl
from Classes.ConstructionBay import ConstructionBay
class Faction:
    

    
    def __init__(self,namae="nameless",bases=1,slaves=500):
        self.basecount=bases
        self.slavepop=slaves
        self.memberlist={}
        self.attritiongrowth=0.00  # fraction of growth(+) and attrition(-) 
        self.mooknumbers={}
        self.acbnumber=1
        self.baseprod=ConstructionBay()
        self.mookmags=[]
        self.slavemags=[]
        self.baseslavemag=5000
        self.factionname=namae
        self.slave2mookratio=1/2  #2 slave mags for 1 mook mag
        self.resourcemode=1
        self.resources={"Steel":0,"Fuel":0,"Ammo":0,"Exotics":0,"Matter":0,"Energy":0}
        self.resourceincome={"Steel":0,"Fuel":0,"Ammo":0,"Exotics":0,"Matter":0,"Energy":0}
        for key in self.baseprod.production.keys():

            self.mooknumbers[key]=self.mooknumbers.get(key,self.baseprod.production[key]*self.baseprod.prodmultiplier*self.acbnumber)
        
    
    #Might need to alter member adding and removing in the future
    def addmember(self, bote: Shipgirl):#Accepts a Shipgirl type object
        self.memberlist[bote.name]=self.memberlist.get(bote.name,bote)

    def rmvmember(self, bote:Shipgirl):
        self.memberlist.pop(bote.name)
        
    
            
    def addweekmooks(self):
        for key in self.baseprod.production:
            if key in self.mooknumbers.keys():
                self.mooknumbers[key]+=int(self.baseprod.production[key]*self.baseprod.prodmultiplier*self.acbnumber)
            else:
                self.mooknumbers[key]=int(self.mooknumbers.get(key,self.baseprod.production[key]*self.baseprod.prodmultiplier*self.acbnumber))
    
    def addspecificmooks(self,key,number):
        self.mooknumbers[key]+=number
    
    def rmvspecificmooks(self,key,number):
        self.mooknumbers[key]-=number
    def setmooks(self,key,number):
        self.mooknumbers[key]=number
        
    def getmooknums(self):
        mookreturn=""
        for shiptype in self.mooknumbers:
            mookreturn+=str(shiptype)+": "+str(self.mooknumbers[shiptype])+"\n"
        return mookreturn

    def addmookmags(self,numlist,shiptype:str,conveff=1): #numlist is a binary array with the mags being starting at position 0 and increasing, up to mag 20
        mags=[]
        basemag=self.baseprod.magnumbers[shiptype]
        mags.append(basemag)
        for x in range(1,20):
            mags.append(mags[x-1]*2)
        pos=0
        for mag in numlist:
            rawnum=mag*mags[pos]*conveff
            self.addspecificmooks(shiptype,rawnum)
            pos+=1

    def rmvmookmags(self,numlist,shiptype:str):
        mags=[]
        basemag=self.baseprod.magnumbers[shiptype]
        mags.append(basemag)
        for x in range(1,20):
            mags.append(mags[x-1]*2)
        pos=0
        for mag in numlist:
            rawnum=mag*mags[pos]
            self.rmvspecificmooks(shiptype,rawnum)
            pos+=1        
                

    def mooknum2mag(self):
        magstring=""
        print("---------")
        for shiptype in self.mooknumbers:
            mags=[]

            basemag=self.baseprod.magnumbers[shiptype]

                
            mags.append(basemag)
            for x in range(1,20):
                mags.append(mags[x-1]*2)
            mags.reverse()
            
            mooks=self.mooknumbers[shiptype]

            magquant=[]
            
            for num in mags:
                if mooks%num==mooks:
                    magquant.append(0)
                else:
                    magquant.append(1)
                    mooks-=num
            print("2")
            magamount=len(mags)
            magstring+=shiptype+": "
            for status in magquant:
                
                if status==1:
                    magstring+=str(magamount)+"+"
                    magamount-=1
                else:
                    magamount-=1
            if magstring[len(magstring)-1]=="+":
                magstring=magstring[0:len(magstring)-1]
            magstring+="\n"
        
        return magstring
        
    def slavenum2mag(self):
        mags=[]
        basemag=self.baseslavemag
        mags.append(basemag)
        for x in range(1,20):
            mags.append(mags[x-1]*2)
        mags.reverse()
        mooks=self.slavepop
        magquant=[]
        for num in mags:
            if mooks%num==mooks:
                magquant.append(0)
            else:
                magquant.append(1)
                mooks-=num
        magamount=len(mags)
        magstring="Slave Mags: " 
        for status in magquant:
            if status==1:
                magstring+=str(magamount)+"+"
                magamount-=1
            else:
                magamount-=1
        if magstring[len(magstring)-1]=="+":
            magstring=magstring[0:len(magstring)-1]
        return magstring
    
    def getprodmags(self):
        magstring=""
        for shiptype in self.baseprod.production:
            mags=[]
            basemag=self.baseprod.magnumbers[shiptype]
            mags.append(basemag)
            for x in range(1,20):
                mags.append(mags[x-1]*2)
            mags.reverse()
            mooks=self.baseprod.production[shiptype]*self.acbnumber
            magquant=[]
            for num in mags:
                if mooks%num==mooks:
                    magquant.append(0)
                else:
                    magquant.append(1)
                    mooks-=num

            magamount=len(mags)
            magstring+=shiptype+": "
            for status in magquant:
                if status==1:
                    magstring+=str(magamount)+"+"
                    magamount-=1
                else:
                    magamount-=1
            if magstring[len(magstring)-1]=="+":
                magstring=magstring[0:len(magstring)-1]
            magstring+="\n"
        return magstring
    
    def getprodraw(self):
        mookreturn=""
        for shiptype in self.baseprod.production:
            mookreturn+=str(shiptype)+": "+str(self.baseprod.production[shiptype]*self.acbnumber)+"\n"
        return mookreturn
    def addslaves(self,num):
        self.slavepop+=num
    def rmvslaves(self,num):
        self.slavepop-=num
    def setslaves(self,num):
        self.slavepop=num
        
    def getslavenums(self):
        mookreturn=str(self.slavepop)
        return mookreturn
            

    def addslavemags(self,numlist): #numlist is a binary array with the mags being starting at position 0 and increasing, up to mag 20
        mags=[]
        basemag=self.baseslavemag
        mags.append(basemag)
        for x in range(1,20):
            mags.append(mags[x-1]*2)
        pos=0
        for mag in numlist:
            rawnum=mag*mags[pos]
            self.addslaves(rawnum)
            pos+=1
        


    def rmvslavemags(self,numlist): #numlist is a binary array with the mags being starting at position 0 and increasing, up to mag 20
        mags=[]
        basemag=self.baseslavemag
        mags.append(basemag)
        for x in range(1,20):
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
    
    def slavegrowth(self):
        self.slavepop*=(1+self.attritiongrowth)
        if self.slavepop<0:
            self.slavepop=0
    
    
    def changeresmode(self):
        if self.resourcemode==1:
            self.resourceincome["Matter"]=self.resourceincome["Steel"]+self.resourceincome["Exotics"]
            self.resourceincome["Energy"]=self.resourceincome["Fuel"]+self.resourceincome["Ammo"]
            self.resources["Matter"]=self.resources["Steel"]+self.resources["Exotics"]
            self.resources["Energy"]=self.resources["Fuel"]+self.resources["Ammo"]
            self.resourcemode=2
        elif self.resourcemode==2:
            self.resourcemode==1 #made so that the user can go back in case of accidentally changing modes.
            
    def addresources(self,restype,amount):
        self.resources[restype]+=amount
    def rmvresources(self,restype,amount):
        self.resources[restype]-=amount
    def setresources(self,restype,amount):
        self.resources[restype]=amount

    def addresincome(self,restype,amount):
        self.resourceincome[restype]+=amount
    def rmvresincome(self,restype,amount):
        self.resourceincome[restype]-=amount
    def setresincome(self,restype,amount):
        self.resourceincome[restype]=amount
        
    def addweeklyresources(self):
        for element in self.resourceincome:
            self.addresources(element,self.resourceincome[element])
            
    def getincome(self):
        
        incomereturn=""

        for element in self.resources:
            if self.resourcemode==1:
                if not(element=="Matter" or element=="Energy"):
                    incomereturn+=str(element)+": "+str(self.resourceincome[element])+"\n"
            elif self.resourcemode==2:
                if element=="Matter" or element=="Energy":
                    incomereturn+=str(element)+": "+str(self.resourceincome[element])+"\n"

        
        return incomereturn
        
        
    def getres(self):
        
        incomereturn=""

        for element in self.resources:
            if self.resourcemode==1:
                if not(element=="Matter" or element=="Energy"):
                    incomereturn+=str(element)+": "+str(self.resources[element])+"\n"
            elif self.resourcemode==2:
                if element=="Matter" or element=="Energy":
                    incomereturn+=str(element)+": "+str(self.resources[element])+"\n"

        
        return incomereturn



    
    
    