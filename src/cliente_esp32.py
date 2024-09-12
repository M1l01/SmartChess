import socket
import struct
import math

class ESP32Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = None
    
    def connect(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.host, self.port))
            print(f"Conectado a la ESP32 en {self.host}:{self.port}")
        except Exception as e:
            print(f"Error al conectar con la ESP32: {e}")

    def send_msg(self, msg):
        #Envia un mensaje al servidor ESP32
        if self.socket:
            try:
                self.socket.sendall(msg.encode("utf-8"))
                print(f"Enviado: {msg}")
            except Exception as e:
                print(f"Error al enviar datos: {e}")
    
    def recibir_msg(self, buffer_size=16, total_size = 64):
        #Recibe un mensaje del servidor
        if self.socket:
            try:
                data = b""
                while len(data) < total_size:
                    paqueteDatos = self.socket.recv(buffer_size)
                    if not paqueteDatos:
                        print("No se han recibido datos")
                        return
                    data += paqueteDatos

                if len(data) == total_size:
                    try:
                        array = struct.unpack('64B', data)
                        array = list(array)
                        matChess = []
                        contador = 0
                        for i in range(0, int(math.sqrt(len(array)))): #Len array -> 64
                            matChess.append([]) #Agregamos una lista vacía
                            for j in range(0, int(math.sqrt(len(array)))):
                                matChess[i].append(array[contador])
                                contador+=1
                        return matChess

                    except struct.error as se:
                        print(f"Error al desempaquetar los datos {se}")
                        return None
                else:
                    print(f"Datos recibidos incompletos se esperaban {buffer_size} bytes")
                    return None
                
            except Exception as e:
                print(f"Error al recibir datos: {e}")
                return None

    def close(self):
        if self.socket:
            self.socket.close()
            print("Conexion cerrada")

if __name__ == "__main__":
    host = "ip_ep32"
    port = "puerto"
    app = ESP32Client(host, port)
    while(1):
        app.connect()
        message = "Hola mundo"
        app.send_msg(message)
        msgRecibido = app.recibir_msg()
        print(msgRecibido)
        app.close()
    