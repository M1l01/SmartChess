#include "common/imprimir_arrays.h"
#include <esp_log.h>
#include <vector>

void imprimirVector(std::vector<uint8_t> &vector){
    ESP_LOGI("Vector Print", "%u %u %u %u %u %u %u %u", vector[0], vector[1], vector[2],
             vector[3], vector[4], vector[5], vector[6], vector[7]);
}

void imprimirMatrix(std::vector<std::vector<uint8_t>> &matriz){
    ESP_LOGI("Matrix Print", "\n%u %u %u %u\n%u %u %u %u", 
                   matriz[0][0], matriz[0][1], matriz[0][2], matriz[0][3], 
                   matriz[1][0], matriz[1][1], matriz[1][2], matriz[1][3]
    );
}