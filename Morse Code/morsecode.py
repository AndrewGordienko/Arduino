import serial
import time

morsecode = {"a" : ".-", "b" : "-...", "c" : "-.-.", "d" : "-..", "e" : ".",
"f" : "..-.", "g" : "--.", "h" : "....", "i" : "..", "j" : ".---", "k" : "-.-",
"l" : ".-..", "m" : "--", "n" : "-.", "o" : "---", "p" : ".--.", "q" : "--.-",
"r" : ".-.", "s" : "...", "t" : "-", "u" : "..-", "v" : "...-", "w" : ".--",
"x" : "-..-", "y" : "-.--", "z" : "--.."}

ourstring  = ""  # any string that the user wants
temp = ""  # leave blank

for i in range(len(ourstring)):
    for key, value in morsecode.items():
        if key == ourstring[i]:
            temp += value


for i in range(len(temp)):
    with serial.Serial('COM3', 9800, timeout=1) as ser:  # change COM3 depending on the port your arduino is plugged into
        print (temp[i])
        if temp[i] == "-":
            ser.write(b'H')
            time.sleep(2)
            ser.write(b'L')

        else:
            ser.write(b'H')
            time.sleep(1)
            ser.write(b'L')
