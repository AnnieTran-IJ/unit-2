# Quiz 017
## Paper Solution
![image](https://github.com/user-attachments/assets/dbbfc2f3-d6d8-4290-bb8d-18d7711f4724)

## Code
```.py
def truth_table(n:int):
    for i in range(n):
        print(f"bit{i}", end=" | ")
    print()
    for i in range(2 ** n):
        binary_string = f"{i:0{n}b}"
        for bit in binary_string:
            print(bit, end="   | ")
        print("\n")

#3 inputs
truth_table(3)
```
## Proof of work
![image](https://github.com/user-attachments/assets/96bccf39-9179-49e6-b9ad-bdc71ca1dc20)

## b.Truth table and circuit for: Light = S1S2+(S2+S3(notS1))S1 
![image](https://github.com/user-attachments/assets/74285339-177e-49b6-b1fc-b159e013a06c)
