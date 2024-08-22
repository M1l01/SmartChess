#ifndef GPIO_CONFIG_H
#define GPIO_CONFIG_H

#include <driver/gpio.h>
#include <vector>

void setupGPIOs(std::vector<gpio_num_t>& ROWS, std::vector<gpio_num_t>& COLS);

#endif
