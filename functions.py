# Creating the functions class containing all the calculator functions

class Functions:
    def __init__(self):
        pass

    def add(self, numbers):
        total = numbers[0]
        for i in range (len(numbers)):
            if i != 0:
                total += numbers[i]
            else:
                print("Why add 0?")
        return total

    def subtract(self, numbers):
        total = numbers[0]
        for i in range (len(numbers)):
            if i != 0:
                total -= numbers[i]
            else:
                print("Why Subtract 0?")
        return total

    def multiply(self, numbers):
        total = numbers[0]
        for i in range (len(numbers)):
            if i != 0:
                total *= numbers[i]
            else:
                print("Cannot multiply by 0")
        return total

    def divide(self, numbers):
        total = numbers[0]
        for i in range (len(numbers)):
            if i != 0:
                total /= numbers[i]
            else:
                print("Cannot divide by 0")
        return total

    def modulus(self, numbers):
        total = numbers[0]
        for i in range(len(numbers)):
            if i != 0:
                if total % numbers[1]:
                    total = True
                else:
                    total = False
            else:
                print("Cannot modulus by 0")
        return total