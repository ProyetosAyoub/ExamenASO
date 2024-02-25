import psutil
import logging

# Configuración de logging
logging.basicConfig(filename='/home/alumno/logs/espacio.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Función para analizar el espacio disponible en la partición raíz
def analizar_espacio():
    espacio_usado_percent = psutil.disk_usage('/').percent
    if espacio_usado_percent > 80:
        logging.error("Espacio ocupado es mayor que 80%")
    elif espacio_usado_percent > 60:
        logging.warning("Espacio ocupado es mayor que 60% pero menor que 80%")
    else:
        logging.info("Espacio ocupado es menor que 60%")

if __name__ == "__main__":
    analizar_espacio()

