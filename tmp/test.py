from mpython import *

p1=MPythonPin(1,PinMode.IN)
p1.write_digital(1)

wifi.connectWiFi()