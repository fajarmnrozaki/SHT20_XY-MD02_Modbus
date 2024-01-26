import minimalmodbus
import time

MODBUS_ADDRESS = 1
COM_PORT = '/dev/ttyS0'
BAUD_RATE = 9600
TIMEOUT = 1

READ_TEMPERATURE_CMD = 0x04
READ_HUMIDITY_CMD = 0x04

def read_temperature():
    temperature = instrument.read_register(0x0001, number_of_decimals=1, functioncode=READ_TEMPERATURE_CMD)
    return temperature

def read_humidity():
    humidity = instrument.read_register(0x0002, number_of_decimals=1, functioncode=READ_HUMIDITY_CMD)
    return humidity

if __name__ == "__main__":
    try:
        instrument = minimalmodbus.Instrument(COM_PORT, MODBUS_ADDRESS)
        instrument.serial.baudrate = BAUD_RATE
        instrument.serial.timeout = TIMEOUT
        instrument.serial.parity = minimalmodbus.serial.PARITY_NONE  # Adjust based on your device's requirements

        while True:
            temperature = read_temperature()
            humidity = read_humidity()

            print(f"Temperature: {temperature} °C, Humidity: {humidity} %")

            time.sleep(60)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

