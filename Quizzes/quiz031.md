# Quiz 031
## Code
```.py
import matplotlib.pyplot as plt

x1 = [x/100 for x in range(-200,200)]
y1 = [x*x for x in x1]
y2 = [x*x*-1 for x in x1]

ya = [y/100 for y in range(-200,200)]
xa = [y*y for y in ya]
xb = [y*y*-1 for y in ya]

plt.plot(x1, y1, color='red', label='Parabola 1 (X-axis)')
plt.plot(x1, y2, color='gray', label='Parabola 2 (X-axis)')
plt.plot(xa, ya, color='purple', label='Parabola 3 (Y-axis)')
plt.plot(xb, ya, color='blue', label='Parabola 4 (Y-axis)')  # Add this without a duplicate label to avoid redundancy

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()
```
## Proof of work
![image](https://github.com/user-attachments/assets/81079fb5-9358-44aa-b54f-eff939f4b10a)
