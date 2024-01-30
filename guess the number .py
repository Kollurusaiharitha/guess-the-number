from random import randint

random_number = randint(0,10)
print(random_number)
x = -1
x =  int(x)
while x != random_number:
    if x != -1:
        print("you guessed wrong")
    x = input("Enter a number: ")
    x = int(x)
    print("you guessed correctly")
    
