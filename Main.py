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


firstcolumn=[
    [
     sg.Text("Faction Manager")
     ],
    [
     sg.Text("Drop Down Faction List"),
     sg.Text("Add Faction/Remove Faction"),
     ],
    
    [
     sg.Text("Memberlist goes here")
     ],
    [
     sg.Text("Add Bote"),sg.Text("Remove Bote"),sg.Text("Transfer Bote")
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





layout=[[sg.Column(firstcolumn),sg.VSeperator(),sg.Column(secondcolumn)]]
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