# Quiz 029

## Code
```.py
import requests
from matplotlib import pyplot as plt
import matplotlib
from my_lib import moving_average
import numpy as np

server_ip = "192.168.4.137"

#part a
request = requests.get(f"http://{server_ip}/readings") #register is a set of commands that the public can't access
readings = request.json()["readings"][0]

temp = []
pressure = []
for r in readings:
    if r["sensor_id"] == 11:
        temp.append(r["value"])
    if r["sensor_id"] == 12:
        pressure.append(r["value"])

new_temp = []
for i in pressure:
    new_temp.append(((i/1010)**5.25)*15)

average = []
for q in range(len(new_temp)):
    average.append((new_temp[q]+temp[q])/2)



plt.subplot(3,1,1)
plt.plot(temp, color ="blue", linewidth = 2)
plt.ylabel("Temperature")

plt.subplot(3,1,2)
plt.plot(new_temp, color ="blue", linewidth = 2)
plt.ylabel("Pressure")

plt.subplot(3,1,3)
plt.plot(average, color ="blue", linewidth = 2)
plt.ylabel("Average")
plt.show()
```
## Proof of work
![image](https://github.com/user-attachments/assets/7cce125d-97a8-4963-8bb9-b6f9a367f12c)
