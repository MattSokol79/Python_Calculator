# Creating the functions class containing all the calculator functions

class Functions:
    def __init__(self):
        pass

    def add(self, numbers):
        total = numbers[0]
        for i in range (len(numbers)):
            if i != 0:
                total += numbers[i]
        return total

    def subtract(self, numbers):
        total = numbers[0]
        for i in range (len(numbers)):
            if i != 0:
                total -= numbers[i]
        return total

    def multiply(self, numbers):
        total = numbers[0]
        for i in range (len(numbers)):
            if i != 0:
                total *= numbers[i]
        return total

    def divide(self, numbers):
        total = numbers[0]
        for i in range (len(numbers)):
            if i != 0:
                total /= numbers[i]
        return total

    def modulus(self, numbers):
        total = numbers[0]
        for i in range(len(numbers)):
            if i != 0:
                if total % numbers[1]:
                    total = True
                else:
                    total = False
        return total