weight = float(input("Enter Weight: "))
unit = input("(K)g or (L)bs: ")


if unit.upper() == 'K':
    pound = weight / 0.45
    print ("Weight in Lbs: " + str(pound))
elif unit.upper() == 'L':
    kg = weight * 0.45
    print ("Weight in KG: " + str(kg))
else:
    print("Nothing more")