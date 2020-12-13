# Python ToolBox by Darius
https://github.com/dariusbogers/Make1.2.1

<h1>Python ToolBox</h1>

<h2>GUI.py</h2>

    the main GUI file is used the have the first line of seqeunce flow of the status
    of the variable Logged in is false the user wil be taken to the login screen else
    the user will be taken to the main program

<h2>GUI/loginScreen.py</h2>

    this is the login screen where the user will give up credetnials these will be checked
    if they are correct the user will be logged in else an error will popup
    
    --note the login system is not yet complete at the moment it just compaires the the 
    --input to strings

<h2>GUI/mainScreen.py</h2>

    here you get an overview of the programs scripts 

<h2>GUI/IPScan.py</h2>

    this showes the IP adress of the current device as well as it runs a networkscan

<h2>GUI/pwdGen.py</h2>

    this generates a random password from 128bit, 256bit or 512bit
    the way it does the is it generates a sequence of 8bits at a time 
    say we got this sequence of bits --01101000 01100001 01101100 01101100 01101111--
    that would be translated to --104 97 108 108 111-- and that would translate to 'hallo'

<h2>GUI/SystemUpgrade.py</h2>

    this is a script to execute 'sudo apt-get update && sudo apt-get upgrade'
    your sudo password is asked in a graphical window and is passed through to the backlying script
    to execute the update

    --note there is no password check yet so make sure to enter the correct password


<h2>GUI.sharedVariable.py</h2>

    this file has a list of variables wich are being used globaly over the entire program

<h2>lib</h2>

    this folder contains downloaded`` modules
