import PySimpleGUI as pyGui
import PasswordGenerator as pwdGen

pwd = ""
test = 'Hallo'

loggedIn = False
bitlength = [128, 256, 512]

loginlayout = [[pyGui.Text('Welcome')],
               [pyGui.Text('User')],
               [pyGui.Input(key=('-User-'))],
               [pyGui.Text('Password')],
               [pyGui.Input(key=('-Pwd-'),password_char='*')],
               [pyGui.Button('Login'), pyGui.Button('Exit')]]

LoginScreen = pyGui.Window('Login', loginlayout)

programLayout = [[pyGui.Button('Get IP')],
                 [pyGui.Button('Password Generator')],
                 [pyGui.Button('System Upgrade')],
                 [pyGui.Button('Software Management')],
                 [pyGui.Button('System Info')],
                 [pyGui.Button('IP Scanner')],
                 [pyGui.Button('GPIO Status')],
                 [pyGui.Button('--upcoming--')],
                 [pyGui.Button('exit')]]

programWindow = pyGui.Window('Welcome', programLayout, size=(500, 300), element_justification='c')

loginErrorLayout = [[pyGui.Text("User and/or Password In incorrect")]]
loginerrorpopup = pyGui.Window("ERROR", loginErrorLayout, size=(300, 50))

pwdgenLayout = [[pyGui.Text('select Bit length')],
                [pyGui.Combo(bitlength, size=(8, 4), key=('-BitLength-'))],
                [pyGui.Button('Generate')]]
pwdgenScreen = pyGui.Window('Password Generator', pwdgenLayout)

pwdLayout = [[pyGui.Text(pwd)]]
pwdScreen = pyGui.Window('Generated Password', pwdLayout, size=(200, 80))

while True:
    event, values = LoginScreen.read()
    if event == pyGui.WINDOW_CLOSED or event == 'Exit':
        break
    elif event == 'Login':
        if values['-User-'] != 'Admin' or values['-Pwd-'] != '123456789':
            print("User: " + values['-User-'] + "\nPassword: " + values['-Pwd-'])
            loginerrorpopup.read()
        else:
            LoginScreen.close()
            event, values = programWindow.read()

            if event == 'Password Generator':
                event, values = pwdgenScreen.read()
                if event == 'Generate':
                    print(values['-BitLength-'])
                    j = values['-BitLength-']
                    pwd = pwdGen.genpwd(j)
                    print(pwd)
                    pwdgenScreen.close()
                    event = pwdScreen.read()



