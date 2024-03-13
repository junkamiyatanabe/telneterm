#!/usr/bin/python3

import PySimpleGUI as sg
import telnetlib

# コマンド送信の関数
def send_command(cmd):
    tn.write(cmd.encode("utf-8")) # cmdをUTF-8にエンコードして送信
    response = tn.read_some().decode("utf-8")  # 受信データもUTF-8にエンコード
    window["-OUTPUT-"].update(response) # 受信データをTextに表示

#　検査設定読み出しの関数
def send_pr():
    tn.write("PR\r\n".encode("utf-8"))
    setnum = tn.read_some().decode("utf-8") 
    window["-NNN-"].update(setnum[5:9]) # 検査設定Noだけスライスして表示



HOST = "192.168.0.10"
PORT = 8500

# Window配置
layout = [
    [sg.Text("Setting No.",size=(10,1),font=('Arial',20)),sg.Text(size=(10,1), key="-NNN-",font=('Arial',20))],
    [sg.Button("000", key="000_btn"), sg.Button("001", key="001_btn")],
    [sg.Button("TRG", key="trg_btn"), sg.Button("RS", key="rs_btn")],
    [sg.Text(size=(40,5), key="-OUTPUT-")] ,
    [sg.Input(key='-INPUT-')],
    [sg.Button('Send')]
]

# ウィンドウを作成
window = sg.Window('TEST Running', layout)

# Telnet接続
tn = telnetlib.Telnet(HOST, PORT)

#最初だけ実行
tn.write("RUN\r\n".encode("utf-8"))
tn.write("PR\r\n".encode("utf-8"))
setnum = tn.read_some().decode("utf-8") 

# メインループ
while True:
    event, values = window.read()
    window["-NNN-"].update(setnum[5:9]) 

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

    if event == "000_btn":
        cmd = "PL,2,000\r\n"        
        send_command(cmd)
        send_pr()

    if event == "001_btn":
        cmd = "PL,2,001\r\n"        
        send_command(cmd)
        send_pr()

    if event == 'Send':
        cmd = values['-INPUT-'] + '\r\n' 
        send_command(cmd)
        window["-INPUT-"].update("")

window.close()
tn.close()
