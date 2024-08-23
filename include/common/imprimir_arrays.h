#ifndef IMPRIMIR_ARRAYS_H
#define IMPRIMIR_ARRAYS_H

#include <esp_types.h>
#include <vector>

void imprimirVector(std::vector<uint8_t> &vector);
void imprimirMatrix(std::vector<std::vector<uint8_t>> &matriz);

#endif