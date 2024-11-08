# Quiz 018

## Paper Solution
![image](https://github.com/user-attachments/assets/3d8efc2b-cce1-4e99-99c0-dde1f3be97dd)

## Code
```.py
header_name = ["A","B", "C" , "AB+(not B)+not(CB)"]
def truth_table():
    for i in range(4):
        print(f"{header_name[i]}", end=" | ")
    print()
    for i in range(8):
        binary_string = f"{i:03b}"
        A = int(binary_string[0])
        B = int(binary_string[1])
        C = int(binary_string[2])
        for bit in binary_string:
            result = (A and B) or (not B) or not(C and B)
        print(f"{A}   | {B}   | {C}   | {int(result)}")
        print("\n")

truth_table()
```
## Proof of work
![image](https://github.com/user-attachments/assets/77c71eb6-ade3-4ac7-8c30-34b38c61908f)

<img width="707" alt="Image_20241105_194245" src="https://github.com/user-attachments/assets/14fcf209-adeb-45b4-b3a2-1a3ad8296781">
