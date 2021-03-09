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



weeklist={}
weeklist["Currentweek"]=weeklist.get("Currentweek",AAQWeek())
#Add a load file option as a default and this in case there is nothing to load.
weeklist["Currentweek"].addfaction(Faction("Dumbass"))
weeklist["Currentweek"].addfaction(Faction("assdumb"))

aval_types=["DD","CL","CA","CVL","BB","CV","Installation","Other"] #same as the shipgirl class
factionlist=[]

for key in     weeklist["Currentweek"].factionlist.keys():
    factionlist.append(key)

firstcolumn=[
    [
     sg.Text("Faction Manager")
     ],
    [
    # sg.Text("Drop Down Faction List"),

     sg.Combo([],size=(25,5),key="-factionname-"),
     sg.Button("Add Faction",key="-addfaction-"),sg.Button("Remove Faction",key="-rmvfaction-",enable_events=True)
     ],
    
    [
     sg.Text("Memberlist")
     ],
    [
     sg.Text("Installations")],
    [
     sg.Listbox([],key="-mem_inst-",size=(25,5))
     ],
    [
     sg.Text("CV")
     ],
    [
     sg.Listbox([],key="-mem_cv-",size=(25,5))
     ],
    [
     sg.Text("BB")],
    [
     sg.Button("Add Bote",key="-addbote-"),sg.Button("Remove Bote",key="-rmvbote-"),sg.Button("Transfer Bote",key="-rmvbote-")
     ]
    ]

secondcolumn=[
    [
     sg.Text("Mook Mags")
     ],
    [
     sg.Text("Mook Mag Numbers")
     ],
    [
     sg.Text("Mooks Raw")
     ],
    [
     sg.Text("Mook Raw Numbers")
     ],
    [
     sg.Text("Production")
     ],
    [
     sg.Text("Production Mags"),
     sg.Text("Production Raw")
     ],
    [
     sg.Text("ACB Numbers")
     ],
    [sg.Text("Production per ACB")]
    ]

thirdcolumn=[
    [
     sg.Text("Week #X")
     ],
    [
     sg.Text("Resources")
     ],
    [
     sg.Text("Resources display")
     ],

    [
     sg.Text("Slave Population:Number"),
     sg.Text("Numbers")
     ],
    [
     sg.Text("Slave Mags:"),
     sg.Text("Mags")
     ],
    [
     sg.Text("Slave to Mook Conversion")
     ],
     [
      sg.Text("Slave to Mooks Conversion")
      ],
     [
      sg.Text("Conversion Efficiency")
      ],
     [
      sg.Button("Convert Mags")
      
      ]

    ]





layout=[[sg.Column(firstcolumn),sg.VSeperator(),sg.Column(secondcolumn),sg.VSeperator(),sg.Column(thirdcolumn)]]
window=sg.Window("Demo", layout)

while True:
    event,values=window.read()
    
    if event=="OK" or event == sg.WIN_CLOSED():
        break
    
    
window.close()


# import os.path


# # First the window layout in 2 columns


# file_list_column = [

#     [

#         sg.Text("Image Folder"),

#         sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),

#         sg.FolderBrowse(),

#     ],

#     [

#         sg.Listbox(

#             values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"

#         )

#     ],

# ]


# # For now will only show the name of the file that was chosen

# image_viewer_column = [

#     [sg.Text("Choose an image from list on left:")],

#     [sg.Text(size=(40, 1), key="-TOUT-")],

#     [sg.Image(key="-IMAGE-")],

# ]


# # ----- Full layout -----

# layout = [

#     [

#         sg.Column(file_list_column),

#         sg.VSeperator(),

#         sg.Column(image_viewer_column),

#     ]

# ]


# window = sg.Window("Image Viewer", layout)


# # Run the Event Loop

# while True:

#     event, values = window.read()

#     if event == "Exit" or event == sg.WIN_CLOSED:

#         break

#     # Folder name was filled in, make a list of files in the folder

#     if event == "-FOLDER-":

#         folder = values["-FOLDER-"]

#         try:

#             # Get list of files in folder

#             file_list = os.listdir(folder)

#         except:

#             file_list = []


#         fnames = [

#             f

#             for f in file_list

#             if os.path.isfile(os.path.join(folder, f))

#             and f.lower().endswith((".png", ".gif"))

#         ]

#         window["-FILE LIST-"].update(fnames)

#     elif event == "-FILE LIST-":  # A file was chosen from the listbox

#         try:

#             filename = os.path.join(

#                 values["-FOLDER-"], values["-FILE LIST-"][0]

#             )

#             window["-TOUT-"].update(filename)

#             window["-IMAGE-"].update(filename=filename)


#         except:

#             pass


# window.close()