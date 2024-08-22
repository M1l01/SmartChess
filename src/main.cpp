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
unsigned int interval = 50;   //tiempo de interrupción en milisegundos
int timerID = 1;

static const char* TAG = "Main";

//Vector guardar las salidas
uint8_t outRows = 0;

//Vector de Detección de Entradas - Columnas
std::vector<uint8_t> DetColumns = {0,0,0,0,0,0,0,0}; //Detectará las columnas y almacenará en la matChess

//Matriz de Ajedrez para almacenar la detección
std::vector<std::vector<uint8_t>> matChess(8, std::vector<uint8_t>(8));

//Prototipo de Funciones
void activacionSalidas(std::vector<gpio_num_t> Salidas);
void deteccionColumnas(void);
void almacenarValores(void);
void imprimirVector(std::vector<uint8_t> vector);
void imprimirMatrix(std::vector<std::vector<uint8_t>> matriz);

//-----------------------------Interrupciones-----------------------------

//Función de Interrupción Lectura
void ISR_funcionLectura(TimerHandle_t timer){
    //ESP_LOGI(TAG, "Detección de Piezas");
    //llamamos a la funcion para lectura de columnas
    //ESP_LOGI(TAG, "Fila Activada: %u", outRows);
    deteccionColumnas();
    //imprimirVector(DetColumns);
    //llamamos a la función para almacenar valores
    almacenarValores();
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
        activacionSalidas(ROWS);
    }   
}

//-----------------------------FUNCIONES-----------------------------
/*Función para activar Salidas*/
void activacionSalidas(std::vector<gpio_num_t> Salidas){
    for(size_t i=0; i<Salidas.size(); i++){
        gpio_set_level(Salidas[i], 1);                          //Activación de la salida actual
        outRows = i;                                            //Guardamos la posición de la activación actual
        gpio_set_level((i==0) ? Salidas[7] : Salidas[i-1], 0);  //Desactivamos la salida anterior

        vTaskDelay(pdMS_TO_TICKS(150));
    }
    gpio_set_level(Salidas[7], 0);
}

/*Función para la detección de Columnas*/
void deteccionColumnas(void){
    //Agregamos cada lectura de la columna al vector
    for(size_t i=0; i<DetColumns.size(); i++){
        DetColumns[i] = gpio_get_level(COLS[i]);    //Lectura de los Sensores
    }
}

/*Función para almacenar las columnas leidas en la matríz*/
void almacenarValores(void){
    //Recorremos la matriz de almacenamiento
    //Mi variable para recorrer filas es outRows
    for(size_t c=0; c<matChess[0].size(); c++){ //Recorremos solo las columnas
        matChess[outRows][c] = DetColumns[c];
    }
}

/*Función para imprimir vectores*/
void imprimirVector(std::vector<uint8_t> vector){
    ESP_LOGI(TAG, "%u %u %u %u %u %u %u %u", vector[0], vector[1], vector[2],
             vector[3], vector[4], vector[5], vector[6], vector[7]);
}

/*Función para imprimir la matriz*/
void imprimirMatrix(std::vector<std::vector<uint8_t>> matriz){
    ESP_LOGI(TAG, "\n%u %u %u %u\n%u %u %u %u", 
                   matriz[0][0], matriz[0][1], matriz[0][2], matriz[0][3], 
                   matriz[1][0], matriz[1][1], matriz[1][2], matriz[1][3]
    );
}