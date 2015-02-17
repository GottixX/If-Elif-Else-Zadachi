a = input ("Enter a: ")
b = input ("Enter b: ")
oper = input ("Enter operation:")
a = int(a)
b = int(b)
result = False

if oper == "+":
    result =  a + b
elif oper == "-":
    result = a - b
elif oper == "*":
    result = a * b
elif oper == "/":
    result = a / b

if result != False:
    print("Result is: " + str(result))
else:
    print ("We don't support this opperation")
