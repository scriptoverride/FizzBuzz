# after i learnt how to use modulus i found this solution. I still think there is a better way

for i in range(100):
    if ((i + 1) % 3 == 0) and ((i + 1) % 5 == 0): print("FizzBuzz")
    elif ((i + 1) % 3 == 0): print("Fizz")
    elif ((i + 1) % 5 == 0): print("Buzz")  
    else: print(i + 1)
