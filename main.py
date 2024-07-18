print("welcome to the tip calculator")
bill = int(input("what was the total bill? $ "))
tipCalc = int(input("how much tip did you want to give: 10,12 or 15? "))
tip = tipCalc / 100
billPlusTip = bill + (bill * tip)
people = int(input("how many people to split the bill?"))
BillPlusTipPlusPeople = billPlusTip / people
print(BillPlusTipPlusPeople)