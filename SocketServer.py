### 성공!!
### SocketClient.Java와 통신

import socket
import toDB
import SttAndTts

### 수정 ###
host = "172.30.1.84" #IPv4 값 수정하고 실행하세요
host = "127.0.0.1"  # BY YEWON
port = 8000
############

soc = socket.socket()
soc.bind((host, port))
soc.listen(5)

def send_msg(message_to_send) :
    try:
        message_to_send = message_to_send.encode("UTF-8")
        conn.send(len(message_to_send).to_bytes(2, byteorder='big'))
        conn.send(message_to_send)
    except ConnectionAbortedError:
        print("disconnect")
    except ConnectionResetError:
        print("disconnect")

while True:
    try:
        print("Ready to connect")
        conn, addr = soc.accept()
        print("Got connection from",addr)
        length_of_message = int.from_bytes(conn.recv(2), byteorder='big')
        msg = conn.recv(length_of_message).decode("UTF-8")
        print('받은 메세지: ' + msg)
    except ConnectionResetError:
        print("disconnect")

    if "0" in msg:
        query_txt = SttAndTts.get_key()
        if query_txt == -1:
            print("fail to get key")
            send_msg("fail to get key")
        else:
            print(query_txt)
            send_msg(query_txt)
            # toDB.start(query_txt)

            # send_msg(SttAndTts.dir_audio)
    else:
        toDB.start(msg)
        print("use key from input\n")

        send_msg(SttAndTts.dir_audio)

    # message_to_send = SttAndTts.dir_audio.encode("UTF-8")
    # conn.send(len(message_to_send).to_bytes(2, byteorder='big'))
    # conn.send(message_to_send)