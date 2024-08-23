#ifndef ROWS_CONTROL_H
#define ROWS_CONTROL_H

#include <vector>
#include <driver/gpio.h>

void activacionSalidas(std::vector<gpio_num_t> &ROWS, uint8_t &outRows);

#endif