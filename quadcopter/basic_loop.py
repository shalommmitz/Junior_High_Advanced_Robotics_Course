import socket, codecs, time

HOST = "192.168.4.153"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((HOST, 8090))
cmd = '6680800080008099'

try:
    while True:
        s.send(codecs.decode(cmd, 'hex'))
        time.sleep(.05)
except:
    print("FAILED")
print("DONE")
s.close()
