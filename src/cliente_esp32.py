import socket

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
    
    def recibir_msg(self, buffer_size=1024):
        #Recibe un mensaje del servidor
        if self.socket:
            try:
                data = self.socket.recv(buffer_size)
                if data:
                    print(f"Recibido: {data.decode()}")
                else:
                    print(f"No se ha recibido datos")
            except Exception as e:
                print(f"Error al recibir datos: {e}")
    def close(self):
        if self.socket:
            self.socket.close()
            print("Conexion cerrada")

class ESP32Comunication:
    def __init__(self, host, port):
        self.client = ESP32Client(host, port)
    
    def run(self):
        self.client.connect()
        message = "Hola mundo"
        self.client.send_msg(message)
        self.client.recibir_msg()
        self.client.close()

if __name__ == "__main__":
    host = "192.168.100.172"
    port = 3333
    app = ESP32Comunication(host, port)
    app.run()