from string import digits,ascii_letters
import random

print(digits)
print(ascii_letters)
print("Raju")
listvalue=['A1','A2','A3','A4','A5','A6','A7','A8','PP']
for val in range(1,11):
    print(random.choices(listvalue,k=2))
print("Sample Function ")
for val in range(1,11):
    print(random.sample(listvalue,2))    