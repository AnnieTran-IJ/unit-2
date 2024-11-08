# Quiz 022
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
    n = start + step * i
    x.append(n)
    if n >= 0:
        y.append(n)
    if n < 0:
        y.append(n*-1)
        
plt.plot(x, y, linewidth = 2, color="#ABCDEF")
plt.xlabel('x')
plt.ylabel('$y = |x|$')
plt.title("Graph for the parabola of y = |x|")
plt.show()
```
## Proof of work
<img width="809" alt="Image_20241105_204030" src="https://github.com/user-attachments/assets/b05f17a3-5019-407b-a0e2-7416067038ea">

