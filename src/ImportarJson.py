import json

class tratamientoJson:
    def __init__(self, nombrePieza = ""):
        self.ruta = "..//SmartChess//src//piezas.json"

        self.nombrePieza = nombrePieza

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

    def Almacenar_coordenada(self, casillaSelect):
        print(self.nombrePieza)
        piezasJson = self.import_datos()
        if self.nombrePieza in piezasJson:
            for clave, piezaParams in piezasJson.items():
                if clave != self.nombrePieza:
                    piezaParams["coordenada"].append(piezaParams["coordenada"][-1])
            piezasJson[self.nombrePieza]["coordenada"].append(casillaSelect)
            self.modificar_datos(piezasJson)
        else:
            print("No se encuentra esa pieza")

    def default_params(self):
        piezasJson = self.import_datos()
        for _, piezaParams in piezasJson.items():
            piezaParams["coordenada"] = [piezaParams["coordenada"][0]]
            piezaParams["estado"] = "vivo"

        self.modificar_datos(piezasJson)
            

if __name__ == "__main__":
    tratamientoJson().Almacenar_coordenada("A3")


        