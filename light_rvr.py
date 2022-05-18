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
average_values = []
AVERAGE_COUNT = 10
smoothing_values = []
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
def return_heading(elem):
  return float(elem[2])
def return_light(elem):
  return float(elem[1])

rvr.sensor_start()



starting_time = time.monotonic()
time_elapsed = time.monotonic() - starting_time
rvr.update_sensors()

starting_heading = rvr.get_heading()
print(f'starting heading: {starting_heading}')

while time_elapsed < 3:
    rvr.update_sensors()
    time_elapsed = time.monotonic() - starting_time
    rvr.setMotors(-130, 130)

    heading = rvr.get_heading()

    light_data.append([time_elapsed, light_sensor.value, heading])

    time.sleep(0.02)
    print(light_data[-1])

    light_data.sort(key=return_heading)

    for row in light_data:
        row[1] = float(row[1])

    for row in light_data:
        line_count = 0
        if (line_count < AVERAGE_COUNT):
            smoothing_values.append(float(row[1]))
            average_values.append([float(row[2]),float(row[1])])
        else:
            #print(f'{type(smoothing_values)}, {type(row[1])}')
            averaged = float(sum(smoothing_values)) + float(row[1]) / float(len(smoothing_values)+1)
            average_values.append([row[2],averaged])

        smoothing_values.pop(0)
        smoothing_values.append(row[1])
        line_count += 1

rvr.setMotors(0, 0)

average_values.sort(key=return_light)
print(f'Value of {average_values[0][1]} at heading {average_values[0][0]}')

rvr.update_sensors()

tolerance = 4
smoothed_heading = rvr.get_heading()
smoothies = []
smoothies.append(rvr.get_heading())
smoothie_amount = 10
"""
while not (rvr.get_heading() < average_values[0][0]+tolerance and rvr.get_heading() > average_values[0][0]-tolerance)
"""
time_start = time.monotonic()

while not (smoothed_heading < average_values[0][0]+tolerance and smoothed_heading > average_values[0][0]-tolerance):
    rvr.update_sensors()
    current_heading = rvr.get_heading()
    print(f'{current_heading}')
    smoothed_heading = (float(sum(smoothies)) + current_heading) / float(len(smoothies)+1)
    print((float(sum(smoothies)) + current_heading) / float(len(smoothies)+1))
    
    print('length of smoothies: ' + str(len(smoothies)))
    print('difference: ' + str(smoothed_heading-average_values[0][0]))

    if len(smoothies)+1 > smoothie_amount:
        smoothies.pop(0)
    smoothies.append(rvr.get_heading())
    rvr.setMotors(-110, 110)
    time.sleep(0.01)
    rvr.update_sensors()

rvr.setMotors(0, 0)
time.sleep(1)
print('success')

time.sleep(1)
rvr.setMotors(130, 130)
#drive in direction of { average_values[0][0] }
time.sleep(4)

rvr.setMotors(0, 0)



rvr.stop()
