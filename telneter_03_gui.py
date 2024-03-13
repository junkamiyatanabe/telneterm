#!/usr/bin/python3

import PySimpleGUI as sg
import telnetlib

# コマンド送信の関数
def send_command(cmd):
    tn.write(cmd.encode("utf-8")) # cmdをUTF-8にエンコードして送信
    response = tn.read_some().decode("utf-8")  # 受信データもUTF-8にエンコード
    # window["-OUTPUT-"].update(cmd) # 送信データをTextに表示
    window["-INPUT-"].update(response) # 受信データをTextに表示

#　検査設定読み出しの関数
def send_pr():
    tn.write("PR\r\n".encode("utf-8"))
    response = tn.read_some().decode("utf-8") 
    window["-NNN-"].update(response[5:9]) # 検査設定Noだけスライスして表示
    window["-INPUT-"].update(response) # 受信データをTextに表示

HOST = "192.168.0.10"
PORT = 8500

numbers = [0, 1, 2, 3, 4, 5] 

# Window配置
layout = [
    [sg.Text("Setting")],
    [sg.Text("No.",size=(3,1),font=('Arial',20)),sg.Text(size=(3,1), key="-NNN-",font=('Arial',20))],
    [sg.Combo(numbers, default_value=0, key='-COMBO-'),sg.Button("Setting", key="set_btn"), sg.Button("reset", key="rs_btn",pad=((10,0),(0,0)))],
    [sg.Button("START", font=('Arial',20), key="trg_btn", pad=((0,10),(20,20)) ,size=(10,3))],
    [sg.Text("OUT>",size=(5,1),justification='right'),sg.Text(size=(20,1), key="-OUTPUT-")] ,
    [sg.Text(" IN>",size=(5,1),justification='right'),sg.Text(size=(20,1), key="-INPUT-")] ,
    [sg.Input(key='-SENDCOM-',size=(23,1), pad=((0,0),(20,0)))],
    [sg.Button('Command Send',key="Send")]
]

# ウィンドウを作成
window = sg.Window('TEST Running', layout)

# Telnet接続
tn = telnetlib.Telnet(HOST, PORT)

#最初だけ実行
tn.write("RUN\r\n".encode("utf-8"))
response = tn.read_some().decode("utf-8")
tn.write("PR\r\n".encode("utf-8"))
response = tn.read_some().decode("utf-8") 
event, values = window.read(timeout=100)
window["-NNN-"].update(response[5:9]) 
cmd = "Start"

# メインループ
while True:
    event, values = window.read()
    
    # 各イベント処理
    if event == sg.WIN_CLOSED:
        cmd ="SET\r\n"
        send_command(cmd)
        break

    if event == "trg_btn":
        cmd = "TRG\r\n"
        send_command(cmd)

    if event == "rs_btn":
        cmd = "RS\r\n"        
        send_command(cmd)

    if event == "set_btn":
        number = str(values['-COMBO-'])
        cmd = "PL,2," + number + "\r\n"        
        send_command(cmd)
        send_pr()

    if event == 'Send':
        input_value = values['-SENDCOM-']
        if input_value:
            cmd = values['-SENDCOM-'] + '\r\n' 
            send_command(cmd)
            window["-SENDCOM-"].update("")
        else:
            cmd = "Command is empty"

    window["-OUTPUT-"].update(cmd) # 送信データをTextに表示
    # window["-INPUT-"].update(response) # 受信データをTextに表示

window.close()
tn.close()
