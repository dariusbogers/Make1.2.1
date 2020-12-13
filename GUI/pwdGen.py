import random
import PySimpleGUI as pyGui
import GUI.sharedVariable as var
import clipboard

bitlength = [128, 256, 512]


# generates sequences of 8bits or 1Byte if these sequences match undesirable UTF-8 characters
# a new Sequence will be generated *note that this function is recursive meaning as long as
# the 8bit sequence is unwanted a new one will be generated over and over
def genbyte():
    temp = ""
    for y in range(8):
        i = round(random.random())
        temp = temp + str(i)

    while 0 <= int(temp, 2) <= 32:
        temp = genbyte()

    while 126 <= int(temp, 2):
        temp = genbyte()

    while int(temp, 2) == 94:
        temp = genbyte()

    while int(temp, 2) == 96:
        temp = genbyte()

    return temp


# the 8bit sequenses are encoded to their UTF-8 counterparts and joint together to form the password
def genpwd(bitL):
    pwd = ""
    byteL = int(bitL / 8)
    for x in range(byteL):
        pwd = pwd + chr(int(genbyte(), 2))
    return pwd


# generates the password generator main screen
def genwin():
    pwdgenlayout = [[pyGui.Text('select Bit length')],
                    [pyGui.Combo(bitlength, size=(8, 4), key=('-BitLength-'))],
                    [pyGui.Button('Generate')]]
    var.pwdgenscreen = pyGui.Window('Password Generator', pwdgenlayout)

    pwdlayout = [[pyGui.Text('Please note that this password is generated randomly to the bit and that it will never'
                             ' generate the same password twice, if you lose your password this generater will not '
                             'be able to regenerate it',size=(76, 4))],
                 [pyGui.InputText('', key=('-passGen-'),size=(76, 2), use_readonly_for_disable=True, disabled=True)]]
    var.pwdscreen = pyGui.Window('Generated Password', pwdlayout, size=(600, 300), element_justification='c')


# starts the password generator to ask for the requested bitlength of the password
def start():
    genwin()
    while True:
        var.event, var.values = var.pwdgenscreen.read()
        if var.event in [pyGui.WINDOW_CLOSED, 'Exit']:
            break
        elif var.event == 'Generate':
            passgen(var.values['-BitLength-'])

        break


# is the window needs to be closed from another file no current use
def close():
    var.pwdgenscreen.close()


# generates a random password and opens the screen to display it
def passgen(bitl):
    pwd = genpwd(bitl)
    var.pwdscreen.finalize()
    var.pwdscreen.FindElement('-passGen-').Update(value=pwd)
    var.pwdgenscreen.close()
    var.event = var.pwdscreen.read()
    if var.event == 'copy to clipboard':
        clipboard.copy(pwd)

