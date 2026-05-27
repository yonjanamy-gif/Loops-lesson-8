actual_cost = int(input("Please Enter the Actual Product Price: "))
sale_amount = int(input("Please Enter the Sales Am)ount: "))
if (sale_amount > actual_cost):
    profit = sale_amount - actual_cost
    print("Total Profit= ", profit, end="$")
else:
    loss = actual_cost - sale_amount
    print("Total Loss= ", loss, end="$")