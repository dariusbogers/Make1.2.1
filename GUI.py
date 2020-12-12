import PySimpleGUI as pyGui
import GUI.sharedVariable as var
import GUI.loginScreen as login
import GUI.mainScreen as program

bitlength = [128, 256, 512]

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

pwdgenLayout = [[pyGui.Text('select Bit length')],
                [pyGui.Combo(bitlength, size=(8, 4), key=('-BitLength-'))],
                [pyGui.Button('Generate')]]
pwdgenScreen = pyGui.Window('Password Generator', pwdgenLayout)

pwdLayout = [[pyGui.Text('', key=('-passGen-'),size=(66,1))]]
pwdScreen = pyGui.Window('Generated Password', pwdLayout, size=(600, 300),element_justification='c')

while True:
    if var.LoggedIn == False:
        login.start()
        if var.event == pyGui.WINDOW_CLOSED or var.event == 'Exit':
            break
        elif var.event == 'Login':
            login.login()
            if var.LoggedIn:
                login.close()

    if var.LoggedIn:
        program.start()
        if var.event == pyGui.WINDOW_CLOSED or var.event == 'Exit':
            break









#    event, values = LoginScreen.read()
#    if event == pyGui.WINDOW_CLOSED or event == 'Exit':
#        break
#    elif event == 'Login':
#        if values['-User-'] != 'Admin' or values['-Pwd-'] != '123456789':
#            print("User: " + values['-User-'] + "\nPassword: " + values['-Pwd-'])
#            loginerrorpopup.read()
#        else:
#            LoginScreen.close()
#            event, values = programWindow.read()

#            if event == 'Password Generator':
#                event, values = pwdgenScreen.read()
#                if event == 'Generate':
#                    print(values['-BitLength-'])
#                    j = values['-BitLength-']
#                    pwdScreen.finalize()
#                    pwd = pwdGen.genpwd(j)
#                    print(pwd)
#                    pwdScreen.FindElement('-passGen-').Update(value=pwd)
#                    pwdgenScreen.close()
#                    event = pwdScreen.read()



