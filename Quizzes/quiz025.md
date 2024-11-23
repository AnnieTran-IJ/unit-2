# Quiz 025

## Paper Solution


## Code
```.py
def count_letters(lexicon: dict, msg: str) -> dict:
    msg = msg.lower()
    for letter in lexicon.keys():
        lexicon[letter] = msg.count(letter)
    return lexicon

#test:
lexicon1 = {'w': 0, 'l': 0, 'c': 0}
msg1 = "hello world"
result1 = count_letters(lexicon1, msg1)
print(result1)

lexicon2 = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
msg2 = "Why did I choose CS?"
result2 = count_letters(lexicon2, msg2)
print(result2)
```
## Proof of work
![image](https://github.com/user-attachments/assets/fc509134-045b-4773-828c-dc53cae597fa)
