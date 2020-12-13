# import hashlib
#
# test = hashlib.md5("Hallo World".encode())
# print(hashlib.md5("Hallo World".encode).hexdigest() == b'2bdb9e0e0220c27394afda6a1a105eee')
import PySimpleGUI as pyGui
import GUI.sharedVariable as var



def genwin1():
    layout1 = [[pyGui.Button('login'), pyGui.Button('Exit')]]
    var.window1 = pyGui.Window('login', layout1)

def genwin2():
    layout2 = [[pyGui.Button('logout'), pyGui.Button('Exit')]]
    var.window2 = pyGui.Window('logout', layout2)

def start1():
    genwin1()
    while True:
        event, values = var.window1.read()
        if event in [pyGui.WINDOW_CLOSED, 'Exit']:
            break
        elif event == 'login':
            var.loggedin = True
            if var.loggedin:
                var.window1.close()

def start2():
    genwin2()
    while True:
        event, values = var.window2.read()
        if event in [pyGui.WINDOW_CLOSED, 'Exit']:
            break
        elif event == 'logout':
            var.loggedin = False
            if not var.loggedin:
                var.window2.close()


while True:
    if not var.loggedin:
        start1()
        if not var.loggedin:
            break
    elif var.loggedin:
        start2()
        if var.loggedin:
            break
    else:
        break