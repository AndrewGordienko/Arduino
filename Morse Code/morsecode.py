import serial
import time

morsecode = {"a" : ".-", "b" : "-...", "c" : "-.-.", "d" : "-..", "e" : ".",
"f" : "..-.", "g" : "--.", "h" : "....", "i" : "..", "j" : ".---", "k" : "-.-",
"l" : ".-..", "m" : "--", "n" : "-.", "o" : "---", "p" : ".--.", "q" : "--.-",
"r" : ".-.", "s" : "...", "t" : "-", "u" : "..-", "v" : "...-", "w" : ".--",
"x" : "-..-", "y" : "-.--", "z" : "--.."}

ourstring  = "abc"
temp = ""

for i in range(len(ourstring)):
    for key, value in morsecode.items():
        if key == ourstring[i]:
            temp += value


for i in range(len(temp)):
    with serial.Serial('COM3', 9800, timeout=1) as ser:
        print (temp[i])
        if temp[i] == "-":
            ser.write(b'H')
            time.sleep(1)
        else:
            ser.write(b'H')
            time.sleep(2)