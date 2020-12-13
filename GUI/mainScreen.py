# importing required Modules
import PySimpleGUI as pyGui
import GUI.sharedVariable as var
import GUI.IPScan as IPScan
import GUI.pwdGen as pwdGen
import GUI.SystemUpgrade as SU


# generating the main program window
def genwin():
    programlayout = [[pyGui.Button('Get IP / IP Scanner')],
                     [pyGui.Button('Password Generator')],
                     [pyGui.Button('System Upgrade')],
                     [pyGui.Button('Software Management')],
                     [pyGui.Button('System Info')],
                     [pyGui.Button('GPIO Status')],
                     [pyGui.Button('Logout')],
                     [pyGui.Button('Exit')]]

    var.programwindow = pyGui.Window('Welcome', programlayout, size=(500, 300), element_justification='c')


# starts the main program and attaches the functions to the buttons
def start():
    genwin()
    while True:
        var.event, var.values = var.programwindow.read()
        if var.event in [pyGui.WINDOW_CLOSED, 'Exit']:
            break
        elif var.event == 'Get IP':
            #print('Get IP --> debugging')
            IPScan.start()
        elif var.event == 'Password Generator':
            #print('Password Generator --> debugging')
            pwdGen.start()
        elif var.event == 'System Upgrade':
            #print("System Upgrade --> debugging")
            SU.start()
        elif var.event == 'Software Management':
            print("Software Management --> coming soon!")
        elif var.event == 'System Info':
            print("System Info --> coming soon!")
        elif var.event == 'GPIO Status':
            print("GPIO Status --> coming soon!")
        elif var.event == 'Logout':
            var.loggedin = False
            if not var.loggedin:
                var.programwindow.close()


# is the window needs to be closed from another file no current use
def close():
    var.programwindow.close()
