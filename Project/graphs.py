from graph_lib import *
import requests
from matplotlib import pyplot as plt
import numpy as np

server_ip = "192.168.4.137"
data = {
    "temperature_DHT": [],
    "humidity_DHT": [],
    "temperature_BME": [],
    "humidity_BME": [],
    "pressure_BME": [],
    "time":[]
}

request = requests.get(f"http://{server_ip}/readings")
d = request.json()
readings = d['readings'][0]
count = 0

for entry in readings:
    # if count == 14425:
    #     break
    if entry['sensor_id'] == 432:
        data["temperature_DHT"].append(entry["value"])
        data["time"].append(entry["datetime"])
        count += 1
    elif entry['sensor_id'] == 433:
        data["humidity_DHT"].append(entry["value"])
        count += 1
    elif entry['sensor_id'] == 434:
        data["temperature_BME"].append(entry["value"])
        count += 1
    elif entry['sensor_id'] == 435:
        data["humidity_BME"].append(entry["value"])
        count += 1
    elif entry['sensor_id'] == 436:
        data["pressure_BME"].append(entry["value"])
        count += 1
        
data["temperature_DHT"] = data["temperature_DHT"][0:980]
data["humidity_DHT"] = data["humidity_DHT"][0:980]
data["temperature_BME"] = data["temperature_BME"][0:980]
data["humidity_BME"] = data["humidity_BME"][0:980]
data["pressure_BME"] = data["pressure_BME"][0:980]
data["time"] = data["time"][0:980]
#debugging
# print(len(data["time"]),len(data["temperature_DHT"]),len(data["humidity_DHT"]),len(data["temperature_BME"]),len(data["humidity_BME"]),len(data["pressure_BME"]))
# minimum_len = min(len(data["time"]),len(data["temperature_DHT"]),len(data["humidity_DHT"]),len(data["temperature_BME"]),len(data["humidity_BME"]),len(data["pressure_BME"]))
# print(minimum_len)

#graph properties
fig = plt.figure(figsize=(12, 6))
gs = fig.add_gridspec(3, 2)
x = []
for i in range(len(data["time"])):
    x.append(i)

#DHT graphs
#temp
g1 = fig.add_subplot(gs[0, 0])
xDT = data["time"]
yDT = data["temperature_DHT"]
yDT_smoothed = moving_average(50,yDT)
print(plot_data(g1,xDT,yDT,"Temperature"," (°C)"))
g1.plot(xDT[25:len(yDT_smoothed)+25],yDT_smoothed,color="#577c8e")

#hum

g2 = fig.add_subplot(gs[1, 0])
xDH= data["time"]
yDH = data["humidity_DHT"]
yDH_smoothed = moving_average(50,yDH)
print(plot_data(g2,xDH,yDH,"Humidity"," (%)"))
g2.plot(xDH[25:len(yDH_smoothed)+25],yDH_smoothed,color="#577c8e")

g3 = fig.add_subplot(gs[0, 1])
xBT= data["time"]
yBT = data["temperature_BME"]
yBT_smoothed = moving_average(50,yBT)
print(plot_data(g3,xBT,yBT,"Temperature"," (°C)"))
g3.plot(xBT[25:len(yBT_smoothed)+25],yBT_smoothed,color="#577c8e")

g4 = fig.add_subplot(gs[1, 1])
xBH= data["time"]
yBH = data["humidity_BME"]
yBH_smoothed = moving_average(50,yBH)
print(plot_data(g4,xBH,yBH,"Humidity"," (%)"))
g4.plot(xBH[25:len(yBH_smoothed)+25],yBH_smoothed,color="#577c8e")

g5 = fig.add_subplot(gs[2, 1])
xBP= data["time"]
yBP = data["pressure_BME"]
yBP_smoothed = moving_average(50,yBP)
print(plot_data(g5,xBP,yBP,"Pressure"," (hPa)"))
g5.plot(xBP[25:len(yBP_smoothed)+25],yBP_smoothed,color="#577c8e")

plt.show()


