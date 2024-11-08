# Quiz 024

## Code
```.py
import random

from matplotlib import pyplot as plt
import matplotlib

plt.style.use('ggplot')  #

data =  {'x': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
'y': [24, 1, 2, 25, 26, 21, 23, 34, 49, 2, 19, 32, 7, 17, 36, 7, 45, 28, 40, 46]}

x_coordinate = []
y_coordinate = []
for i in range(20):
    x_coordinate.append(data["x"][i])
    y_coordinate.append(data["y"][i])

#y['new key'] = 'value' - add new item to the list
data['title'] = 'quiz_data_science'

plt.plot(x_coordinate, y_coordinate, "o-")
#add marker of each dots on the graph
plt.xlabel('x')
plt.ylabel('$y')
plt.title({data['title']})
plt.show()

```
## Proof of work
![image](https://github.com/user-attachments/assets/27a7f939-5899-4a59-9ee2-e1b3da02ecf5)

*Run it with the input and output given*
