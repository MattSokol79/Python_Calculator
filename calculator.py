# Creating the calculator
from functions import Functions

class Calculator(Functions):
    def __init__(self):
        super().__init__()

    def calculation(self):
        print("Select function")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5.Modulus")

        while True:
            # Ask user for function
            function = int(input("Enter what function would you like to execute (1,2,3,4,5)\n => "))

            if function in [1, 2, 3, 4, 5]:
                numbers = input("What are your values?\n Format: No. No. No. \n --> ").split(" ")

                for i in range(len(numbers)):
                    numbers[i] = int(numbers[i])

                if len(numbers) > 1:
                    digits = True

                    if digits:
                        if function == 1:
                            print(self.add(numbers))
                        elif function == 2:
                            print(self.subtract(numbers))
                        elif function == 3:
                            print(self.multiply(numbers))
                        elif function == 4:
                            print(self.divide(numbers))
                        elif function == 5:
                            print(self.modulus(numbers))
                    else:
                        print("You need to provide integer numbers!")
                else:
                    print("You need to provide more than 1 value to calculate")
            else:
                print("Sorry that choice is not on the list")

test = Calculator()

print(test.calculation())

