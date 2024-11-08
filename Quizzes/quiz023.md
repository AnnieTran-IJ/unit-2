# Quiz 023

## Paper Solution

## Code
```.py
import random

from matplotlib import pyplot as plt
import matplotlib
import numpy as np

# Relative humidity data
h = [57.0, 56.0, 57.0, 56.0, 55.0, 55.0, 54.0, 54.0, 54.0, 53.0,
     53.0, 54.0, 53.0, 53.0, 52.0, 52.0, 51.0, 51.0, 51.0, 50.0,
     50.0, 49.0, 50.0, 49.0, 49.0, 48.0, 49.0, 49.0, 48.0, 48.0,
     48.0, 49.0]
x = []

for i in range(32):
    x.append(i)

plt.style.use('ggplot')
plt.scatter(x, h, label='Measured Humidity')


m, b = np.polyfit(x, h, 1)
def model (x,m,b):
    H_model = m*x+b
    return H_model
x_model = [min(x), max(x)]
y_model = [model(min(x),m,b), model(max(x),m,b)]

print(f"h = {m:.02f}, b = {b:02f}")
# Plot the linear model
plt.plot(x_model, y_model)

# Add labels and title
plt.xlabel('Time (10-minute intervals)')
plt.ylabel('Relative Humidity (%)')
plt.title("Relative Humidity Over Time with Linear Model")

plt.show()
```
## Proof of work
![image](https://github.com/user-attachments/assets/de0d13e9-3644-4d22-a09b-bed192000bfe)

![Image_20241105_204037_116](https://github.com/user-attachments/assets/5ff890b5-cb61-4b31-8bdd-d640696969ec)
