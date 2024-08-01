person = {
    "name": "Alice",
    "age": 25
}

print("Name:", person["name"])
print("Age:", person["age"])

person["city"] = "Wonderland"
print("City:", person["city"])

for key, value in person.items():
    print(key, ":", value)
