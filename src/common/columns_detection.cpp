#include <driver/gpio.h>
#include <esp_types.h>
#include <vector>

/*Función para la detección de Columnas*/
void deteccionColumnas(std::vector<uint8_t> &DetColumns, std::vector<gpio_num_t> &COLS){
    //Agregamos cada lectura de la columna al vector
    for(size_t i=0; i<DetColumns.size(); i++){
        DetColumns[i] = gpio_get_level(COLS[i]);    //Lectura de los Sensores
    }
}

/*Función para almacenar las columnas leidas en la matríz*/
void almacenarValores(std::vector<std::vector<uint8_t>> &matChess, std::vector<uint8_t> &DetColumns, uint8_t &outRows){
    //Recorremos la matriz de almacenamiento
    //Mi variable para recorrer filas es outRows
    for(size_t c=0; c<matChess[0].size(); c++){ //Recorremos solo las columnas
        matChess[outRows][c] = DetColumns[c];
    }
}
