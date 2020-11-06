# Creating the calculator

class Calculator:

    def add(self, numbers):
        total = numbers[0]
        for i in range (len(numbers)):
            if i != 0:
                total += numbers[i]
            else:
                print("No need to add 0?")
        return total

    def subtract(self, numbers):
        total = numbers[0]
        for i in range (len(numbers)):
            if i != 0:
                total -= numbers[i]
            else:
                print("No need to subtract 0?")
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

