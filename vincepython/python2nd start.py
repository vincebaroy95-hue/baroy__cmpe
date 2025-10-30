#LIST
#CRUD - CREATE(append, insert)  READ(view)  UPDATE(assign value by index)  DELETE(pop, remove, clear)

fruitsA = ["apple", "apple", "orange", "banana", "grapes"]
print(fruitsA)
fruitsA.append("rambutan")

print(fruitsA)
fruitsA.insert(2, "lychee")

print(fruitsA)
print(fruitsA.index("banana"))
fruitsA[4] = "pineapple"
print(fruitsA)
print(len(fruitsA))
print(fruitsA.count("apple"))
fruitsA.remove("apple")
print(fruitsA)
fruitsA.insert(5, "ramburat")
print(fruitsA)
print(fruitsA[4])
fruitsA.clear()
print(fruitsA)

#LIST
#CRUD - CREATE(append, insert)  READ(view)  UPDATE(assign value by index)  DELETE(pop, remove, clear)

fruitsA = ["apple", "apple", "orange", "banana", "grapes"]
fruitsB = ["banana", "mango", "lychee", "orange", "mango"]
fruitsC = ["mango", "grapes", "apple", "mango", "lychee"]

fruitBasket = [fruitsA, fruitsB, fruitsC]
print(fruitBasket)
print(fruitBasket[2][3])

#LIST OF A different data types and List
myInfoList = ["Binsoy", 18, True, ["Basketball", "Gym", "Anime"]]
print(myInfoList[0])
print(myInfoList[1])
print(myInfoList[2])
print(myInfoList[3])
print(myInfoList[3][1])

#TUPLE
fruitsA = ("apple", "apple", "orange", "banana", "grapes")
print(fruitsA[3])

#fruitsA[3] = "pineapple" - not supported, immutable
print(fruitsA[3])

print(fruitsA.count("apple"))

fruitsB = ("banana", "mango", "lychee", "orange", "mango")
fruitsC = ("mango", "grapes", "apple", "mango", "lychee")

fruitBasket = (fruitsA, fruitsB, fruitsC)
print(fruitBasket[2][4])

# SET {} CURLY BRACE
fruitsA = {"apple", "orange", "banana", "grapes"}
fruitsB = {"grapes", "apple", "mango", "Lychee"}
#print(fruitsA)

fruitsUnion = fruitsA.union(fruitsB)
print(fruitsUnion)

fruitsIntersection = fruitsA.intersection(fruitsB)
print(fruitsIntersection)

fruitsDifference = fruitsA.difference(fruitsB)
print(fruitsDifference)

fruitsUnionB = fruitsA | fruitsB
print(fruitsUnionB)

fruitsIntersectionB = fruitsA & fruitsB
print(fruitsIntersectionB)

fruitsDifferenceB = fruitsA - fruitsB
print(fruitsDifferenceB)

print(fruitsDifference)

fruitsDifferenceB = fruitsA - fruitsB
print(fruitsDifferenceB)

# SUBSET
fruitsA = {"apple", "orange", "banana", "grapes"}
fruitsB = {"grapes", "apple", "mango", "Lychee"}
fruitsC = {"orange", "banana"}
fruitsD = {"orange", "chico"}

print(fruitsC.issubset(fruitsA))  # is fruitsC a subset of fruitsA
print(fruitsD.issubset(fruitsA))  # is fruitsD a subset of fruitsA

# DICTIONARY - dict - CURLY BRACES, KEY-VALUE PAIR

myInfo = {"Name": "Vince Baroy", "Age": 18, "Citizenship": "Filipino"}
print(myInfo)

print(myInfo["Name"])
print(myInfo.get("Name"))
print(myInfo["Age"])
print(myInfo.get("Age"))
print(myInfo["Citizenship"])
print(myInfo.get("Citizenship"))

myInfo.update({"Address": "Biringan"})
print(myInfo)

myInfo.update({"Age": 99})  # update
print(myInfo)

myInfo["Age"] = 999  # assigned value
print(myInfo)


myInfo = {
    "Name": {
        "FirstName": "Vince",
        "LastName": "Baroy"
    },
    "Age": 18,
    "Citizenship": "Filipino",
    "Hobbies": [
        "Working out",
        "Watching anime",
        "Playing ml"
    ]
}

print(myInfo)
print(myInfo["Name"]["FirstName"])
print(myInfo["Name"]["LastName"])
print(myInfo["Name"]["FirstName"] + " " + myInfo["Name"]["LastName"])
print(myInfo["Age"])
print(myInfo["Hobbies"][2])

myListOfDictionary = [
    {'fruit': 'Apple'},
    {'fruit': 'Grapes'},
    {'fruit': 'Banana'}
]

print(myListOfDictionary[2])
print(myListOfDictionary[2]['fruit'])




