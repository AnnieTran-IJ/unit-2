# Quiz 032
## Paper Solution
![image](https://github.com/user-attachments/assets/1eded281-f3ce-451a-80af-9c52bcc6af86)

## Code
```.py
def mystery(a:int, b:int)->list:
    output = []
    for i in range(a):
        for r in range(b):
            if i == r:
                output.append(i)
    return output

print(mystery(7,5))
```
## Proof of work
*Run it with the input and output given*
![image](https://github.com/user-attachments/assets/3984e930-b366-44ac-ba11-66fd9f37d011)
