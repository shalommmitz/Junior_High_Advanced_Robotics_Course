import time
from DroneController import Drone

def wait_sec(seconds):
    for i in range(seconds*20): time.sleep(0.05)


drone = Drone()

drone.connect()

#wait(5)

drone.calibrate()

#wait(5)
drone.unlock_motor()
#wait(5)
drone.take_off(0.1)
drone.land(10)

drone.disconnect()  

