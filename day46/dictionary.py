dict={"name":"anchal","state":"rajasthan","age": 20 ,"caste":"obc"}
print(dict["caste"][1])
print(dir(dict))
print(dict.get("age"))
print(dict.get("r"))
print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.popitem())
print(dict.setdefault("state"))
print(dict.pop(("age")))


dict={"name":"anchal","state":"rajasthan","age": 20 ,"caste":"obc"}
for x in dict:
    print(x)
    print(dict[x])