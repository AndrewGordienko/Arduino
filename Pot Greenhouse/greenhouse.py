import serial
from datetime import datetime

temp = ""

L = 0  # Where we store values for light
MinLight = 0
MaxLight = 10

M = 0  # Where we store values for moisture
MinMoisture = 50

Hours = 0
RedFlag = False

Earliest = 10
Latest = 21

ser = serial.Serial('COM5', 115200, timeout=.1)

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    Hours = current_time[0:2]
    Hours = int(Hours)

    if RedFlag:
        if Hours > Earliest or Hours < Latest:
            ser.write(b'T')

    data = ser.readline()[:-2]
    print(data)
    if data:
        temp = (data[0:5])
        temp = (temp.decode('utf-8'))

        for i in range(len(temp)):
            if temp[i] == "L":  # Light
                L = temp[0:2]
                L = int(L)
                if L < MinLight or L > MaxLight:
                    RedFlag = True

            if temp[i] == "M":  # Moisture
                M = temp[0:2]
                M = int(M)
                if M < MinMoisture:
                    RedFlag = True




