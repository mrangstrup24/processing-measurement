# sonar example 2022-02-21
import board, busio, time, math, digitalio, adafruit_hcsr04
from ssis_rvr import pin
from sphero_rvr import RVRDrive
from analogio import AnalogIn
import time


rvr = RVRDrive(uart=busio.UART(pin.TX, pin.RX, baudrate=115200))
# light_sensor = adafruit_hcsr04.HCSR04(trigger_pin=pin.TRIGGER, echo_pin=pin.ECHO)
light_sensor = AnalogIn(board.GP26)

light_data = []
#rvr.reset_yaw()

time.sleep(0.5)

rvr.set_all_leds(255, 0, 0)  # set leds to red
time.sleep(0.1)
rvr.set_all_leds(0, 255, 0)  # set leds to green
time.sleep(0.1)
rvr.set_all_leds(0, 0, 255)  # set leds to blue
time.sleep(0.1)  # turn off
rvr.set_all_leds(255, 255, 255)  # turn off leds or make them all black

print("works")

rvr.sensor_start()



starting_time = time.monotonic()
time_elapsed = time.monotonic() - starting_time
rvr.update_sensors()

starting_heading = rvr.get_heading()
print(f'starting heading: {starting_heading}')

while time_elapsed < 3:
    rvr.update_sensors()
    time_elapsed = time.monotonic() - starting_time
    rvr.setMotors(80, -80)
    
    heading = rvr.get_heading()
    
    light_data.append([time_elapsed, light_sensor.value, heading])
    
    time.sleep(0.1)
    print(light_data[-1])
rvr.update_sensors()


    




rvr.stop()
