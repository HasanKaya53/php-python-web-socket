import socket


HOST = '127.0.0.1'
PORT = 11060


soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    soc.bind((HOST, PORT))
except socket.error as message:
    print("Socket bind failed. Error  : " + message)

print(str(HOST)+":"+str(PORT)+" Socket bind complete")
soc.listen(9)

while 1:
    print("Socket Start")
    try:
        BUFF_SIZE = 4096    # 4 KiB
        conn, address = soc.accept()
        #unpacker = struct.Struct()
        data = conn.recv(BUFF_SIZE)
        print(data)
    except:
        print("Socket Accept Error")