import socket

destination_ip = '192.168.4.153'

COMMAND_PORT = 8090
START_COMMAND = b"\x42\x76"
END_COMMAND = b"\x42\x77"
DEFAULT_COMMAND = b"\x66\x80\x80\x80\x80\x00\x00\x99"
command_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
command_sock.sendto(DEFAULT_COMMAND, (destination_ip, COMMAND_PORT))
