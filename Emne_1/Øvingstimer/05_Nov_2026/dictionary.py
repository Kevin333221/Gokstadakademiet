# Dict: Nøkkel  :   Verdi
# Dict: Key     :   Value

var1 = {
    "kevin": "Kul fyr",
    "hund": "et dyr",
    "katt": 20,
    "hest": [1, 2, 3, 4, "Kevin"]
}

print(var1)

var2 = var1["kevin"]
print(var2)

var1["mus"] = 100

# print(var1.keys())
# print(var1.values())

for x in var1.keys():
    print(f"Nøkkel: {x}")
    print(f"Verdi: {var1[x]}")