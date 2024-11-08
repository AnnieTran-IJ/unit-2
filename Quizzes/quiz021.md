# Quiz 021

## Code
```.py
import random

from matplotlib import pyplot as plt
import matplotlib

plt.style.use('ggplot') #

start = -10
step = 0.01
x,y = [],[]

for i in range(int(20/step)): #20 is from -10 to 10
    x.append(start + step*i)
    y.append(2*(x[-1]+5)**2)

line_x = [-5, -5]
line_y = [0, 2*(15)**2]

plt.plot(line_x, line_y, color = "red")
plt.plot(x, y, linewidth = 2, color="#ABCDEF")
plt.xlabel('x')
plt.ylabel('$y = 2(x+5)^2$')
plt.title("Graph for the parabola of $y = 2(x+5)^2$")
plt.show()
```
## Proof of work
![image](https://github.com/user-attachments/assets/70218e6f-b0da-47eb-995f-4760f8b7da5f)

<img width="768" alt="Image_20241105_195838" src="https://github.com/user-attachments/assets/b4ae2575-da5b-44e0-969d-595861d3510f">
