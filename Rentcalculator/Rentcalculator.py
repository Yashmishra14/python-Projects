rent =int(input("enter your rent:"))


food=int(input("Enter Your food expenses:"))


electricity=int(input("Enter your electricity bill:"))
charge_per_unit=int(input("Enter charge per unit:"))
person=int(input("Enter number of persons living in the room/flat:"))
total=(rent+food+electricity+(electricity*charge_per_unit))/person
print("Total amount You have to pay is",total)