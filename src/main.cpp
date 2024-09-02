#include <stdio.h>
#include <string.h>
#include <sys/param.h>
#include <freertos/FreeRTOS.h>
#include <freertos/task.h>
#include <freertos/timers.h>
#include <freertos/event_groups.h>
#include <driver/gpio.h>
#include "esp_system.h"
#include "esp_wifi.h"
#include "esp_event.h"
#include "esp_log.h"
#include "nvs_flash.h"
#include "lwip/sockets.h"
#include "lwip/netdb.h"
#include "esp_netif.h"
#include "drivers/gpio_config.h"
#include "drivers/rows_control.h"
#include "common/imprimir_arrays.h"
#include "common/columns_detection.h"
#include <vector>
#include <cstring>
#include <string>

#define WIFI_SSID "Netlife-ISABELLA"
#define WIFI_PASS "Isaval0102"
#define PORT 3333

#define CHUNK_SIZE 16 //Tamaño del paquete en bytes

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

static const char* TAGMain = "Main";
static const char* TAGServer = "TCP_Server";

//Variable para guardar las salidas - Filas
uint8_t outRows = 0;

//Vector de Detección de Entradas - Columnas
std::vector<uint8_t> DetColumns = {0, 0, 0, 0, 0, 0, 0, 0}; //Detectará las columnas y almacenará en la matChess

//Matriz de Ajedrez para almacenar la detección
std::vector<std::vector<uint8_t>> matChess(8, std::vector<uint8_t>(8));

// Prototipos de las Funciones
void activarFilasTask(void *pvParameters);
void wifi_init_sta(void);
void tcp_server_task(void *pvParameters);
void enviarDatosPaquetes(int sock, const uint8_t* datos, size_t tam);

//-----------------------------Interrupciones-----------------------------

//Función de Interrupción Lectura
void ISR_funcionLectura(TimerHandle_t timer){
    //llamamos a la funcion para lectura de columnas
    deteccionColumnas(DetColumns, COLS);
    //llamamos a la función para almacenar valores
    almacenarValores(matChess, DetColumns, outRows);
}

//-----------------------------MAIN-----------------------------
extern "C" void app_main();

void app_main(){
    //Setup
    setupGPIOs(ROWS, COLS);
    ESP_LOGI(TAGMain, "GPIOS Inicializados");

    //Configuración Timer
    ESP_LOGI(TAGMain, "Inicializacion de Timer");
    timer_isr = xTimerCreate("Timer",
                             pdMS_TO_TICKS(interval),
                             pdTRUE, //Auto reinicio del Timer,
                             (void*)timerID,
                             ISR_funcionLectura //Función de Callback de la interrupción
    );
    //MSG error de configuración
    if(timer_isr == NULL){
        ESP_LOGW(TAGMain, "Timer no fue creado");
    }else{
        if(xTimerStart(timer_isr, 0) != pdPASS){
            ESP_LOGW(TAGMain, "El timer no fue habilitado");
        }
    }

    nvs_flash_init();
    wifi_init_sta();
    
    //Tareas
    xTaskCreate(activarFilasTask, "activar_filas", 512, NULL, 5, NULL);
    xTaskCreate(tcp_server_task, "tcp_server", 4096, NULL, 5, NULL);
}

void activarFilasTask(void *pvParameters){
    //Bucle 
    while(1){
        //Activación de Filas
        activacionSalidas(ROWS, outRows);
    }   
}

//------------------------------Configuración del WIFI--------------------
static void event_handler(void *arg, esp_event_base_t event_base, int32_t event_id, void *event_data){
    if(event_base == WIFI_EVENT && event_id == WIFI_EVENT_STA_START){
        esp_wifi_connect();
    }else if(event_base == WIFI_EVENT && event_id == WIFI_EVENT_STA_DISCONNECTED){
        ESP_LOGI(TAGServer, "Conexión Fallida, reconectando ...");
        esp_wifi_connect();
    }else if(event_base == IP_EVENT && event_id == IP_EVENT_STA_GOT_IP){
        ip_event_got_ip_t *event = (ip_event_got_ip_t *)event_data;
        ESP_LOGI(TAGServer, "Conectado con éxito a la red");
        ESP_LOGI(TAGServer, "Dirección IP asignada: " IPSTR, IP2STR(&event->ip_info.ip));
    }
}

void wifi_init_sta(void) {
    esp_netif_init();
    esp_event_loop_create_default();
    esp_netif_create_default_wifi_sta();
    wifi_init_config_t cfg = WIFI_INIT_CONFIG_DEFAULT();
    esp_wifi_init(&cfg);

    //Registrar el manejador de Eventos
    esp_event_handler_instance_t instance_any_id;
    esp_event_handler_instance_t instance_got_ip;
    esp_event_handler_instance_register(WIFI_EVENT, ESP_EVENT_ANY_ID, &event_handler, NULL, &instance_any_id);
    esp_event_handler_instance_register(IP_EVENT, IP_EVENT_STA_GOT_IP, &event_handler, NULL, &instance_got_ip);

    esp_wifi_set_mode(WIFI_MODE_STA);
    wifi_config_t wifi_config = {
        .sta = {
            .ssid = WIFI_SSID,
            .password = WIFI_PASS,
        },
    };
    esp_wifi_set_config(WIFI_IF_STA, &wifi_config);
    esp_wifi_start();
    esp_wifi_connect();
}

void tcp_server_task(void *pvParameters) {
    char addr_str[128];
    int addr_family;
    int ip_protocol;

    struct sockaddr_in destAddr;
    destAddr.sin_addr.s_addr = htonl(INADDR_ANY);
    destAddr.sin_family = AF_INET;
    destAddr.sin_port = htons(PORT);
    addr_family = AF_INET;
    ip_protocol = IPPROTO_IP;
    inet_ntoa_r(destAddr.sin_addr, addr_str, sizeof(addr_str) - 1);

    int listen_sock = socket(addr_family, SOCK_STREAM, ip_protocol);
    if(listen_sock < 0){
        ESP_LOGE(TAGServer, "No se pudo crear el socket: errno %d", errno);
    }
    ESP_LOGI(TAGServer, "Socket Creado");

    bind(listen_sock, (struct sockaddr *)&destAddr, sizeof(destAddr));
    
    listen(listen_sock, 1);

    while (1) {
        struct sockaddr_in sourceAddr;
        socklen_t addrLen = sizeof(sourceAddr);
        int sock = accept(listen_sock, (struct sockaddr *)&sourceAddr, &addrLen);
        if(sock < 0){
            ESP_LOGE(TAGServer, "Error de accept: errno %d", errno);
            continue;
        }
        ESP_LOGI(TAGServer, "Cliente Conectado");

        char rx_buffer[128];
        while (1) {
            int len = recv(sock, rx_buffer, sizeof(rx_buffer) - 1, 0);
            if (len < 0) {
                ESP_LOGE(TAGServer, "Error de recepción: errno %d", errno);
                break;
            } else if (len == 0) {
                ESP_LOGI(TAGServer, "Conexión cerrada");
                break;
            } else {
                rx_buffer[len] = 0;
                ESP_LOGI(TAGServer, "Recibido: %s", rx_buffer);

                //Envío de la matriz de posiciones
                uint8_t paqueteDatos[64]; //Matriz de 8x8 a Array de 64 elementos
                int idx = 0;    //Indice de paquete de datos
                //Transformar Matriz a Array
                for(size_t i=0; i<matChess.size(); i++){
                    for(size_t j=0; j<matChess[0].size(); j++){
                        paqueteDatos[idx] = matChess[i][j];
                        idx++;
                    }
                }
                enviarDatosPaquetes(sock, paqueteDatos, sizeof(paqueteDatos));
                ESP_LOGI(TAGServer, "Datos Enviados");          
            }
        }
        shutdown(sock, 0);
        close(sock);
    }
}

void enviarDatosPaquetes(int sock, const uint8_t* datos, size_t tam){
    size_t sent = 0;
    while(sent < tam){
        size_t remaining = tam - sent;
        size_t toSend = (remaining > CHUNK_SIZE) ? CHUNK_SIZE : remaining;

        int result = send(sock, datos + sent, toSend, 0);
        if(result < 0){
            ESP_LOGE(TAGServer, "Error al enviar datos: %d", errno);
            break;
        }
        sent += result;
    }
}