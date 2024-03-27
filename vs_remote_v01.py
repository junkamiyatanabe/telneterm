#!/usr/bin/python3

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import telnetlib

# アイコンのデータ　============================================================
data =  '''
        R0lGODlhgACAAPcAAAAAAAAAMwAAZgAAmQAAzAAA/wArAAArMwArZgArmQArzAAr
        /wBVAABVMwBVZgBVmQBVzABV/wCAAACAMwCAZgCAmQCAzACA/wCqAACqMwCqZgCq
        mQCqzACq/wDVAADVMwDVZgDVmQDVzADV/wD/AAD/MwD/ZgD/mQD/zAD//zMAADMA
        MzMAZjMAmTMAzDMA/zMrADMrMzMrZjMrmTMrzDMr/zNVADNVMzNVZjNVmTNVzDNV
        /zOAADOAMzOAZjOAmTOAzDOA/zOqADOqMzOqZjOqmTOqzDOq/zPVADPVMzPVZjPV
        mTPVzDPV/zP/ADP/MzP/ZjP/mTP/zDP//2YAAGYAM2YAZmYAmWYAzGYA/2YrAGYr
        M2YrZmYrmWYrzGYr/2ZVAGZVM2ZVZmZVmWZVzGZV/2aAAGaAM2aAZmaAmWaAzGaA
        /2aqAGaqM2aqZmaqmWaqzGaq/2bVAGbVM2bVZmbVmWbVzGbV/2b/AGb/M2b/Zmb/
        mWb/zGb//5kAAJkAM5kAZpkAmZkAzJkA/5krAJkrM5krZpkrmZkrzJkr/5lVAJlV
        M5lVZplVmZlVzJlV/5mAAJmAM5mAZpmAmZmAzJmA/5mqAJmqM5mqZpmqmZmqzJmq
        /5nVAJnVM5nVZpnVmZnVzJnV/5n/AJn/M5n/Zpn/mZn/zJn//8wAAMwAM8wAZswA
        mcwAzMwA/8wrAMwrM8wrZswrmcwrzMwr/8xVAMxVM8xVZsxVmcxVzMxV/8yAAMyA
        M8yAZsyAmcyAzMyA/8yqAMyqM8yqZsyqmcyqzMyq/8zVAMzVM8zVZszVmczVzMzV
        /8z/AMz/M8z/Zsz/mcz/zMz///8AAP8AM/8AZv8Amf8AzP8A//8rAP8rM/8rZv8r
        mf8rzP8r//9VAP9VM/9VZv9Vmf9VzP9V//+AAP+AM/+AZv+Amf+AzP+A//+qAP+q
        M/+qZv+qmf+qzP+q///VAP/VM//VZv/Vmf/VzP/V////AP//M///Zv//mf//zP//
        /wAAAAAAAAAAAAAAACH5BAEAAPwALAAAAACAAIAAAAj/APcJHEiwoMGDCBMqXMiw
        ocOHECNKnEixosWLGDNq3Mixo8ePIEOKHEmypMmTKFOqXMmypcuXMGPKnEmzps2b
        OHPq3Mmzp8+fQIMKHUq0qNGjSJMqXcq0qVOBmcTEAEC1qtWrWLNq3cp1awwxmW4q
        E9O1rNmzaLOKgTYTTdq3cONiFQNy0o0YMW5MUqhsqty/gM/GULZxrNawBpUFXsyY
        K+GLxG50pUtQ2YrGmDNTtZjJb1k0BD1rHh144iS49QSSJc0aMGiHhuOChsY1RqbH
        PJV1dswwMuAY+1ZnRSw001bKCHcv3reVmFHFWg9CO/3W9uHDSI0Prywc7Q3nzNVm
        /wWeVHRVyr7fisEdHqt5qsSPar9q+33Z+APTsn/O2HbCtEwF9t1CAC7113oNFahU
        XHs9pGBSafkX0YNInTXgRBQeVRaCFWVoFFcNXuRhUdhpNCJR0W104lApmohWgFlx
        tKJQLWY0Y1A1YnQjUDmK+KKBMar444JBungWjFjJOCSERdq4ZIVN6vikhlH6eCSQ
        SQp5JZFZGmkWklcpuSWTXTo5JpRlSnkmlWla+SWWYWr5JpdxelkWmFaJOSeZdZq5
        J5p9qvknm4G6eSececp5KJ2J2tkVnlXpuSifjfo5KaCVCnopoZka+iiikSr6KaOh
        OsoVpJuJeiqoqZq6FaoA4GNn0Y4/cYXcrFN+ONl+E+ZKolk3yOoQrT5FKCyBvqII
        1yS8/pcsi3JxiOyauv51obNnNTsUdIFJeJBW9h1b3HjKpYVGagVp1V1V5CF12VwC
        pZeWtO1dNd9VIRZ1r1XxQbMusOCmRbeVtj4R8+pBaLyLlnUx/ltVvkDta9WtBpUL
        2D7cjsesT8pMYl9VbC0kb1zkudXayXBRrJC/cr22z8cox0zfRAm/la7MOGtFMEMW
        g1hQxjnnnNHIaiEEc9CaDbYRy9sl5DDSmbnckV14geXQ01ADJga6NUV1dNZd3WD1
        U2SXbfbZaKet9tpst+3223DHLffcdNdt991456333nz37fffgAcuuNwBAQA7
    '''

# コマンド送信の関数　============================================================
def send_command(cmd):
    if not connection_error_occurred:
        tn.write(cmd.encode("utf-8")) # cmdをUTF-8にエンコードして送信
        response = tn.read_some().decode("utf-8")  # 受信データもUTF-8にエンコード
        output_value.set(cmd) # 送信データをTextに表示
        input_value.set(response) # 受信データをTextに表示


# 検査設定読み出しの関数
def send_pr():
    if not connection_error_occurred:
        tn.write("PR\r\n".encode("utf-8"))
        response = tn.read_some().decode("utf-8")
        nnn_value.set("No. " + response[5:7]) # 検査設定Noだけスライスして表示
        input_value.set(response) # 受信データをTextに表示
        global nnn_num
        nnn_num = int(response[5:7])

def receive_data():
    global rdat
    if not connection_error_occurred:
        rdat = tn.read_until(b"\r\n").decode("utf-8")  # データを受信し、UTF-8にデコード
        # input_value.set(rdat) # 受信データをTextに表示
        rgb_classification(rdat)
        

def rgb_classification(rdat): 

    if nnn_num == 3:
        # RGB値を取得
        R, G, B = map(int, rdat.split(','))
        # 色相を判定
        if abs(R - G) < 30 and R > B and G > B:  # RとGがおおよそ同じような値で、B値より大きい場合を黄色系と判定
            Hcolor = 'YELLOW'
        elif R > G and R > B:
            Hcolor = 'RED'
        elif G > R and G > B:
            Hcolor = 'GREEN'
        elif B > R and B > G:
            Hcolor = 'BLUE'
        else:
            Hcolor = 'NG' # 上記のどれにも該当しない場合
        
        in_color_value.set(Hcolor)
   
        Lcolor = '#{:02x}{:02x}{:02x}'.format(R, G, B)
        input_color_a.config(bg=Lcolor)
    elif nnn_num == 10:
        # RGB値を取得
        H, S, V = map(int, rdat.split(','))
        # H値を判定
        if H > 0 and H < 35: 
            Hcolor = 'red'
        elif H >= 35 and H < 70: 
            Hcolor = 'yellow'
        elif H >= 70 and H < 120:
            Hcolor = 'green'
        elif H >= 120 and H < 210:
            Hcolor = 'blue'
        elif H >= 210 and H <= 256:
            Hcolor = 'red'
        else:
            Hcolor = 'error' # 上記のどれにも該当しない場合
        in_color_value.set(Hcolor)
        if Hcolor == "error":
            input_color_a.config(bg="white")
        else:
            input_color_a.config(bg=Hcolor)


# GUI作成　 ============================================================
root = tk.Tk()
root.title("VS Smart Camera Remote")
img = tk.PhotoImage(data=data) 
# root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(data=data))
root.iconphoto(False, img)

# StringVars
nnn_value = tk.StringVar()
output_value = tk.StringVar()
input_value = tk.StringVar()
sendcom_value = tk.StringVar()
cnt_value = tk.StringVar()

in_color_value =  tk.StringVar()
in_color_rgb =  tk.StringVar()

# main frame
frame = tk.Frame(root)
frame.grid(padx=20,pady=10)

# Setting frame
set_frame = tk.LabelFrame(frame, text='Setting', bd=2, relief=tk.RIDGE)
set_frame.grid(row=0, column=0, sticky="nsew")

nnn_label = tk.Label(set_frame, width=6, font=("Arial", 40),  textvariable=nnn_value)
nnn_label.grid(row=0, column=0, rowspan=2 ,sticky="nsew", padx=5, pady=5)
nnn_label_dummy= tk.Label(set_frame, text="").grid(row=0,column=1,columnspan=2)


numbers = list(range(100))
combo = ttk.Combobox(set_frame, values=numbers, width=3, justify='center')
combo.current(0)
combo.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
set_button = tk.Button(set_frame, text="SET", command=lambda: set_btn_clicked())
set_button.grid(row=1, column=2, sticky="nsew")

# Trigger frame
trg_frame = tk.LabelFrame(frame, text='Trigger', bd=2, relief=tk.RIDGE)
trg_frame.grid(row=1, column=0, sticky="nsew", pady=20)

start_button = tk.Button(trg_frame, text="START (s)", image=img, compound="top", command=lambda: start_btn_clicked(), width=300 )#,height=5)
start_button.grid(row=0, column=0, columnspan=3, padx=20, pady=10)

reset_button = tk.Button(trg_frame, text="Reset (r)", command=lambda: reset_btn_clicked())
reset_button.grid(row=1, column=2, sticky="nsew", padx=20, pady=10)

# color frame
clr_frame = tk.LabelFrame(frame, text='Color', bd=2, relief=tk.RIDGE)
clr_frame.grid(row=2, column=0, sticky="nsew", padx=10,pady=20)
input_color_a = tk.Label(clr_frame,font=("Arial", 30),text="       ")
input_color_a.grid(row=0, column=0, sticky="nsew", padx=10)
input_color_b = tk.Label(clr_frame, font=("Arial", 30),textvariable=in_color_value)
input_color_b.grid(row=0, column=1, sticky="nsew")
input_color_c = tk.Label(clr_frame, textvariable=in_color_rgb)
input_color_c.grid(row=0, column=2, sticky="nsew", padx=10)

# telnet接続エラーの場合アラートを出す（messagebox使用） ==============================
HOST = "192.168.0.10"
PORT = 8500
try:
    tn = telnetlib.Telnet(HOST, PORT)
except Exception as e:
    messagebox.showerror("Error", "接続が失敗しました。詳細：" + str(e))
    tn = None
    output_value.set("Telnet connection errors \r\n") 
    input_value.set("Telnet connection errors \r\n") 
    # フラグを立てておく（接続ＮＧ）
    connection_error_occurred = True
else:
    output_value.set("Send Command\r\n") 
    input_value.set("Recive Response\r\n") 
    # フラグを立てておく（接続ＯＫ）
    connection_error_occurred = False 


# 最初だけ実行　==============================
if not connection_error_occurred:
    # 運転モードへ
    tn.write("RUN\r\n".encode("utf-8"))
    response = tn.read_some().decode("utf-8")
    # 検査設定番号取得
    tn.write("PR\r\n".encode("utf-8")) 
    response = tn.read_some().decode("utf-8")
    nnn_value.set("No. " + response[5:7])
    nnn_num = int(response[5:7])

# イベント処理の関数　==============================
# 検査設定
def set_btn_clicked():
    number = str(combo.get())
    cmd = "PL,2," + number + "\r\n"        
    send_command(cmd)
    send_pr()
# リセット
def reset_btn_clicked():
    cmd = "RS\r\n"        
    send_command(cmd)
# トリガー
def start_btn_clicked():
    cmd = "TRG\r\n"
    send_command(cmd)
    receive_data()

# bind処理 ============================================================
def key_pressed(event):
    if event.char == 's':
        start_btn_clicked()
    if event.char == 'r':
        reset_btn_clicked()
    if event.char == '+':
        count_up()
    if event.char == '-':
        count_down()
    if event.char == '0':
        count_rst()
# キー入力イベントをバインド
root.bind("<Key>", key_pressed)

# 終了処理　============================================================
root.protocol("WM_DELETE_WINDOW", lambda: on_closing())

def on_closing():
    root.quit()
    if not connection_error_occurred:
        # 設定モードに戻す
        cmd ="SET\r\n" 
        send_command(cmd)
        tn.close()
# ============================================================
root.mainloop()


