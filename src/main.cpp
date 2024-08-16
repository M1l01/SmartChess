#include <stdio.h>
#include <freertos/FreeRTOS.h>
#include <freertos/task.h>
#include <freertos/queue.h>
#include <freertos/timers.h>
#include <driver/gpio.h>
#include <esp_types.h>
#include <esp_log.h>
#include "gpio_config.h"
#include <vector>
#include <string>

//Matriz de Detección - FILAS
constexpr gpio_num_t ROW1 = GPIO_NUM_4;
constexpr gpio_num_t ROW2 = GPIO_NUM_13;
constexpr gpio_num_t ROW3 = GPIO_NUM_14;
constexpr gpio_num_t ROW4 = GPIO_NUM_15;
constexpr gpio_num_t ROW5 = GPIO_NUM_16;
constexpr gpio_num_t ROW6 = GPIO_NUM_17;
constexpr gpio_num_t ROW7 = GPIO_NUM_18;
constexpr gpio_num_t ROW8 = GPIO_NUM_19;
//Vector de Filas
std::vector<gpio_num_t> ROWS = {ROW1, ROW2, ROW3, ROW4, ROW5, ROW6, ROW7, ROW8};

//Matriz de Detección - COLUMNAS
constexpr gpio_num_t COLa = GPIO_NUM_21;
constexpr gpio_num_t COLb = GPIO_NUM_22;
constexpr gpio_num_t COLc = GPIO_NUM_23;
constexpr gpio_num_t COLd = GPIO_NUM_25;
constexpr gpio_num_t COLe = GPIO_NUM_26;
constexpr gpio_num_t COLf = GPIO_NUM_27;
constexpr gpio_num_t COLg = GPIO_NUM_32;
constexpr gpio_num_t COLh = GPIO_NUM_33;
//Vector de Columnas
std::vector<gpio_num_t> COLS = {COLa, COLb, COLc, COLd, COLe, COLf, COLg, COLh};

//Variables para la interrupciones
TimerHandle_t timer_isr;
unsigned int interval = 500;   //tiempo de interrupción en milisegundos
int timerID = 1;

static const char* TAG = "Main";

bool in_out_state = true;   //Variable de cambio E/S

//Vector Lectura Filas
std::vector<uint8_t> lecRows(ROWS.size());
std::vector<uint8_t> lecCols(COLS.size());

//Matriz Deteccion
std::vector<std::vector<uint8_t>> matChess = {
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0}, 
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0}
};

//Prototipo de Funciones
void activacionSalidas(std::vector<gpio_num_t> Salidas);
void WMatrixChess(void);

//-----------------------------Interrupciones-----------------------------

//Función de Interrupción Lectura
void ISR_funcionLectura(TimerHandle_t timer){
    //Lectura de los Sensores
    if(in_out_state){
        //Lectura de Columnas
        lecCols[0] = gpio_get_level(COLa);
        lecCols[1] = gpio_get_level(COLb);
        lecCols[2] = gpio_get_level(COLc);
        lecCols[3] = gpio_get_level(COLd);
        lecCols[4] = gpio_get_level(COLe);
        lecCols[5] = gpio_get_level(COLf);
        lecCols[6] = gpio_get_level(COLg);
        lecCols[7] = gpio_get_level(COLh);
    }else{
        //Lectura de Filas
        lecRows[0] = gpio_get_level(ROW1);
        lecRows[1] = gpio_get_level(ROW2);
        lecRows[2] = gpio_get_level(ROW3);
        lecRows[3] = gpio_get_level(ROW4);
        lecRows[4] = gpio_get_level(ROW5);
        lecRows[5] = gpio_get_level(ROW6);
        lecRows[6] = gpio_get_level(ROW7);
        lecRows[7] = gpio_get_level(ROW8);
    }
    ESP_LOGI(TAG, "Datos Guardados");
}

//-----------------------------MAIN-----------------------------
extern "C" void app_main();

void app_main(){
    //Setup
    setupGPIOs(ROWS, COLS, in_out_state);
    ESP_LOGI(TAG, "GPIOS Inicializados");

    //Configuracion Timer
    ESP_LOGI(TAG, "Inicializacion de Timer");
    timer_isr = xTimerCreate("Timer",
                             pdMS_TO_TICKS(interval),
                             pdTRUE, //Auto reinicio del Timer,
                             (void*)timerID,
                             ISR_funcionLectura //Función de Callback de la interrupción
    );
    //MSG error de configuración
    if(timer_isr == NULL){
        ESP_LOGI(TAG, "Timer no fue creado");
    }else{
        if(xTimerStart(timer_isr, 0) != pdPASS){
            ESP_LOGI(TAG, "El timer no fue habilitado");
        }
    }

    //Bucle 
    while(1){
        if(in_out_state){
            //Detección de Columnas
            activacionSalidas(ROWS);
        }else{
            //Deteccion de Filas
            activacionSalidas(COLS);
        }
    }
}

//-----------------------------FUNCIONES-----------------------------
/*Funcion para activar Salidas*/
void activacionSalidas(std::vector<gpio_num_t> Salidas){
    for(size_t i=0; i<Salidas.size(); i++){
        gpio_set_level(Salidas[i], 1);
        gpio_set_level((i==0) ? Salidas[7] : Salidas[i-1], 0);
        
        vTaskDelay(pdMS_TO_TICKS(50));
    }
    gpio_set_level(Salidas[7], 0);
    in_out_state = !in_out_state;
    setupGPIOs(ROWS, COLS, in_out_state);
}

/*Funcion para escribir los datos en la Matriz de Detección*/
void WMatrixChess(){
    for(size_t i=0; i<8; i++){
        for(size_t j=0; j<8; j++){
            matChess[i][j] = (lecRows[i] == lecCols[j]) ? 1:0; 
        }
    }
}