"""In this exercise, you have to implement a calculator that can perform addition, subtraction, multiplication, and division.

Problem statement Write a Python class called Calculator by completing the tasks below:

Task 1

👉 Initializer

Implement an initializer to initialize the values of num1 and num2. Properties

• num1
• num2
Task 2

👉 Methods

• add() is a method that returns the sum of num1 and num2.
• subtract() is a method that returns the subtraction of num1 from num2.
• multiply() is a method that returns the product of num1 and num2.
• divide() is a method that returns the division of num2 by num1.
Input - Pass numbers (integers or floats) in the initializer.

Output - addition, subtraction, division, and multiplication

Sample input

obj = Calculator(10, 94)
obj.add()
obj.subtract()
obj.multiply()
obj.divide()
Sample output

104
84
940
9.4
Coding exercise"""

class Calculator:
    op =0
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        op = self.num1 +self.num2
        print("Addition : ",op)
        
    def subtract(self):
        op =abs(self.num1 - self.num2)
        print("Substraction : ",op)
        
    def multiply(self):
        
        op =self.num1 * self.num2
        print("multiplication :",op)
        
    def divide(self):
        if self.num1>self.num2:
            op =self.num1 / self.num2
            print("division :",op)
        if self.num2>self.num1:
            op =self.num2 / self.num1
            print("division :",op)
obj= Calculator(10,94)
obj.add()
obj.subtract()
obj.multiply()
obj.divide()