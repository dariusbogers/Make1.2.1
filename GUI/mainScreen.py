import PySimpleGUI as pyGui
import GUI.sharedVariable as var

programLayout = [[pyGui.Button('Get IP')],
                 [pyGui.Button('Password Generator')],
                 [pyGui.Button('System Upgrade')],
                 [pyGui.Button('Software Management')],
                 [pyGui.Button('System Info')],
                 [pyGui.Button('IP Scanner')],
                 [pyGui.Button('GPIO Status')],
                 [pyGui.Button('--upcoming--')],
                 [pyGui.Button('Exit')]]

programWindow = pyGui.Window('Welcome', programLayout, size=(500, 300), element_justification='c')


def start():
    var.event, var.values = programWindow.read()


def close():
    programWindow.close()
