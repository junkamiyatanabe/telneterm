import telnetlib
import tkinter as tk
import threading

# Telnetに接続
tn = telnetlib.Telnet('192.168.0.10', 8500)

# GUIの設定
root = tk.Tk()
label = tk.Label(root)
label.pack()
entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text='送信', command=lambda: send_command(entry.get()))
button.pack()

# データ受信と表示の関数
def receive_data():
    global rdat
    while True:
        rdat = tn.read_until(b"\r\n").decode("utf-8")  # データを受信し、UTF-8にデコード
        label.config(text=rdat)  # データをラベルに表示
        root.update()  # GUIを更新

# コマンド送信の関数
def send_command(sdat):
    tn.write((sdat + '\r\n').encode('utf-8'))  # コマンドをエンコードし、送信

# データ受信のスレッドを開始
thread = threading.Thread(target=receive_data)
thread.daemon = True
thread.start()

# GUIを開始
root.mainloop()
