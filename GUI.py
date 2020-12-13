# importing required Modules
import GUI.sharedVariable as var
import GUI.loginScreen as login
import GUI.mainScreen as program

# starting while loop for the PySimpleGUI
# block contains a Logged In check
# Not Logged In --> Show Login screen
# Logged In --> Show Program Main Screen
while True:
    if not var.loggedin:
        login.start()
        if not var.loggedin:
            break
    elif var.loggedin:
        program.start()
        if var.loggedin:
            break
    else:
        break
