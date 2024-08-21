#include <driver/gpio.h>
#include "gpio_config.h"
#include <vector>

void setupGPIOs(std::vector<gpio_num_t>& ROWS, std::vector<gpio_num_t>& COLS, bool SaveState){
    gpio_config_t config;
    if(SaveState){
        //Filas como Salidas
        for(size_t i = 0; i<ROWS.size(); i++){
            config.mode = GPIO_MODE_OUTPUT;
            config.pin_bit_mask = (1ULL << ROWS[i]);
            config.intr_type = GPIO_INTR_DISABLE;
            config.pull_down_en = GPIO_PULLDOWN_DISABLE;
            config.pull_up_en = GPIO_PULLUP_DISABLE;
            gpio_config(&config);
        }
        //Columnas como Entradas
        for(size_t j=0; j<COLS.size(); j++){
            config.mode = GPIO_MODE_INPUT;
            config.pin_bit_mask = (1ULL << COLS[j]);
            config.pull_down_en = GPIO_PULLDOWN_ENABLE;
            gpio_config(&config);
        }
    }else{
        //Columnas como Salidas
        for(size_t i = 0; i<COLS.size(); i++){
            config.mode = GPIO_MODE_OUTPUT;
            config.pin_bit_mask = (1ULL << COLS[i]);
            config.intr_type = GPIO_INTR_DISABLE;
            config.pull_down_en = GPIO_PULLDOWN_DISABLE;
            config.pull_up_en = GPIO_PULLUP_DISABLE;
            gpio_config(&config);
        }
        //Filas como Entradas
        for(size_t j=0; j<ROWS.size(); j++){
            config.mode = GPIO_MODE_INPUT;
            config.pin_bit_mask = (1ULL << ROWS[j]);
            config.pull_down_en = GPIO_PULLDOWN_ENABLE;
            gpio_config(&config);
        }
    }
}