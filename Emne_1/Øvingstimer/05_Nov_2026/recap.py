kevin = "Kevin er tøff" # String  / str()
alder = 25              # Integer / int()
høyde = 185.7           # Float   / float()
vekkeklokke = True      # Boolean / bool()
hund = "120"

print(f"Heisann! Jeg er {alder} år")

var1 = input("Hva heter du? ")
print(var1)

# Typecast
alder_ny = str(alder)
kevin_ny = int(hund)

# Betingelser
if alder < 18:
    print("Du er ikke gammel nok :( ")
    
    if høyde > 160:
        print("Du er høy")
else:
    print("Du er gammel nok :) ")
    

    