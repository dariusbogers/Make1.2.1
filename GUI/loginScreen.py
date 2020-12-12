import PySimpleGUI as pyGui
import GUI.sharedVariable as var

loginlayout = [[pyGui.Text('Welcome')],
               [pyGui.Text('User')],
               [pyGui.Input(key=('-User-'))],
               [pyGui.Text('Password')],
               [pyGui.Input(key=('-Pwd-'), password_char='*')],
               [pyGui.Button('Login'), pyGui.Button('Exit')]]

LoginScreen = pyGui.Window('Login', loginlayout)

loginErrorLayout = [[pyGui.Text("User and/or Password In incorrect")]]
loginerrorpopup = pyGui.Window("ERROR", loginErrorLayout, size=(300, 50))


def start():
    var.event, var.values = LoginScreen.read()


def close():
    LoginScreen.close()


def login():
    if var.values['-User-'] != 'Admin' or var.values['-Pwd-'] != '123456789':
        print("User: " + var.values['-User-'] + "\nPassword: " + var.values['-Pwd-'])
        loginerrorpopup.read()
    else:
        print("User: " + var.values['-User-'] + "\nPassword: " + var.values['-Pwd-'])
        print('Login succesful')
        var.LoggedIn = True
