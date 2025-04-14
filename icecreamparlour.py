ice_cream=["vanilla","chocolate","mint","strawberry","bubble gum"]

print ("here are the ice cream flavours")
print (ice_cream)

ice_cream.append("cookies and cream")
print (ice_cream)

ice_cream.insert(1,"banana")
print (ice_cream)

ice_cream += ("birthday cake","orange")
print(ice_cream)

ice_cream.extend(["blueberry","pistacio","rasberry"])
print(ice_cream)

ice_cream.pop()
print (ice_cream)

ice_cream.remove("orange")
print (ice_cream)

del ice_cream[7]
print (ice_cream)

#ice_cream.clear()

ice_cream.sort()
print (ice_cream)

ice_cream[0]="caramel"
print (ice_cream)

for ice in ice_cream:
    print (ice)

ice_cream.reverse()
print (ice_cream)