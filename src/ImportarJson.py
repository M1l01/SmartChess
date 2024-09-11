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

    def Almacenar_coordenada(self):
        piezasJson = self.import_datos()
        if self.nombrePieza in piezasJson:
            print("si esta")
        else:
            print("no esta")

    def default_params(self):
        piezasJson = self.import_datos()
        for _, piezaParams in piezasJson.items():
            piezaParams["coordenada"] = [piezaParams["coordenada"][0]]
            piezaParams["estado"] = "vivo"
            piezaParams["move"] = False

        self.modificar_datos(piezasJson)
            

if __name__ == "__main__":
    ImportarJson().Almacenar_coordenada()


        