import socket
ip= "192.168.1.69"
puerto = 6969
objsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
objsocket.connect((ip, puerto))

print("MENSAJE DE ADVERTENCIA - CECIBER ")

while True:
    enviar="Dato recibido satifactoriamente"
    objsocket.send(enviar.encode(encoding="ascii", errors="ignore"))
    recibido=objsocket.recv(1024)
    print("CECIBER----> ", recibido.decode(encoding="ascii", errors="ignore"))
objsocket.close()



