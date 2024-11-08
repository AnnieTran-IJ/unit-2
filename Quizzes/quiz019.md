# Quiz 019
## Paper Code
![image](https://github.com/user-attachments/assets/adc94e42-4d89-4f0f-a10f-40e0882255df)

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
    print("|  x  |  y(x)  |")
    for i in range(n):
        print(f"|{x[i]:^6}|{y[i]:^8.2f}|")
        print("\n")

print(produce())
```
## Proof of work
![image](https://github.com/user-attachments/assets/f514f27a-e981-4e5f-a1c6-bce199f24765)

<img width="753" alt="Image_20241105_195157" src="https://github.com/user-attachments/assets/2f914c8d-4d2b-48cb-bb85-ebff2bc63c50">
