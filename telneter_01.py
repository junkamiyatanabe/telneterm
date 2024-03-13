#!/usr/bin/python3

import telnetlib

HOST = "192.168.0.10"
PORT = 8500

tn = telnetlib.Telnet(HOST, PORT)

# コマンドをUTF-8でエンコード
cmd = "TRG\r\n".encode("utf-8") 

# コマンド送信
tn.write(cmd)

# 応答を取得
response = tn.read_some()

# 応答をUTF-8でデコード
print(response.decode("utf-8"))
