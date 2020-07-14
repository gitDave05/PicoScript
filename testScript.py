from PT104 import PT104, Channels, DataTypes, Wires
import socket
import time
from datetime import datetime

unit = PT104()
unit.connect('HS337/135')
unit.set_channel(Channels.CHANNEL_1, DataTypes.PT100, Wires.WIRES_4)
unit.set_channel(Channels.CHANNEL_2, DataTypes.PT100, Wires.WIRES_4)
unit.set_channel(Channels.CHANNEL_3, DataTypes.PT100, Wires.WIRES_4)

LaudaIP = '192.168.0.6'
LaudaPort = 54321
Buffer = 1001
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((LaudaIP, LaudaPort))
s.send('OUT_SP_01_8\r\n')
time.sleep(.300)
s.send('START\r\n')

"""First loop, running for 30 min to -20"""
s.send('OUT_SP_00_-20.00\r\n')
t_end = time.time()+60*30
while time.time() < t_end:
    bottom = unit.get_value_channel_1
    s.send(''.join(['OUT_PV_05_', str(bottom), '\r\n']))
    sens1 = unit.get_value_channel_2
    sens2 = unit.get_value_channel_3
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    f = open('record01.txt', 'w+')
    f.write(''.join([current_time, ', ', str(bottom), ', ', str(sens1), ', ', str(sens2),
                     ', ', '-20\r\n']))
    f.close()
    print(bottom)
    time.sleep(1)

"""Second loop, running for 10 min to -16"""
s.send('OUT_SP_00_-16.00\r\n')
t_end = time.time()+60*10
while time.time() < t_end:
    bottom = unit.get_value_channel_1
    s.send(''.join(['OUT_PV_05_', str(bottom), '\r\n']))
    sens1 = unit.get_value_channel_2
    sens2 = unit.get_value_channel_3
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    f = open('record01.txt', 'w+')
    f.write(''.join([current_time, ', ', str(bottom), ', ', str(sens1), ', ', str(sens2),
                     ', ', '-16\r\n']))
    f.close()
    print(bottom)
    time.sleep(1)

"""Third loop, running for 20 min to -25"""
s.send('OUT_SP_00_-25.00\r\n')
t_end = time.time()+60*20
while time.time() < t_end:
    bottom = unit.get_value_channel_1
    s.send(''.join(['OUT_PV_05_', str(bottom), '\r\n']))
    sens1 = unit.get_value_channel_2
    sens2 = unit.get_value_channel_3
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    f = open('record01.txt', 'w+')
    f.write(''.join([current_time, ', ', str(bottom), ', ', str(sens1), ', ', str(sens2),
                     ', ', '-25\r\n']))
    f.close()
    print(bottom)
    time.sleep(1)

s.send('STOP\r\n')
time.sleep(.300)
unit.disconnect()
time.sleep(.300)
s.close()