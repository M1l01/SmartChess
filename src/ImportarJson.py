import json

class ImportarJson:
    def __init__(self, nombrePieza = "", paramPieza = "", ListaClaves = []):
        self.ruta = "..//SmartChess//src//piezas.json"

        self.nombrePieza = nombrePieza
        self.paramPieza = paramPieza

        self.ListaClaves = ListaClaves

    def import_datos(self):
        try:
            with open(self.ruta, 'r') as archivo:
                piezas = json.load(archivo)
            return piezas
        except FileNotFoundError:
            return {"Pieza": []}
        
    def modificar_datos(self, piezas):
        try:
            with open(self.ruta, 'w') as archivo:
                json.dump(piezas, archivo, indent=4)
        except Exception as e:
            print(f"Error al guardar los datos: {e}")



        