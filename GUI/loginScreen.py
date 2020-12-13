# importing required Modules
import PySimpleGUI as pyGui
import GUI.sharedVariable as var


# generates PySimpleGUI Main Window
def genwin():
    loginlayout = [[pyGui.Text('Welcome', key=('-Welcome-'), size=(40, 1))],
                   [pyGui.Text('User')],
                   [pyGui.Input(key=('-User-'))],
                   [pyGui.Text('Password')],
                   [pyGui.Input(key=('-Pwd-'), password_char='*')],
                   [pyGui.Button('Login'), pyGui.Button('Exit')]]

    var.loginscreen = pyGui.Window('Login', loginlayout)


# generates PySimpleGUI error Popup window incase of wrong credentials
def generror():
    loginerrorlayout = [[pyGui.Text("User and/or Password In incorrect", text_color='red')]]
    var.loginerrorpopup = pyGui.Window("ERROR", loginerrorlayout, size=(300, 50))


# starts the login screen this function has several conditions for the sequence flow
# the program stops if the window is closed
# if the logged in status is set to true the window closes and the program continues the the main window
def start():
    genwin()
    while True:
        var.event, var.values = var.loginscreen.read()
        if var.event in [pyGui.WINDOW_CLOSED, 'Exit']:
            break
        elif var.event == 'Login':
            login()
            if var.loggedin:
                var.loginscreen.close()


# is the window needs to be closed from another file no current use
def close():
    var.loginscreen.close()


# login check if the credentials are correct the logged in status changes to true else wrong credetnials popup
def login():
    generror()
    if var.values['-User-'] != 'Admin' or var.values['-Pwd-'] != '123456789':
        var.loginerrorpopup.read()
    else:
        var.loggedin = True
