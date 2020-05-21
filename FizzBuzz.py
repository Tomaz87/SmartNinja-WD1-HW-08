print("Wellcome to FizzBuzz game!")

# The % is a Modulus and when it is = 0 it tels that a number divided by other number doesn't have a remainder.

x = int(input("Please enter a number between 1 and 100: "))

for x in range(1, x+1):
    if x % 3 == 0 and x % 5 == 0:   # you have to write conditions for both first. Otherwise it won't work properly.
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)

print("The result is above :)")