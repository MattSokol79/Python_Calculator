# Creating the calculator
from functions import Functions

class Calculator(Functions):
    def __init__(self):
        super().__init__() # Inherits the calculator functions
    # Prompts the user of the different calculator functions available
    def calculation(self):
        print("Select function")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5.Modulus")

        while True:
            # Ask user for their desired calculator function
            function = int(input("Enter what function would you like to execute (1,2,3,4,5)\n => "))
            # Checks if the input matches the available functions
            if function in [1, 2, 3, 4, 5]:
                numbers = input("What are your values?\n Format: No. No. No. \n --> ").split(" ")   # Changes the input into a list with .split()
                # Changes the values inputted into int
                for i in range(len(numbers)):
                    numbers[i] = int(numbers[i])
                # Makes sure there are more than 2 inputs so a calculation can be made
                if len(numbers) > 1:
                    digits = True
                    # If the input is more than 1, do the calculation as selected:
                    if digits:
                        if function == 1:
                            print("Answer => " + str(self.add(numbers)))
                        elif function == 2:
                            print("Answer => " + str(self.subtract(numbers)))
                        elif function == 3:
                            print("Answer => " + str(self.multiply(numbers)))
                        elif function == 4:
                            print("Answer => " + str(self.divide(numbers)))
                        elif function == 5:
                            print("Answer => " + str(self.modulus(numbers)))
                        # Break once the calculation is complete
                        break
                    else:
                        print("You need to provide integer numbers!")
                else:
                    print("You need to provide more than 1 value to calculate")
            else:
                print("Sorry that choice is not on the list")
    def triangle_area(self):
        base = float(input("What is the length of the base?\n -> "))
        height = float(input("What is the length of the height?\n -> "))
        return "Area of the triangle is:\n -> " + str(0.5 * base * height)

    def cm_to_inch(self):
        cm = float(input("What is the length in cm?\n -> "))
        return "{:.2f}".format(cm / 2.54)

    def inch_to_cm(self):
        inches = float(input("What is the length in inches?\n -> "))
        return "{:.2f}".format(inches * 2.54)

def main():
    # Calling an object of the Calculator() class
    test = Calculator()

    print(test.calculation())
    print(test.triangle_area())
    print(test.cm_to_inch())
    print(test.inch_to_cm())

if __name__ == '__main__':
    main()