
print("Hello word")
print('Hello word')
print('Coco Martin said')


input("Enter your name :")



print("Sir Leonel said \"Bat ambilis mo natapos?\"")

print("Pwede ba chatgpt sir?")
print(input("Enter your respone: "))


firstName = input("Enter your first name:")
lastName = input("Enter your last name:")

print("Your Full name is: "+ firstName + " " + lastName)

print("First Line")
print("Second Line")
print("Third Line")
print("Fourth Line")
print("Fifth Line")
print("Sixth Line")
print("Seventh Line")



#this is a single line comment
print("Ano jo pagod ka na jo?")

''' comment
pagod 
na pagod
na
pagod na ako'''



#this is a single line comment
print("Ano jo pagod ka na jo?")

''' comment
pagod 
na pagod
na
pagod na ako'''



strFullName = "Vince Baroy"
intLength = len(strFullName) #len for length

#function call - ()
#range or index - []
#list []

print (strFullName)
print(intLength)
print(strFullName[0])
print(strFullName[5])
print(strFullName[6])
print(strFullName[14])
print(strFullName [intLength-1])

mySubString = strFullName[0:4:1] #will get character 0-3
print(mySubString)

strFullName = strFullName + "a"
print(strFullName)





strFullName = "Vince Baroy"

#string methods

newValue = strFullName.upper()
print(newValue)
newValue = strFullName.lower()
print(newValue)
newValue = strFullName.capitalize()
print(newValue)

newValue = strFullName.split(" ")
print(newValue)
newValue = strFullName.split("ho")
print(newValue)


newValue = strFullName.replace("e", "a")
print(newValue)
newValue = strFullName.replace("bins", "HOTDOG")
print(newValue)
newValue = strFullName.replace("e", " ")
print(newValue)


myFirstName = "Vince"
myMiddleName = "Anghag"
myLastName = "Baroy"

myFullNameList = [myFirstName, myMiddleName, myLastName]

print("dipogi".join([myFirstName, myMiddleName, myLastName]))
print("mabaitnalang".join(myFullNameList))

newValue = strFullName.count("a")
print(newValue)

myChar=strFullName[2]
print(myChar)
intIndex = strFullName.index("h")
print(intIndex)


#Numeric type
#Integer -10,0,2324
#Float 25.232
#Complex 25 + 47 j #i = ampere, j impedance -> resistance + reactance
import math

intA = 25
intB = 15
intC = 5

#arithmetic operations
intSum = intA + intB + intC
print(intSum)
intDiff = intA - intB
print(intDiff)
intProd = intA * intB
print(intProd)
intQuot = intA / intB
print(intQuot)
intResult = intA ** intB
print(intResult)


intAngle = 90
result = round(math.cos(math.radians(intAngle)), 1)
print(result)
result = round(math.sin(math.radians(intAngle)), 1)
print(result)
result = round(math.tan(math.radians(intAngle)), 1)
print(result)

intAngle =45
result = round(math.tan(math.radians(intAngle)), 1)
print(result)

intX = 5 #5!
facResult = math.factorial(intX)
print(facResult)


myComA= 25+5j
myComB = 10-10j
comProd = myComA * myComB
print(comProd)

#Comparison Operator
# ==,>,<,>=,<=,!=
#BOOLEAN DATATYPE True or False
#"True" 'True' - String
# 1 or 0 - Integer

intA = 5
intB = 6

isResult = intA == intB
print(isResult)

isResult = intA <= intB
print(isResult)

isResult = intA >= intB
print(isResult)

isResult = intA != intB
print(isResult)

isResult = intA > intB
print(isResult)

isResult = intA < intB
print(isResult)



#membership operator included (in), (not in)
isResult = "e" in "madagascar"
print(isResult)
isResult = "e" in "bebetime"
print(isResult)

myListofEssentials = ["bearbrand", "nescafe", "joy", "alcohol", "tissue", "papercup"]
isResult = "bebetime" in myListofEssentials
print(isResult)
myListofEssentials = ["bearbrand", "nescafe", "joy", "alcohol", "tissue", "papercup","bebetime"]
isResult = "bebetime" in myListofEssentials
print(isResult)

isResult = "bebe" in "bebetime"
print(isResult)

#identity operator is, is not
isResult = "bebe" is "bebetime"
print(isResult)
isResult = "bebetime" is "bebetime"
print(isResult)


isMyResult = isResult is True
print(isMyResult)


myInput= "123k2a1i3l2a1n372g18a2n1 254k280o3 93n19a31 9n82g1 87231b9e38b21e309t12i31m83e71 93n2a13n21g3h09i02h1i03n10a9321 721n9a32k9o131"

myOutput = ""

for char in myInput:
    if not char. isnumeric():
        myOutput = myOutput + char

print(myOutput)


myInput = input("Ano kailangan mo?: ")
myOutput = ""

for char in myInput:
    if not char. isnumeric():
        myOutput = myOutput + char

print(myOutput)




#Logical Operator
# Not, And, Or ------ NAND, NOR, EXOR, EXNOR
#LOGIC CIRCUITS AND SWITCHING THEORY


isGroupPassed = False

passingGrade = 85
markGrade = 75
jennyGrade = 95
arthurGrade =86

isMarkPassed = markGrade >= passingGrade
print(isMarkPassed)
isJennyPassed = jennyGrade >= passingGrade
print(isJennyPassed)
isArthurPassed = arthurGrade >= passingGrade
print(isArthurPassed)

isGroupPassed = isMarkPassed and isJennyPassed and isArthurPassed
print(isGroupPassed)

isGroupPassed = isMarkPassed or isJennyPassed or isArthurPassed
print(isGroupPassed)



intA = 555
intB = 4
intC = 5

isDivisible = False

remainder = intA % intB #modulus or the percent sign returns the remainder
print(remainder)
if remainder == 0:
    isDivisible = True

print(isDivisible)

isDivisible = False
remainder = intA % intC
print(remainder)
if remainder == 0:
    isDivisible = True

print(isDivisible)


#List
#CRUD - CREATE(like append and insert)   READ(view)   UPDATE(assign value by index)    DELETE(pop, remove, clear)

fruitsA = ['apple', 'apple', 'orange', 'banana', 'grapes']
print(fruitsA)

fruitsA.append('rambutan')
print(fruitsA)

fruitsA.insert(2, 'lychee')
print(fruitsA)

print(fruitsA.index('banana'))
fruitsA[4] = 'pineapple'
print(fruitsA)
print(len(fruitsA))
print(fruitsA.count('apple'))

fruitsA.remove('apple')
print(fruitsA)

print(fruitsA[4])

fruitsA.clear()
print(fruitsA)


list of lists

fruitBasket = [fruitsA, fruitsB, fruitsC] #list of lists
print(fruitBasket)
print(fruitBasket[2][3])

fruitBasketAdd = fruitsA + fruitsB + fruitsC #single list
print(fruitBasketAdd)

fruitsA.extend(fruitsB)
fruitsA.extend(fruitsC)
print(fruitsA) #single list

#LIST OF A Different data type and list
myInfoList =["vince", 18, True,["cooking", "gaming", "reading"]]
print("Name:",(myInfoList[0]))
print("Age:",(myInfoList[1]))
print("Agree ka ba?:", (myInfoList[2]))
print("What are your hobbies?:",(myInfoList[3]))
print("What is your most favorite hobby?:",(myInfoList[3][0])) #specific

#TUPLE (parenthesis)
fruitsA = ('apple', 'apple', 'orange', 'banana', 'grapes')
print(fruitsA[3])
#fruitsA[3] = 'pineapple' - not supported, immutable
#print(fruitsA[3])
print(fruitsA.count("apple"))
fruitsB = ("banana", "mango","lychee","orange","mango")
fruitsC = ("mango","grapes","apple","mango","lychee")
fruitBasket = (fruitsA, fruitsB, fruitsC)
print(fruitBasket[2][4])



#SET {} CURLY BRACE
fruitsA = {'apple', 'orange', 'banana', 'grapes'}
fruitsB = {'grapes', 'apple', 'mango', 'lychee'}
#print(fruitsA)
fruitsUnion = fruitsA.union(fruitsB)
print(fruitsUnion)


fruitsUnionB = fruitsA | fruitsB
print(fruitsUnionB)

fruitsIntersection = fruitsA.intersection(fruitsB)
print(fruitsIntersection)

fruitsIntersectionB = fruitsA & fruitsB
print(fruitsIntersectionB)

fruitsDifference = fruitsA.difference(fruitsB)
print(fruitsDifference)

fruitsDifferenceB = fruitsA-fruitsB
print(fruitsDifferenceB)
#fruitsA.add("rambutan")
#print(fruitsA)

#SUBSET
fruitsA = {'apple', 'orange', 'banana', 'grapes'}
fruitsB = {'grapes', 'apple', 'mango', 'lychee'}
fruitsC = {"orange","banana"}
fruitsD = {"cherry","chico"}
print(fruitsC.issubset(fruitsA)) #is FruitsC a subset of FruitsA
print(fruitsD.issubset(fruitsA)) #is FruitsD a subset of FruitsA



#DICTIONARY - dict - CURLY BRACES, KEY-VALUE PAIR

#myInfo ={"Name": "Vince Baroy", "Age": 18, "Citizenship": "Filipino"}
myInfo = {
  "Name": "Vince Baroy",
  "Age": 18,
  "Citizenship": "Filipino"
}
print(myInfo)
print(myInfo.get("Name"))
print(myInfo["Name"])
print(myInfo.get("Age"))
print(myInfo["Age"])
print(myInfo.get("Citizenship"))
print(myInfo["Citizenship"])


myInfo.update({"Age": 20})#update
print(myInfo)
myInfo.update({"Address":"Rizal"})
print(myInfo)
myInfo["Age"] = 77 #assigned value
print(myInfo)

print(myInfo.values())
print(myInfo.keys())

for i in myInfo.keys():
    print(myInfo[i])


#myInfo ={"Name": "Vince Baroy", "Age": 19, "Citizenship": "Filipino"}
myInfo = {
    "Name":{
        "FirstName": "Vince",
        "Lastname" : "Baroy"

    },
    "Age":18,
    "Citizenship" : "Filipino",
    "Hobbies": [
        "Cooking","Gaming","Reading"
    ]
}
print(myInfo)
print(myInfo["Name"]["FirstName"])
print(myInfo["Name"]["Lastname"])
print(myInfo["Name"]["FirstName"] + " " + myInfo["Name"]["Lastname"])
print(myInfo["Age"])
print(myInfo["Hobbies"][2])

myInfo["Name"]["FirstName"] = "JP"
print(myInfo["Name"]["FirstName"])


#myInfo ={"Name": "Vince Baroy", "Age": 19, "Citizenship": "Filipino"}
balanceData = {
    "28831" : 129.25,
    "72173" : 9999999999999.25,
    "31889" : 9.25,
    "39109" : 9999999999.25,
}

accountNumber = input("Please enter your account number to check your remaining balance")
print(balanceData)[accountNumber]

#easy
myListofDictionary =[
        {"fruit:":"Apple:"},
        {"fruit:":"Grapes:"},
        {"fruit:":"Banana:"}
]

print(myListofDictionary[2])
print(myListofDictionary[2]["fruit:"])


#IF ELSE GRADING SYSTEM
myGrade =93.5

if myGrade >= 97:
    print("Grade is : 1.0") #statement body
elif myGrade >= 94:
    print("Grade is : 1.25")
elif myGrade >= 91:
    print("Grade is : 1.50")
elif myGrade >= 88:
    print("Grade is : 1.75")
elif myGrade >= 85:
    print("Grade is : 2.0")
elif myGrade >= 82:
    print("Grade is : 2.25")
elif myGrade >= 79:
    print("Grade is : 2.5")
elif myGrade >= 76:
    print("Grade is : 2.75")
elif myGrade >= 75:
    print("Grade is : 3.0")
else:
    print("Grade is : 5.0")

print("After If Else Condition")

#SHAPE OF YOU
shapeofyou = "square"

if shapeofyou == "rectangle":
    print("Your shape is a rectangle")
elif shapeofyou == "triangle":
    print("Your shape is a triangle")
elif shapeofyou == "square":
    print("Your shape is a square")
else:
    print("Your shape is unknown")

print("Next question please")


#VOTE ELIF
age = 18
citizenship ="chinese"
residency = 6 #MONTHS
isregistered = True

if citizenship == "filipino" and age >= 18 and residency >= 6:
    if isregistered:
        print("You can vote")
    else:
        print("You can't vote, Register now")
elif citizenship == "filipino" and age < 18 and residency >= 6:
    print("You can't vote yet, wait till you're eligible (18) to register")
elif citizenship == "filipino" and age >=18 and residency < 6:
    print("You can't vote yet, wait till you've achieved 6 months of residency")
else:
    print("ISPIYA LAYAS! AMIN ANG WEST PHILIPPINE SEA!")


#ELIGIBLE TO VOTE - CHECKER
#nested, if else within if. else, elif
age = input("Please enter your age ")
citizenship = input("Please enter your citizenship ")
residency = input("Please enter your months of residency ")
isregistered = input("Are you a registered voter? yes or no ")
if citizenship == "filipino" and int(age)>= 18 and int(residency)>= 6:
    if isregistered =="yes":
        print("Pag binoto moko yayaman ako ay tayo*")
    else:
            print("You cannot vote but you may register now")
elif citizenship == "filipino" and int(age)< 18 and int(residency) >=6:
    print("You cannot vote but you can wait til you're 18 and above to register")
elif citizenship =="filipino" and int(age) >= 18 and int(residency)> 6:
    print("You cannot vote but you can wait til months of residency is ss 6 months")

else:
    print("you cannot vote or register")

#range
#for (int x = 0; x < 10; x++){
print("before, loop1")
for x in range(0,10,1): #start and interval
    print(x)
print("after, loop1")
#-----
print("before, loop2")
for x in range(10): #stop
    print(x)
print("after, loop2")
#-----
print("before, loop3")
for x in range(0,10): #start and stop
    print(x)
print("after, loop3")


#for any key

fruitlist = ["apple","orange", "banana", "cherry"]

for fruit in fruitlist:
    print("Fruit List includes : " + fruit) #iteration

myWord = "pneumonoultramicroscopicsilicovolcanoconiosis"
for char in myWord:
    print(char.upper())

myInfo = {"name":"Jeho", "age":19, "school": "PUP"}
for anyKey in myInfo:
    print(anyKey)

for anyValues in myInfo.values():
    print(anyValues)

for anyKey in myInfo:
    print(anyKey, myInfo[anyKey])

myTuple = ("Nihao","Mundo","Universe","MeowMeow")
for word in myTuple:
    print(word)

mySet = {"Nihao","Mundo","Universe","MeowMeow"}
for word in Set:
    print(word)

#forloop

import time
isConnected = "no"
#for loop - break or continue
for i in range(4): #if achieve max trials/ break
    time.sleep(2)
    isConnected = input("Is connected?")
    if isConnected == "yes":
        print("Connection is successful")
        break #end the loop immediately #partner of break = continue (will go next iteration/loop
    else:
        print("Request Timeout")
    print("Retrying now in 2 seconds")
print("Processing the request now...")


myList = ["yes","yes","yes","no","yes","yes"]
for x in myList:
    if x == "no":
        print("BOI ID MO?")
        break
    print("may pasok")
    print("walang pasok")

#nested loop

for x in range (10):
    print(str(x) + "======================")
    for y in range (10):#inner loop
        print(y)
#simple code palindrome
myString = "natotorototan"
newValue = ""

for char in myString:
    newValue = char + newValue #inverted
print(newValue)
if myString.lower() == newValue.lower():
    print("PALINDROME")
else:
    print("NOT PALINDROME")

#print(myString[::-1]) #single liner inverted




#first create your own character list

charList = [
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9',  " ", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")",
"-", "_", "=", "+", "[", "]", "{", "}", ";", ":", "'", '"',
",", "<", ".", ">", "/", "?", "\\", "|", "`", "~"]

key = 5
inputMessage = "My Pin Number is 12345"
outputMessage = "" #"RD%Uns%Szrgjw%nx%6789"

indexCounter = 0

for letter in inputMessage:
    indexCounter = charList.index(letter)
    print(indexCounter)
    outputMessage = outputMessage + charList[indexCounter + key]

print(outputMessage) #---->network


#RESOLVE THE POSSIBLE INDEX ERROR PROBLEM
#GO BACK TO START

#DECRYPTION CODE <- (INPUT)--------------outputMessage
#---------------------------------------->inputMessage



#functions
#built in functions
#user defined functions
import time

#functions without parameter, and without return

def welcome_messages():
    for i in range (10, 0, -1):
        print("Counter:" + str(i))
        time.sleep(0.2)

welcome_messages()

#functions with parameter, but without return

def welcome_messages_with_input(message):
    for i in range (10, 0, -1):
        print("Counter:" + str(i))
        time.sleep(0.2)
    print(message)

welcome_messages_with_input("Happy New Year")


#functions without parameter, but with return

def welcome_messages():
    message =  ""
    for i in range (10, 0, -1):
      message = message + " " + str(i)
      time.sleep(0.2)
    return message

print(welcome_messages())


#functions with parameter, and return

def welcome_messages(message):
    for i in range (10, 0, -1):
      message = message + " " + str(i)
      time.sleep(0.2)
    return message

print(welcome_messages("This is my input"))

#example

a = 5
b = 25
c = 15
d = 45

def get_the_sum(inputA, inputB):
    sum = inputA + inputB
    return sum

final_sum = get_the_sum(a, b) + get_the_sum(c, d)
print(final_sum)

print(get_the_sum(get_the_sum(a,b), get_the_sum(c,d)))

print(get_the_sum(a,b))
a=23123
b=24323
print(get_the_sum(a,b))


import time
def any_function_name():
    """This function is a sample code for Continue and return"""
    message = "Sir, Tapos na po."
    for i in range(0,100,1):
        time.sleep(0.4)
        if i == 25:
            continue
        elif i==75:
            return message
        print("Value of i is : " + str(i))
    return None

print(any_function_name())



listofNumbers = [25, 33, 45, 67, 90]

def add_function(a,b):
    """This function is used to add two numbers and return the sum"""
    return a + b

def average_function(inputList):
    """This function is used to get and return the average"""
    totalsum = 0
    for i in inputList:
        totalsum = add_function(totalsum, i)
    average = totalsum / len(inputList)
    return average

print(average_function(listofNumbers))




#SIMPLE DEMO OF ATM WITHDRAWAL FLOW
'''
welcome_message():
card_reader(isCardDetected): return isCardInserted
input_and_validate_pin_number()
transaction_selection() #withdraw #check balance #cancel transaction
transaction_validation(amount) return isValid
card_ejection()
cash_dispensing()
print_receipt() update balance

'''
import time
amount = 5000
user1_balance = 1000
user1_pin = '123456'

def welcome_message():
    print("=================================================")
    print("Welcome to BS ECE 1-2 BANK OF THE PHILIPPINES")
    print("=================================================")
    time.sleep(1)
    print("Please Insert your Card")
    print("=================================================")
    time.sleep(1)

def card_reader(isCardDetected):
    if isCardDetected.upper() == "YES":
        print("Card is Inserted")
        return True
    else:
        return False

def card_ejection():
    "call driver of motor to reject card"
    print("Card is ejected. Please get your card")

def input_pin_number_and_validate():
    for i in range(3):
        input_pin = input("Please Insert Pin Number : ")
        if input_pin == user1_pin:
            print("Pin number is valid")
            return True
        else:
            print("Pin number is invalid. Please try again (attempt: " + str(i+1))
    print("Card is blocked due to 3 failed attempts")
    return False

def transaction_selection():
    print("Available Transactions: WITHDRAW, CHECK BALANCE, CANCEL")
    transaction= input("Please Select your Transaction: ")
    return transaction

def cash_dispense():
    #code for calling the driver for cash dispense
    print("Please get your cash quickly!")

def print_receipt():
    global user1_balance
    user1_balance = user1_balance - amount
    print("Your Balance: " + str(user1_balance))
    print("Please get your receipt")

def transaction_validation(amount):
    global user1_balance
    if amount <=0:
        print("Invalid Amount")
        return False
    if user1_balance > amount:
        print("Valid Amount to withdraw")
        return True
    else:
        print("Insufficient Amount to withdraw. Utang ka muna")
        return False


while True:
    welcome_message()
    isCardDetected = input("Is Card Detected? (YES/NO):")
    if not card_reader(isCardDetected):
        time.sleep(1)
        continue

    if not(input_pin_number_and_validate()):
        card_ejection()
        time.sleep(1)
        continue

    transaction_selected = transaction_selection()
    if transaction_selected.upper() == "WITHDRAW":
        #CODE FOR WITHDRAW
        print("Transaction Selected is WITHDRAW")
        amount = float(input("Please Enter Amount: "))
        if transaction_validation(amount):
            time.sleep(1)
            card_ejection()
            time.sleep(1)
            cash_dispense()
            time.sleep(1)
            print_receipt()
            time.sleep(1)
        else:
            card_ejection()
            continue



    elif transaction_selected.upper() == "CHECK BALANCE":
        #CODE FOR CHECKBALANCE
        print("Transaction Selected is CHECK BALANCE")
        print(user1_balance)
        card_ejection()
        continue

    else:
        print("Transaction is Canceled")
        card_ejection()
        continue


    print("Next Step")
    time.sleep(5)




from RESISTOR import resistor
from CAPACITOR import capacitor
from INDUCTOR import inductor

print("Welcome to Electronics Calculators")

while True:

    selector = input("Please select the right calculator: ")

    match selector.upper():
        case "RC_IV":
            voltage = float(input("Please enter voltage: "))
            current = float(input("Please enter current: "))
            resistor.get_resistance_by_iv(voltage, current)

        case "CC_CV":
            voltage = float(input("Please enter voltage: "))
            charge = float(input("Please enter charge: "))
            capacitor.get_capacitance_by_cv(charge, voltage)

        case "IR_C":
            frequency = float(input("Please enter frequency: "))
            inductance = float(input("Please enter inductance: "))
            inductor.get_inductive_reactance(frequency, inductance)

        case _:
            print("Invalid input")


    student1_name = "Diego"
    student1_grade = "1.5"
    student1_subject = "Algebra"

    student2_name = "Michael"
    student2_grade = "4.0"
    student2_subject = "Geometry"

    student3_name = "Shiela"
    student3_grade = "2.5"
    student3_subject = "physics"

    def print_student_info_function(name, grade, subject):
        print(f"Student {name} grade is {grade} and subject is {subject}")

    if __name__ == "__main__":
        print_student_info_function(student1_name, student1_grade, student1_name)
        print_student_info_function(student2_name, student2_grade, student2_name)
        print_student_info_function(student3_name, student3_grade, student3_name)



#ALL METHODS ARE FUNCTIONS, BUT NOT ALL FUNCTIONS ARE METHODS

class Student:#CLASS IS THE BLUEPRINT FOR CREATING OBJECT
    default_subject = "Basic Electronics"
    year_and_section = "1-2"

    def __init__(self, name, grade, subject):#CONSTRUCTOR
        self.name = name
        self.grade = grade
        self.subject = subject

    def print_student_info_method(self):#REGULAR METHOD
        print(f"Student {self.name} - grade is {self.grade} - subject is {self.subject}")

    @classmethod
    def create_student_with_default_info_method(cls, name, grade):
        print(f"Student {name} - grade is {grade} - subject is {cls.default_subject}")
        return cls(name,grade,cls.default_subject)

    @classmethod
    def update_year_and_section(cls,year_and_section_update):
        cls.year_and_section = year_and_section_update

    @staticmethod
    def is_passing_grade(grade):
        if grade <= 3.0:
            print("passed")
        else:
            print("failed")

    #----------------------------------------------------------------------------------------------
    print("#-----------------------------------------")

if __name__ == "__main__":
    student1 = Student("Rudolf",1.0, "Engineering Economy")#Instance of the class (subject)
    student2 = Student("Miguel", 2.0, "Calculus")#Instance of the class (object)
    student3 = Student("Santa", 4.0, "Energy Conversion")#Instance of the class (object)
    student4 = Student.create_student_with_default_info_method("Diyosa",1.25)

    student1.print_student_info_method()
    student2.print_student_info_method()
    student3.print_student_info_method()


    Student.is_passing_grade(5.0) #f
    Student.is_passing_grade(student1.grade) #p
    Student.is_passing_grade(student2.grade) #p
    Student.is_passing_grade(student3.grade) #f
    Student.is_passing_grade(student4.grade)

    print(student1.year_and_section)
    print(student2.year_and_section)
    print(student3.year_and_section)
    Student.update_year_and_section("2-2")
    print(student1.year_and_section)
    print(student2.year_and_section)
    print(student3.year_and_section)


import subFile

student1_name = "Mica"
student1_grade = "1.5"
student1_subject = "Biology"

#call a function from different file
#subFile.print_student_info_function(student1_name, student1_grade, student1_name)

#call a method from different file
student = subFile.Student("Michael Angelo",1.0,"Literature")
student.print_student_info_method()


import serial
import time
import threading

serialInstance = serial.Serial("COM3",9600,timeout=1)
time.sleep(2)

def send(message):
    serialInstance.write((message + '\n').encode("utf-8"))
    print(f"sent:{message}")


def receive():
    if serialInstance.in_waiting > 0:
        data=serialInstance.readline().decode("utf-8").strip()
        if data:
            print(f"received:{data}")
            return data
    return None

def received_continuous():
    while True:
        received_data = receive()
        time.sleep(0.1)

received_thread_instance = threading.Thread(target=received_continuous,daemon=True)
received_thread_instance.start()

try:
    while True:
        message = input("Enter message: ")
        if message:
            send(message)
except KeyboardInterrupt:
    print("Exit na, masakit na e")
finally:
    serialInstance.close()
import math

def get_resistance_material(resistivity, length, area):
    resistance = (resistivity * length) / area
    print(f"Resistance is {resistance} ohms")
    return resistance


def get_resistance_by_iv(voltage, current):
    resistance = voltage / current
    print(f"Resistance is {resistance} ohms")
    return resistance



if __name__ == "__main__":
    get_resistance_material(0.005, 10, 8)
    get_resistance_by_iv(3.0, 3.0)



import os
import time

print(os.getcwd())
print(os.listdir(os.getcwd()))
#os.makedirs(os.getcwd() + "/" + "new folder")
#os.makedirs(os.path.join(os.getcwd(), "new folder"))
#os.makedirs(os.path.join(os.path.join(os.getcwd(), "new folder 3")), "THIS IS A NEW FOLDER INSIDE A FOLDER")
print(os.path.dirname(os.path.abspath(__file__)))
BASE_PATH = os.path.dirname(os.path.abspath(__file__))


with open(os.path.join(BASE_PATH, "ILOVEYOU.virus"),"w", encoding="utf-8") as f:
    print("Virus is created")
    time.sleep(10)


for root, dirs, files in os.walk(BASE_PATH):
    for filename in files:
        print(filename)
        if filename == "ILOVEYOU.virus":
            print("==============================================")
            print("ILOVEYOU.virus is detected")
            print("==============================================")
            file_loc= os.path.join(root, filename)
            print(file_loc)
            os.remove(file_loc)
            time.sleep(5)
            print("ILOVEYOU.virus is deleted")
            print("==============================================")



import os
import time
import csv

BASE_PATH = os.path.dirname(os.path.abspath(__file__)) #CURRENT WORKING DIRECTORY

RESOURCE_PATH = os.path.join(BASE_PATH, "RESOURCES")
CSV_PATH = os.path.join(RESOURCE_PATH, "MYFIRSTCSV.csv")

csv_list_data = []

with open(CSV_PATH, mode = "r", newline ='') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)
        csv_list_data.append(row)

print(csv_list_data)
print(csv_list_data[1])
print(csv_list_data[1][2])


name_and_address = []

for row in csv_list_data:
    name_and_address.append([row[1], row[4]])

CSV_PATH = os.path.join(RESOURCE_PATH, "NEW_CSV.csv")

with open(CSV_PATH, mode="w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(name_and_address)



import os
import time
import gspread
from googleapiclient.errors import HttpError #google-api-python-client
from gspread.utils import ValueInputOption
from oauth2client.service_account import ServiceAccountCredentials

BASE_PATH = os.path.dirname(os.path.abspath(__file__)) #CURRENT WORKING DIRECTORY
RESOURCE_PATH = os.path.join(BASE_PATH, "RESOURCES")
SERVICE_KEY_PATH = os.path.join(RESOURCE_PATH, "baldovinocmpebsece1-2-3c4f19e4a3d7.json")

sheet_url = "https://docs.google.com/spreadsheets/d/1OzZ10XafK-VpRVU7xdDA-MUsa-QJdQLDV73kUfSaCr0/edit?gid=0#gid=0"

credentials = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_KEY_PATH, scopes=['https://www.googleapis.com/auth/spreadsheets',  'https://www.googleapis.com/auth/drive'])
client = gspread.authorize(credentials)

gs_instance = client.open_by_url(sheet_url)

sheet_instance = gs_instance.get_worksheet(0)

googlesheet_data = sheet_instance.get_all_records()
print(googlesheet_data)

row_data = ["6","Steph Curry","BSECE","1-5","MAKATI"]
sheet_instance.append_row(row_data)

