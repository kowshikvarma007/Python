# Remove and reverse a string
strValue = input('Enter string:')
print(strValue.replace(strValue[0:3],"")[::-1]),print("\n"),
# Arithmetic operations
num1 = input('Enter first number:')
num2 = input('Enter second number:')
fNum = int(num1)
sNum = int(num2)
print('Addition of two numbers is :' + str(fNum + sNum)),
print('Subtraction of two numbers is :' + str(fNum - sNum)),
print('Multiplication of two numbers is :' + str(fNum*sNum)),
print('Division of two numbers is :' + str(fNum / sNum)),
print('Modulo of two numbers is :' + str(fNum % sNum)), print("\n"),
# String replacements
iString = input('enter a sentence:')
print(iString.replace('python','pythons')),
