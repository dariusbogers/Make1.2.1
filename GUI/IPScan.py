# importing required Modules
import lib.networkscan as networkscan
import socket
import PySimpleGUI as pyGui
import GUI.sharedVariable as var


# runs the network scan
def runscan():
    var.scan = networkscan.Networkscan('192.168.0.0/24')
    var.scan.run()


# get the IP if the current device this function is required 'cause socket.gethostbyaddr(socket.gethostname())
# returns the localhost IP --> 127.0.0.1
def getthisdevice():
    while True:
        for i in var.scan.list_of_hosts_found:
            try:
                if socket.gethostname() == socket.gethostbyaddr(i)[0]:
                    return i
                    break
            except:
                pass


# generates the window for the IP Scanner
def genwin():
    ips = var.scan.list_of_hosts_found
    iplayout = [[pyGui.Text('This Device:', font=('Arial', 10, 'bold'))],
                [pyGui.Text(getthisdevice(), size=(60, 2))],
                [pyGui.Text('Network Scan', font=('Arial', 10, 'bold'))]]

    iplayout2 = [[pyGui.Text(ip)] for ip in ips]

    iplayout += iplayout2
    iplayout += [[pyGui.Button('Exit')]]
    var.ipscreen = pyGui.Window("network Scanner", iplayout)


# starts the IP scanner immediately runs the Scanner
def start():
    runscan()
    genwin()
    while True:
        var.event, var.values = var.ipscreen.read()
        if var.event in [pyGui.WINDOW_CLOSED, 'Exit']:
            break


# is the window needs to be closed from another file no current use
def close():
    var.ipscreen.close()
