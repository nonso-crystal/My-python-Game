


print("Welcome to python tip calculator\n")

bill=float(input("What is your total bill.\n$"))
tip=input("What percentage tip will you give.10 12 15\n")
split_bill=int(input("How many people to split the bill.\n"))
tip_as_percent=int(tip)/100 
bill_tip=bill*tip_as_percent
Messi=bill+bill_tip
Ronaldo=Messi/split_bill
salah=round(Ronaldo,2)
total_amount=print(f"Each person should pay ${salah} ")