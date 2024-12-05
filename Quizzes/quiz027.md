# Quiz 027
## Paper Solution
![Uploading image.png…]()

## Code
```.py
#a) Create a function sorts a dictionary by its values in ascending order.
def sort(in_dict: dict) -> dict:
    output = {}
    for _ in range(len(in_dict)):
        min_k = None
        min_v = None
        for k, v in in_dict.items():
            if min_k is None or str(v) < str(min_v):
                min_v = v
                min_k = k
        output[min_k] = min_v

        # Remove the processed key-value pair from the input dictionary
        del in_dict[min_k]

    return output

in_dict_1 = {'apple':5, 'banana': 2, 'orange': 8, 'grape': 1}
result1 = sort(in_dict_1)
print(result1)

in_dict_2 = {'python': 3, 'java': 8, 'c++': 5, 'javascript': 2}
result2 = sort(in_dict_2)
print(result2)

in_dict_3 = {'apple': 'red', 'banana': 2, 'orange': 'orange', 'grape': 1, 'kiwi': 'brown', 'pear': 8}
result3 = sort(in_dict_3)
print(result3)

#b) Create the graph of the function y=sin(2*pi*x) 0<x<1
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(2 * np.pi * x)

x = []
y = []

for i in range(1001):
    value = i / 1000
    x.append(value)
    y.append(f(value))

plt.plot(x, y, label=r'$y = \sin(2\pi x)$')
plt.title(r"Graph of $y = \sin(2\pi x)$ for $0 < x < 1$")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

```
## Proof of work
a)
![image](https://github.com/user-attachments/assets/a28d64e2-5de5-475d-a210-de318444a3c2)

b) 
![image](https://github.com/user-attachments/assets/215f4a2d-11b4-4c53-9920-4aa54216fcf2)
