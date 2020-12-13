# importing required Modules
import os
import PySimpleGUI as pyGui
import GUI.sharedVariable as var


# generating the update complete screen
def gencompletedwin():
    completelayout = [[pyGui.Text('System Update Completed')],
                      [pyGui.Button('Exit')]]
    var.completescreen = pyGui.Window('completed', completelayout)


# uses os to run the update and upgrade command takes the root password as a variable
def update(passwd):
    bashcommand = 'echo ' + passwd + ' | sudo -S apt-get update && echo ' + passwd + ' | sudo -S apt-get upgrade -y'
    try:
        os.system(bashcommand)
        print('1111')
    except:
        print('0000')


# Generates the system upgrade screen with the sudo password as input
def genwin():
    updatelayout = [[pyGui.Text('please enter your sudo password: ')],
                    [pyGui.Input(key=('-suPass-'), password_char='*')],
                    [pyGui.Button('Update')],
                    [pyGui.Button('Exit')]]
    var.updatescreen = pyGui.Window('System Update', updatelayout)


# starts the System update process
def start():
    genwin()
    while True:
        var.event, var.values = var.updatescreen.read()
        if var.event in [pyGui.WINDOW_CLOSED, 'Exit']:
            break
        elif var.event == 'Update':
            gencompletedwin()
            update(var.values['-suPass-'])
