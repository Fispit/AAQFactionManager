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
import PySimpleGUI as sg

sg.theme("DarkAmber")


def addfactionwindow():
    layout = [[sg.Text('Faction Name'), sg.Input(key='-fname-')],
              [sg.Text("Number of Bases"), sg.Input(key="-basenum-")],
              [sg.Text("Number of Slaves"), sg.Input(key="-slavenum-")],
              [sg.Button('Add'), sg.Exit()]]

    window = sg.Window('Add Faction', layout)

    while True:  # The Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        elif event == "Add" and values["-fname-"] != None:
            if (values["-basenum-"].isdecimal or values["-basenum-"] == None) and (
                    values["-slavenum-"].isdecimal or values["-slavenum-"] == None):
                window.close()
                return Faction(values["-fname-"], int(values["-basenum-"]), int(values["-slavenum-"]))
            else:
                sg.Popup("Please put number values or nothing for base numbers or slave numbers.")
    window.close()


def removefactionwindow(namelist):
    layout = [[sg.Combo(namelist, size=(25, 5), key="-factions-"), sg.Button("Remove"), sg.Button("Exit")]]
    window = sg.Window("Remove Faction", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit' or None:
            break
        if event == "Remove":
            window.close()
            return values["-factions-"]
    window.close()


weeklist = {}
weeklist["Currentweek"] = weeklist.get("Currentweek", AAQWeek())
# Add a load file option as a default and this in case there is nothing to load.
weeklist["Currentweek"].addfaction(Faction("Dumbass"))
weeklist["Currentweek"].addfaction(Faction("assdumb"))
invincible=Shipgirl("Invincible","BB")
kaguya=Shipgirl("Kaguya","DD")
weeklist["Currentweek"].factionlist["assdumb"].addmember(kaguya)
weeklist["Currentweek"].factionlist["assdumb"].addmember(invincible)
aval_types = ["SS", "DD", "CL", "CA", "CVL", "BB", "CV", "Installation", "Other"]  # same as the shipgirl class
factionlist = []
for key in weeklist["Currentweek"].factionlist.keys():
    factionlist.append(key)

firstcolumn = [
    [sg.Text("Faction Manager")],
    [sg.Combo(factionlist, size=(25, 5), key="-factionname-", enable_events=True), sg.Button("View", key="-updateall-"),
     sg.Button("Add Faction", key="-addfaction-"), sg.Button("Remove Faction", key="-rmvfaction-", enable_events=True)],
    [sg.Text("Memberlist")],
    [sg.Text("Faction Shipgirls"), sg.Text("Total girls:"),sg.Text("Number", key=("-botecount-"))],
    [sg.Listbox([], key="-botelist-", size=(60, 15))],
    [sg.Button("Add Bote", key="-addbote-"), sg.Button("Remove Bote", key="-rmvbote-"),
     sg.Button("Transfer Bote", key="-transfbote-")]
]

secondcolumn = [
    [sg.Text("Mook Mags")],
    [sg.Text("Mook Mag Numbers", key=("-mookmagnum-"))],
    [sg.Text("Mooks Raw")],
    [sg.Text("Mook Raw Numbers", key=("-mookrawnum-"))],
    [sg.Text("Production")],
    [sg.Text("Production Mags", key=("-prodmags-")), sg.Text("Production Raw", key=("-prodraw-"))],
    [sg.Text("ACB Numbers: "), sg.Text("", key=("-acbnums-"))],
    [sg.Text("Production per ACB")],
    [sg.Text("",key="-acbprod-")]
]

thirdcolumn = [
    [sg.Text("Week #" + str(weeklist["Currentweek"].weeknum))],
    [sg.Text("Resources:")],
    [sg.Text("Resources display",key="-resourcecount-")],
    [sg.Text("Resource Income:")],
    [sg.Text("Income Display",key="-resincome-")],
    [sg.Text("Slave Population:"), sg.Text("Numbers",key="-slavepopraw-")],
    [sg.Text("Slave Mags:")],
    [sg.Text("Mags",key="-slavepopmags-")],
    [sg.Text("Slave to Mook Conversion")],
    [sg.Text("Slave to Mooks Conversion")],
    [sg.Text("Conversion Efficiency")],
    [sg.Button("Convert Mags")]
]
layout = [[sg.Column(firstcolumn), sg.VSeperator(), sg.Column(secondcolumn), sg.VSeperator(), sg.Column(thirdcolumn)]]
window = sg.Window("AAQ - Faction Manager", layout)
while True:
    print("update attempt")
    event, values = window.read()  # add a check with a while loop around here to have a constantly updating ui based on faction.  Similar to the updateall call
    print(event)
    if event == "-addfaction-":
        newfaction = addfactionwindow()
        if newfaction == None:
            newfaction = newfaction
        else:
            weeklist["Currentweek"].addfaction(newfaction)
        factionlist = []
        for key in weeklist["Currentweek"].factionlist.keys():
            factionlist.append(key)
        window.Element("-factionname-").update(values=factionlist)
    if event == "-rmvfaction-":
        deletedfaction = removefactionwindow(factionlist)
        if deletedfaction == None:
            deletedfaction = deletedfaction
        else:
            weeklist["Currentweek"].rmvfaction(weeklist["Currentweek"].factionlist[deletedfaction])
        factionlist = []
        for key in weeklist["Currentweek"].factionlist.keys():
            factionlist.append(key)
        window.Element("-factionname-").update(values=factionlist)
    elif event == sg.WIN_CLOSED:
        break
    elif event == "-updateall-":  # this will update all the elements in the UI with the faction's info
        factionname = values["-factionname-"]
    elif event == "-factionname-":
        print("This changes all values when changing to faction: " + values["-factionname-"])
        #start by updating shipgirl counts and the list of names

        botelistupdate=[]
        botelist=weeklist["Currentweek"].factionlist[values["-factionname-"]].memberlist
        yest=[]
        for girl in botelist:
            yest.append(girl)
            botelistupdate.append(botelist[girl].shiptype+"-"+botelist[girl].name)
        botelistupdate.sort()
        window.Element("-botelist-").Update(values=botelistupdate)
        numbotes=str(len(botelistupdate))
        window.Element("-botecount-").Update(value=numbotes)
        #Shipgirl update is complete
        
        
        
    else:
        print("Error")

window.close()


def updateall(factionname, layout):
    print("All window elements are updated here")
