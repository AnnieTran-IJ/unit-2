# Quiz 020

## Code
```.py
import random

from matplotlib import pyplot as plt
import matplotlib

random.seed(1234)

def produce(n=5,m=3,s=2): #default parameters:input
    x,y = [],[]
    for _ in range(n):
        r = random.randint(0,100)
        x.append(r)
        e = r ** (0.5 * (m/s) ** 2)
        y.append(e)
    return x,y

ax, ay = produce(n=10)
plt.plot(ax,ay) #'or' marker is a circle, color red, no line
plt.show()
```
## Proof of work
![image](https://github.com/user-attachments/assets/e8bb6796-319c-4ae0-a606-d68328cecf79)

<img width="733" alt="Image_20241105_195512" src="https://github.com/user-attachments/assets/fa98256d-1595-43a5-a748-1f3af379b3d4">
