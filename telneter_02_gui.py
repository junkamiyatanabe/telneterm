#!/usr/bin/python3

import PySimpleGUI as sg
import telnetlib

HOST = "192.168.0.10"
PORT = 8500

layout = [
    [sg.Button("Send TRG Command")],
    [sg.Text(size=(40,5), key="-OUTPUT-")] 
]

window = sg.Window('Telnet Test', layout)

tn = telnetlib.Telnet(HOST, PORT)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "Send TRG Command":
        cmd = "TRG\r\n".encode("utf-8")
        tn.write(cmd) 
        response = tn.read_some().decode("utf-8")
        window["-OUTPUT-"].update(response) 

window.close()
tn.close()
