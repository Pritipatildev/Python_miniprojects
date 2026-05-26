# this program is built to calculate the rent ,electricity bill and total spend on the scanking for the hostelers
rent=int(input("Enter the total rent of the flat="))
food=int(input("Enter the total food expenses="))
electricity_spends=int(input("Enter the total electricity used in units="))
rs_per_unit=int(input("Enter the charge per unit ="))
persons=input("Enter the no of persons living in flat=")

total_Electric_bill=electricity_spends*rs_per_unit

output=(rent+food+total_Electric_bill)//int(persons)

print(f"Each person will pay {output} Rs")