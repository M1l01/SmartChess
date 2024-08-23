#include <stdio.h>
#include <freertos/FreeRTOS.h>
#include <freertos/task.h>
#include <freertos/queue.h>
#include <freertos/timers.h>
#include <driver/gpio.h>
#include <esp_types.h>
#include <esp_log.h>
#include "drivers/gpio_config.h"
#include "drivers/rows_control.h"
#include "common/imprimir_arrays.h"
#include "common/columns_detection.h"
#include <vector>
#include <string>

//Vector de Filas
std::vector<gpio_num_t> ROWS = {GPIO_NUM_4, GPIO_NUM_13, GPIO_NUM_14, GPIO_NUM_15,
                                GPIO_NUM_16, GPIO_NUM_17, GPIO_NUM_18, GPIO_NUM_19
};

//Vector de Columnas
std::vector<gpio_num_t> COLS = {GPIO_NUM_21, GPIO_NUM_22, GPIO_NUM_23, GPIO_NUM_25,
                                GPIO_NUM_26, GPIO_NUM_27, GPIO_NUM_32, GPIO_NUM_33
};

//Variables para la interrupciones
TimerHandle_t timer_isr;
unsigned int interval = 50;   //tiempo de interrupción en milisegundos
int timerID = 1;

static const char* TAG = "Main";

//Variable para guardar las salidas - Filas
uint8_t outRows = 0;

//Vector de Detección de Entradas - Columnas
std::vector<uint8_t> DetColumns = {0, 0, 0, 0, 0, 0, 0, 0}; //Detectará las columnas y almacenará en la matChess

//Matriz de Ajedrez para almacenar la detección
std::vector<std::vector<uint8_t>> matChess(8, std::vector<uint8_t>(8));

//-----------------------------Interrupciones-----------------------------

//Función de Interrupción Lectura
void ISR_funcionLectura(TimerHandle_t timer){
    //llamamos a la funcion para lectura de columnas
    deteccionColumnas(DetColumns, COLS);
    //llamamos a la función para almacenar valores
    almacenarValores(matChess, DetColumns, outRows);
    imprimirMatrix(matChess);
}

//-----------------------------MAIN-----------------------------
extern "C" void app_main();

void app_main(){
    //Setup
    setupGPIOs(ROWS, COLS);
    ESP_LOGI(TAG, "GPIOS Inicializados");

    //Configuración Timer
    ESP_LOGI(TAG, "Inicializacion de Timer");
    timer_isr = xTimerCreate("Timer",
                             pdMS_TO_TICKS(interval),
                             pdTRUE, //Auto reinicio del Timer,
                             (void*)timerID,
                             ISR_funcionLectura //Función de Callback de la interrupción
    );
    //MSG error de configuración
    if(timer_isr == NULL){
        ESP_LOGW(TAG, "Timer no fue creado");
    }else{
        if(xTimerStart(timer_isr, 0) != pdPASS){
            ESP_LOGW(TAG, "El timer no fue habilitado");
        }
    }

    //Bucle 
    while(1){
        //Activación de Filas
        activacionSalidas(ROWS, outRows);
    }   
}