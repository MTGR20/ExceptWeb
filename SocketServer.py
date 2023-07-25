### 성공!!
### SocketClient.Java와 통신

import socket
import toDB
import SttAndTts


soc = socket.socket()
host = "172.30.1.87" #IPv4 값 수정하고 실행하세요
port = 8000
soc.bind((host, port))
soc.listen(5)

while True:
    print("Ready to connect")
    conn, addr = soc.accept()
    print("Got connection from",addr)
    length_of_message = int.from_bytes(conn.recv(2), byteorder='big')
    msg = conn.recv(length_of_message).decode("UTF-8")
    print('받은 메세지: ' + msg)

    if "0" in msg:
        query_txt = SttAndTts.get_key()
        if query_txt == -1:
            print("fail to get key")
        else:
            print(query_txt)
            toDB.start(query_txt)
    else:
        toDB.start(msg)
        print("use key from input\n")

    message_to_send = SttAndTts.filename.encode("UTF-8")
    conn.send(len(message_to_send).to_bytes(2, byteorder='big'))
    conn.send(message_to_send)