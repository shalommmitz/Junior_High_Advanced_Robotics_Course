# Controlling the "E99 Pro" AKA "E99 K3" Drone from Python

This drone can be bought in AliExperss and many other locations for less than $20.
We document here how to control it from python - to be used in education.

## Install:
 
  - Install the virtual env.: `python3 -m venv venv`
  - Activate the venv: `. v`
  - Update pip: `pip install -u pip setuptools wheel`
  - Install packages: `pip install -r requirements.txt`

## Using:

  - Activate the venv:`. v`
  - Connect your PC/laptop to the access point presented by the drone
    It is called  "WIFI_4K_<some number>"
    You should get the IP: 192.168.4.100
  - Connect to the drone: `python3 1_connect.py`
 
    The drone should stop blinking

  - Take off: `python3 2_take_off.py`

    NOTE: need more work to land...

  - Take off/fly/land (untested): `python3 3_all_steps.py`
 
## Description of the reversing process:

 - https://medium.com/@amine.lemaizi/hacking-a-toy-drone-to-put-artificial-intelligence-on-it-part-1-the-hack-7454e42de376

 - https://dspace.ut.ee/server/api/core/bitstreams/22f3fe08-b3f2-4051-a2df-c83fcb621126/content

 - https://blog.horner.tj/hacking-chinese-drones-for-fun-and-no-profit/

## Relevant repositories

- https://github.com/Hermann-SW/wireless-control-Eachine-E52-drone?tab=readme-ov-file#capturing-wireless-traffic-between-android-ufo-app-and-e52-drone
- https://github.com/Artemish/e99_k3_controller/blob/master/drone_control_2.py
- https://github.com/dronekit/dronekit-python

## Credits

Source URL for "main_loop_not_working_1.py":
https://dspace.ut.ee/server/api/core/bitstreams/22f3fe08-b3f2-4051-a2df-c83fcb621126/content
The sw is near the end of the PDF

Drone controller.py:
https://github.com/abdalrahimnaser/dronelib_py/blob/main/DroneController.py

