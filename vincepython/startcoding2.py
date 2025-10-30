myInput = '1231he1231312lo2313 23123231w231orld123'

myOutput = ""

for char in myInput:
    if not char.isnumeric():  # kung ang sagot mo ay hindi number, pasok ka
        myOutput = myOutput + char

print(myOutput)

# NOT, AND, OR ---- NAND, NOR, XOR, EXNOR
# LOGIC CIRCUITS AND SWITCHING THEORY

isGroupPassed = False
passingGrade = 85
markGrade = 75
jennyGrade = 90
arthurGrade = 86

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
remainder = intA % intB   # modulus (%) returns the remainder
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
