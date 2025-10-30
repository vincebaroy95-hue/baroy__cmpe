strFullName = "Vince A. Baroy"
intLength = len(strFullName)
print(strFullName)
print(intLength)
print(strFullName[0])
print(strFullName[6])
print(strFullName[9])
print(strFullName[intLength-4])
mySubstring = strFullName[2:5:3]
print(mySubstring)
strFullName = strFullName
print(strFullName)
newValue = strFullName.upper()
print(newValue)
newValue = strFullName.capitalize()
print(newValue)
newValue = strFullName.split(" ")
print(newValue)
newValue = strFullName.replace("Vince", " ")
print(newValue)
myFirstName = "Monkey"
myMiddleName = "D"
myLastName = "Luffy"

myFullNameList = [myFirstName, myMiddleName, myLastName]

print("Wanted".join([myFirstName, myMiddleName, myLastName]))
print("Wanted".join(myFullNameList))
newValue = strFullName.count("e")
print(newValue)

myChar = strFullName[2]
print(myChar)
intIndex = strFullName.index("y")
print(intIndex)
intA = 25
intB = 15
intC = 5

# arithmetic operations
intSum = intA + intB + intC
print(intSum)

intDiff = intA - intB
print(intDiff)

intProd = intA * intB
print(intProd)

intQu = intA / intB
print(intQu)

intResult = intA ** intB
print(intResult)
import math


intAngle = 9
result = round(math.cos(math.radians(intAngle)), 1)
print(result)

result = round(math.sin(math.radians(intAngle)), 1)
print(result)

result = round(math.tan(math.radians(intAngle)), 1)
print(result)

intAngle = 45
result = round(math.tan(math.radians(intAngle)), 1)
print(result)

intX = 5  # 5! = 5×4×3×2×1
facResult = math.factorial(intX)
print(facResult)

# BOOLEAN DATATYPE True or False
# "True" - String
# True  - Boolean
# 1 or 0 - Integer

intA = 5
intB = 8

isResult = intA == intB
print(isResult)  # False
isResult = intA <= intB
print(isResult)  # True

isResult = intA != intB
print(isResult)  # True

isResult = intA >= intB
print(isResult)  # False

isResult = intA < intB
print(isResult)  # True

isResult = intA > intB
print(isResult)  # False


#Membership operator in, not in
isResult = "a" in "abracadabra"
print(isResult) #True

isResult = "e" in "references"
print(isResult) #True

myList = ["bread", "nescafe", "joy", "alcohol", "tissue", "paper cup"]
isResult = "biscuit" in myList
print(isResult) #False

myList = ["bread", "nescafe", "joy", "alcohol", "tissue", "paper cup", "biscuit"]
isResult = "biscuit" in myList
print(isResult) #True


