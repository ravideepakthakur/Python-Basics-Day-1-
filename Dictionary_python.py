mydict = {"name": "ravi", "age": "25","city":"vadodara"} 
print(mydict)

mydict2 = dict(name="rohan", age="26", city="aurangabad")
print(mydict2)

mydict["email"] = "ravi@xyz.com"
print(mydict)

mydict2["email"] = "rohan@xyz.com"
print(mydict2)

del mydict["name"]
print(mydict)

mydict2.pop("age")
print(mydict2)

mydict.popitem()
print(mydict)


if "city" in mydict:
	print(mydict["city"])


try:
	print(mydict["name"])
except:
	print("error")

for key in mydict.keys():
	print(key)

for value in mydict.values():
	print(value)


for key, value in mydict.items():
	print(key, value)

mydict.update(mydict2)
print(mydict)

