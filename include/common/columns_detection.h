#ifndef COLUMNS_DETECTION_H
#define COLUMNS_DETECTION_H

#include <driver/gpio.h>
#include <esp_types.h>
#include <vector>

void deteccionColumnas(std::vector<uint8_t> &DetColumns, std::vector<gpio_num_t> &COLS);
void almacenarValores(std::vector<std::vector<uint8_t>> &matChess, std::vector<uint8_t> &DetColumns, uint8_t &outRows);

#endif