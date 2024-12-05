# Quiz 026

## Paper Solution
![image](https://github.com/user-attachments/assets/48c1a8ea-0996-4dcc-b56c-06ce92d6dbbf)

## Code
```.py
def flip(in_dict:dict):
    output= {}
    for k, v in in_dict.items():
        if v not in output:
            output[v] = [k]
        else: output[v].append(k)
    return output

#test"
in_dict_1 = {'a':1,'b':2,'c':3}
result1 = flip(in_dict_1)
print(result1)

in_dict_2 = {'bob':26,'alice':30,'carl':40}
result2 = flip(in_dict_2)
print(result2)

in_dict_3 = {'q1':True,'q2':False,'q3':True}
result3 = flip(in_dict_3)
print(result3)
```
## Proof of work
![image](https://github.com/user-attachments/assets/80f1b739-c175-410f-833f-a9f60e4dc61b)

b) Add the binary numbers 1011 and 1101 and express the result in binary.
<img width="1180" alt="Image_20241127_083503" src="https://github.com/user-attachments/assets/47e19ef1-5ed8-42f1-9d8f-0c768f81b314">
