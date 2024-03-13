#!/usr/bin/python3

import tkinter as tk
from tkinter import ttk
import telnetlib

# コマンド送信の関数
def send_command(cmd):
    tn.write(cmd.encode("utf-8")) # cmdをUTF-8にエンコードして送信
    response = tn.read_some().decode("utf-8")  # 受信データもUTF-8にエンコード
    output_value.set(cmd) # 送信データをTextに表示
    input_value.set(response) # 受信データをTextに表示

# 検査設定読み出しの関数
def send_pr():
    tn.write("PR\r\n".encode("utf-8"))
    response = tn.read_some().decode("utf-8")
    nnn_value.set("\r\nNo. " + response[5:9]) # 検査設定Noだけスライスして表示
    input_value.set(response) # 受信データをTextに表示

HOST = "192.168.0.10"
PORT = 8500

numbers = [0, 1, 2, 3, 4, 5]

root = tk.Tk()
root.title("VS Remote")

# StringVars
nnn_value = tk.StringVar()
output_value = tk.StringVar()
input_value = tk.StringVar()
sendcom_value = tk.StringVar()

# レイアウト
nnn_label = tk.Label(root, textvariable=nnn_value)
nnn_label.grid(row=0, column=1, sticky="nsew")

combo = ttk.Combobox(root, values=numbers, width=3, justify='center')
combo.current(0)
combo.grid(row=1, column=1, sticky="nsew")
set_button = tk.Button(root, text="Setting", command=lambda: set_btn_clicked())
set_button.grid(row=1, column=2, sticky="nsew")

start_button = tk.Button(root, text="START", command=lambda: start_btn_clicked(),height=5)
start_button.grid(row=2, column=0, columnspan=3, sticky="nsew", pady=10)

reset_button = tk.Button(root, text="Reset", command=lambda: reset_btn_clicked())
reset_button.grid(row=3, column=2, sticky="nsew")

label_dummy = tk.Label(root,text="- - - - - - - - - - - - - -", height=2)
label_dummy.grid(row=4, column=0, pady=10,columnspan=3)

output_label = tk.Label(root, text="COM>\r\n")
output_label.grid(row=5, column=0, sticky="nsew")
output_text = tk.Label(root, textvariable=output_value, anchor='w', justify='left')
output_text.grid(row=5, column=1, columnspan=2, sticky="nsew")

input_label = tk.Label(root, text="RES>\r\n")
input_label.grid(row=6, column=0, sticky="nsew")
input_text = tk.Label(root, textvariable=input_value, anchor='w', justify='left')
input_text.grid(row=6, column=1, columnspan=2, sticky="nsew")

sendcom_entry = tk.Entry(root, textvariable=sendcom_value)
sendcom_entry.grid(row=7, column=0, columnspan=3, sticky="nsew")
send_button = tk.Button(root, text="Command", command=lambda: send_btn_clicked())
send_button.grid(row=8, column=2, sticky="nsew")

root.grid_columnconfigure(0, weight=1, minsize=100)
root.grid_columnconfigure(1, weight=1, minsize=100)
root.grid_columnconfigure(2, weight=1, minsize=100)
root.grid_rowconfigure(0,weight=1)
root.grid_rowconfigure(1,weight=1)
root.grid_rowconfigure(2,weight=1)
root.grid_rowconfigure(3,weight=1)
root.grid_rowconfigure(5,weight=1)
root.grid_rowconfigure(6,weight=1)
root.grid_rowconfigure(7,weight=1)
root.grid_rowconfigure(8,weight=1)

tn = telnetlib.Telnet(HOST, PORT)

# 最初だけ実行
tn.write("RUN\r\n".encode("utf-8"))
response = tn.read_some().decode("utf-8")
tn.write("PR\r\n".encode("utf-8"))
response = tn.read_some().decode("utf-8")
nnn_value.set("\r\nNo. " + response[5:9])

output_value.set("Send Command\r\n") 
input_value.set("Recive Response\r\n") 


def set_btn_clicked():
    number = str(combo.get())
    cmd = "PL,2," + number + "\r\n"        
    send_command(cmd)
    send_pr()

def reset_btn_clicked():
    cmd = "RS\r\n"        
    send_command(cmd)

def start_btn_clicked():
    cmd = "TRG\r\n"
    send_command(cmd)

def send_btn_clicked():
    input_value = sendcom_value.get()
    if input_value:
        cmd = input_value + '\r\n' 
        send_command(cmd)
        sendcom_value.set("")
    else:
        cmd = "Command is empty\r\n"
    output_value.set(cmd) # 送信データをTextに表示

root.protocol("WM_DELETE_WINDOW", lambda: on_closing())
def on_closing():
    cmd ="SET\r\n"
    send_command(cmd)
    root.quit()
    tn.close()

root.mainloop()
