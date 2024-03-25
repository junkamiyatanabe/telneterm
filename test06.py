#!/usr/bin/python3

import telnetlib
import tkinter as tk
import threading

# Telnetに接続
tn = telnetlib.Telnet('192.168.0.10', 8500)

# GUIの設定
root = tk.Tk()
label = tk.Label(root)
label.pack()

# データ受信と表示の関数
def receive_data():
    global rdat
    while True:
        rdat = tn.read_until(b"\r\n").decode("utf-8")  # データを受信し、UTF-8にデコード
        label.config(text=rdat)  # データをラベルに表示
        root.update()  # GUIを更新

# データ受信のスレッドを開始
thread = threading.Thread(target=receive_data)
thread.daemon = True
thread.start()

# GUIを開始
root.mainloop()