#include "drivers/rows_control.h"
#include <freertos/FreeRTOS.h>
#include <freertos/task.h>
#include <driver/gpio.h>

void activacionSalidas(std::vector<gpio_num_t> &ROWS ,uint8_t &outRows){
    for(size_t i=0; i<ROWS.size(); i++){
        gpio_set_level(ROWS[i], 1);                          //Activación de la salida actual
        outRows = i;                                         //Guardamos la posición de la activación actual
        gpio_set_level((i==0) ? ROWS[7] : ROWS[i-1], 0);     //Desactivamos la salida anterior

        vTaskDelay(pdMS_TO_TICKS(150));
    }
    gpio_set_level(ROWS[7], 0);
}

