import socket
destination_ip = '192.168.4.153'
#VIDEO_PORT = 8080
COMMAND_PORT = 8090
START_COMMAND = b"\x42\x76"
END_COMMAND = b"\x42\x77"
DEFAULT_COMMAND = b"\x66\x80\x80\x80\x80\x00\x00\x99"
#video_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
command_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#video_sock.sendto(START_COMMAND, (destination_ip, VIDEO_PORT))
command_sock.sendto(DEFAULT_COMMAND, (destination_ip, COMMAND_PORT))

def xor_checksum(data):
    checksum = 0
    for byte in data:
    checksum ^= byte
    return checksum

def get_controller():
    devices = [InputDevice(path) for path in list_devices()]
    for device in devices:
    if 'Wireless Controller' in device.name:
        return InputDevice(device.path)
    return None

print(f"Listening on {controller.path} - {controller.name}")
mapper = {'ABS_RX': 0, 'ABS_RY': 1, 'ABS_X': 3, 'ABS_Y': 2}
HEADER = b"\x66"

FOOTER = b"\x99"
command = [0x80, 0x80, 0x80, 0x80, 0x00]
try :
    for event in controller.read_loop():
        if event.type == ecodes.EV_ABS:
            abs_event = categorize(event)
            axis_name = ecodes.ABS[abs_event.event.code]
        if axis_name in mapper:
            command[mapper[axis_name]] = abs_event.event.value
            inverted_output = command.copy()
            inverted_output[mapper['ABS_Y']] = 255 -
            command[mapper['ABS_Y']]
            inverted_output[mapper['ABS_RY']] = 255 -
            command[mapper['ABS_RY']]
            hecksum = xor_checksum(inverted_output)
            command_bytes = HEADER + bytes(inverted_output) +
            bytes([checksum]) + FOOTER
            print(command_bytes.hex())
            command_sock.sendto(command_bytes, (destination_ip, COMMAND_PORT))
except KeyboardInterrupt:
    print("Exiting...")
finally:
    video_sock.sendto(END_COMMAND, (destination_ip, VIDEO_PORT))
    command_sock.close()
    video_sock.close()
    controller.close()
    print("Sockets closed. Exiting.")
